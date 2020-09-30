import zmq
import logging
from logging import NullHandler
import socket
from multiprocessing import Process
from czpurifier.middleware import SimulatorInterface, DeviceInterface
from os import chdir, path, kill, getpid
from signal import signal, SIGQUIT, SIGCONT, SIGUSR1, SIGTERM, SIGUSR2
from json import load
from run_purification import RunPurification
from run_custom_protocol import RunCustomProtol
from PyQt5.QtWidgets import QMessageBox
from math import ceil

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def __init__(self):
        """
        1. Controls the communication between device and controller interface and the GUI
        2. Contains all common methods between the different GUI windows
        3. Controls all access to external file reads i.e. JSON file for default parameters
        """
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        self.device_process = None
        self.device_present = False
        #self.controller_ip = 'pure2.local'
        self.controller_ip = '127.0.0.1'
        self.controller_interface_PID = None
        self.ctrl_proc = None
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'w') as f:
            f.close()
        with open('purification_parameters.json', 'r') as f:
            self._p = load(f)
        self.default_param = [self._p['NUM_COL']['default'], self._p['COL_VOLUME']['default'],
                            self._p['EQUILIBRATE_VOLUME']['default'], self._p['LOAD_VOLUME']['default'],
                            self._p['WASH_VOLUME']['default'], self._p['ELUTE_VOLUME']['default']]
        
        #Stylesheets used for displaying the status
        self.status_display_color_running = '#3CB371'
        self.status_display_color_halt = '#FFFF66'
        self.status_display_stylsheet = '{}'.format("QPushButton#status_display_btn{{"
                                        "border-radius:10;"
                                        "border-width: 2px;"
                                        "background-color: {0};"
                                        "font-size:14px;}}\n"
                                        "QPushButton:disabled#status_display_btn{{"
                                        "background-color:#A9A9A9}}")
        # Controlling pump time for ETA
        self.pump_vol_times = 60
        
        self.init_fraction_collector_params()

    ###################
    # TCP Connections #
    ###################

    def connect_to_device(self):
        """Try to bind to device ip and check if a connection is already there"""
        self.device_present = False
        #self.controller_ip = 'pure2.local'
        #self.device_present = True
        return self.device_present
        
    def connect_to_simulator(self):
        """Connect to the simulator by opening a pub/sub connection at local ip"""
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.daemon = True
        self.device_process.start()
        self.controller_ip = '127.0.0.1'

    def _connect_simulator(self):
        """Method run in the new process generated to connect to the simulator"""
        si = SimulatorInterface()
        si.autorun()
    
    def run_purification_script(self, is_basic_purification, parameters):
        """
        Run the purification protocal on a new process
        If the protocol is run on the simulator a signal is sent to the simulator
        to be the device and pass the 'device is available check' on the controller
        """
        targ = RunPurification if is_basic_purification else RunCustomProtol
        if not self.device_present:
            kill(self.device_process.pid, SIGUSR1)
        self.ctrl_proc = Process(target=targ, args=(parameters, self.getFractionParameters(), self.controller_ip, getpid(),))
        self.ctrl_proc.daemon = True
        self.ctrl_proc.start()
        self.controller_interface_PID = self.ctrl_proc.pid

    #####################
    ## Process Signals ##
    #####################

    def pause_clicked(self):
        """Sends SIGQUIT signal to raise pause flag if pause is clicked"""
        kill(self.controller_interface_PID, SIGQUIT)
    
    def hold_clicked(self):
        """Sends SIGUSR1 signal to raise hold flag if hold is clicked"""
        kill(self.controller_interface_PID, SIGUSR1)
    
    def resume_clicked(self):
        """Sends SIGCONT signal to resume from pause/hold if resume is clicked"""
        kill(self.controller_interface_PID, SIGCONT)
    
    def skip_clicked(self):
        """Sends SIGUSR2 signal to raise skip flag if skip is clicked"""
        kill(self.controller_interface_PID, SIGUSR2)

    def stop_clicked(self):
        """Sends SIGTERM signal to disconnect controller interface"""
        self._needs_connection = False
        kill(self.controller_interface_PID, SIGTERM)
        self.ctrl_proc.join()

    ######################################
    # Common methods between GUI windows #
    ######################################

    def areYouSureMsg(self, action):
        """Confirms whether or not the user meant to click an action button"""
        msg = QMessageBox()
        msg.setText('Are you sure you want to {}'.format(action))
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self._msgbtn)
        msg.exec()
    
    def _msgbtn(self, i):
        """Returns the result from the are you sure pop up"""
        self.is_sure = True if 'ok' in i.text().lower() else False

    def buffer_needed(self, protocol_buffers):
        """Adds the buffers needed for the protocol with purging and cleanup
        and creates a string display of the total buffer needed
        
        Parameters
        -----------------------------
        protocol_buffers = {'BASE': 20, 'ELUTION': 1, ...}
        """
        total_buffers = {}
        purging_buffers = {'BASE': 1, 'ELUTION': 1, 'WASH': 1, 'LOAD_BUFFER': 1}
        cleanup_buffers = {'BASE': 10, 'LOAD_BUFFER': 10}

        for key in purging_buffers:
            total = purging_buffers[key]
            if key in cleanup_buffers:
                total += cleanup_buffers[key]
            if key in protocol_buffers:
                total += protocol_buffers[key]
            total_buffers.update({key: total})
        return total_buffers

    ################################
    ## Fraction Collector Methods ##
    ################################

    def init_fraction_collector_params(self):
        self.frac_col_sel = [0]*10
        self.flow_col_sel = [0]*4
        self.fracflow_objs = {}

    def flowpathwayClicked(self, id, col_size):
        """id: unique identifier for the step selecting the flowpathway"""
        if id not in self.fracflow_objs:
            self.fracflow_objs.update({id: FractionsSelected(id, col_size)})

    def fractionCollectorSel(self, id, vol, col_size):
        """id: unique identifier for the step selecting fraction collector
        vol: the volume flowing through the fraction collector
        col_size: either 1 or 5 or 50"""
        pathway_array = self.flow_col_sel if col_size == 50 else self.frac_col_sel
        num_needed = ceil(vol/col_size)
        last_volume = vol - (col_size*(num_needed-1))
        pathway_array = self.fracflow_objs[id].add_path(pathway_array, col_size, num_needed, last_volume)
        return self.fracflow_objs[id].selectedList

    def okay_vol_checker(self, vol, col_size):
        """Checks if the volume exceeds the maximum"""
        vol_array = self.flow_col_sel if col_size == 50 else self.frac_col_sel
        max_vol = col_size*len(vol_array)
        if vol_array.count(0) >= ceil(vol/col_size):
            return -1
        return col_size*(vol_array.count(0))
    
    def vol_exceeds_msg(self, limit):
        """Throws error if the capacity of the pathway is reached"""
        msg = QMessageBox()
        msg.setText("Error! Exceeds Capacity!")
        msg.setInformativeText('Volume available in selected pathway is {}ml'.format(limit))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    
    def fractionCollectorUnsel(self, id):
        pathway_array = self.flow_col_sel if self.fracflow_objs[id].is_flow else self.frac_col_sel
        pathway_array = self.fracflow_objs[id].remove_path(pathway_array)

    def getFractionParameters(self):
        """Returns all the fraction parameters to run the protocol in the order of the id number"""
        param = []
        for i in range(len(self.fracflow_objs)):
            param.append(self.fracflow_objs[i].selectedList)
        return param

class FractionsSelected():
    def __init__(self, id, col_size):
        """id: Unique identifier of the step
        selectedList: [0,50,0,0] The list of fractions selected
        and the volume to fraction for the step
        is_frac: Stores if the last flowpath was the fraction or the flow through"""
        self.id = id
        self._created_emptySelList(col_size)
        self.is_frac = None
    
    def _created_emptySelList(self, col_size):
        """Create the empty selectedList. The length can change based on the dropdown selection"""
        array_len = 4 if col_size == 50 else 10
        self.selectedList = [0]*array_len
        self.is_flow = True if array_len == 4 else False

    def add_path(self, current_path, col_size, num_needed, last_volume):
        """current_path: [50,0,0,0] The fractions that are already occupied
        col_size: Either 1 or 5 or 50 (the max volume)
        num_needed: The number of fractions needed to be added
        last_volume: The volume in the last fraction (might be less than col_size)"""
        self._created_emptySelList(col_size)
        num_filled = 0
        for i in range(len(current_path)):
            if current_path[i] == 0:
                num_filled +=1
                if num_filled == num_needed:
                    current_path[i] = last_volume
                    self.selectedList[i] = last_volume
                else:
                    current_path[i] = col_size
                    self.selectedList[i] = col_size
            if num_filled == num_needed:
                break
        return current_path
    
    def remove_path(self, current_path):
        """Remove the non zero indexes of selectedList from current_path"""
        for i in range(len(current_path)):
            if self.selectedList[i] != 0:
                current_path[i] = 0
        self.selectedList = [0]*len(current_path)
        return current_path

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()