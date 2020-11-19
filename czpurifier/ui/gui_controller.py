import zmq
import logging
from logging import NullHandler
from multiprocessing import Process
from czpurifier.middleware import SimulatorInterface, DeviceInterface
from os import chdir, path, kill, getpid
from signal import signal, SIGQUIT, SIGCONT, SIGUSR1, SIGTERM, SIGUSR2
from json import load
from run_purification import RunPurification
from run_custom_protocol import RunCustomProtocol
from run_calib_protocol import RunCalibrationProtocol
from fraction_col_gui import Ui_FractionColumn
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QMainWindow, QComboBox
from math import ceil

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def __init__(self):
        """
        1. Controls the communication between the controller interface and the GUI
        2. Contains all common methods between the different GUI windows
        3. Controls all access to external file reads i.e. JSON file for default parameters
        4. Initializes the fraction collector and tracks its use in the GUI
            - Flow Throw Columns: 4 larger columns on the fraction collector
            - Fraction Columns: 10 smaller columns on the fraction collector
        """
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        # The process is None if connected to the device or it holds the process object for the simulator
        self.device_process = None
        # The object that runs the controller and its PID
        self.ctrl_proc = None
        self.controller_interface_PID = None

        # Writes to the purifier.log to create an empty log
        # The log file is read and displayed on the gui
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'w') as f:
            f.close()
        # Open the json file that contains all the defualt parameters
        with open('purification_parameters.json', 'r') as f:
            self._p = load(f)
        # Default parameters for the basic purification window
        self.default_param = [self._p['NUM_COL']['default'],
                            self._p['EQUILIBRATE_VOLUME']['default'], self._p['LOAD_VOLUME']['default'],
                            self._p['WASH_VOLUME']['default'], self._p['ELUTE_VOLUME']['default']]
        # Default flow rate correction factors for each 
        self.default_buffer_fc = [self._p['BASE']['default'], self._p['LOAD_BUFFER']['default'],
                                self._p['WASH']['default'], self._p['ELUTION']['default']]
        # The controller_ip is saved in the json file as pure1/pure2 based on the hardware
        # The controller_ip is overwritten to a local address if the simulation mode is selected
        self.controller_ip = self._p['PURIFIER_IP']['ip']
        #self.controller_ip = '127.0.0.1'
        # Default actual per column volumes for 1mL col size
        self.actualvol1mL = [self._p['PUMP1']['1mL'], self._p['PUMP2']['1mL'], self._p['PUMP3']['1mL'], self._p['PUMP4']['1mL']]
        self.actualvol5mL = [self._p['PUMP1']['5mL'], self._p['PUMP2']['5mL'], self._p['PUMP3']['5mL'], self._p['PUMP4']['5mL']]

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
        
        # Initializing empty fraction collectors
        self.init_fraction_collector_params()
        self.columnsize = None
        self.flow_rate_correction = None
        self.is_sure = None

    ###################
    # TCP Connections #
    ###################

    def hardware_or_sim(self, dev_process):
        """Called when a protocol window is opened to configure the connection variables"""
        self.controller_ip = self.controller_ip if dev_process is None else '127.0.0.1'
        self.device_process = dev_process
        
    def connect_to_simulator(self):
        """Connect to the simulator by opening a pub/sub connection at local ip"""
        self.controller_ip = '127.0.0.1'
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.daemon = True
        self.device_process.start()

    def _connect_simulator(self):
        """Method run in the new process generated to connect to the simulator"""
        si = SimulatorInterface()
        si.autorun()
    
    def run_purification_script(self, is_basic_purification, parameters, calib_list):
        """
        Run the purification protocal on a new process
        If the protocol is run on the simulator a signal is sent to the simulator
        to be the device and pass the 'device is available check' on the controller
        """
        targ = RunPurification if is_basic_purification else RunCustomProtocol
        if self.device_process is not None:
            kill(self.device_process.pid, SIGUSR1)
        self.ctrl_proc = Process(target=targ, args=(parameters, calib_list, self.getFractionParameters(), 
                                    self.flow_rate_correction, self.controller_ip, getpid(),))
        self.ctrl_proc.daemon = True
        self.ctrl_proc.start()
        self.controller_interface_PID = self.ctrl_proc.pid
    
    def run_calibration_protocol(self, columnsize, calib_list, num_cols):
        """Runs the calibration protocol"""
        self.ctrl_proc = Process(target=RunCalibrationProtocol, args = (columnsize, calib_list, num_cols, self.controller_ip, getpid(),))
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
        purging_buffers = {'BASE': 1, 'ELUTION': 1, 'WASH': 1, 'LOAD_BUFFER': 1, 'LOAD': 1}
        cleanup_buffers = {'BASE': 10, 'LOAD_BUFFER': 10}

        for key in purging_buffers:
            total = purging_buffers[key]
            if key in cleanup_buffers:
                total += cleanup_buffers[key]
            if key in protocol_buffers:
                total += protocol_buffers[key]
            total_buffers.update({key: total*self.columnsize})
        return total_buffers

    def setFlowCorrection(self, fc_percent):
        """Converts the percent flow correction to flow correction ratio to pass to 
        the scripts
        flow correction ratio = actual flow rate / expected flow rate
        """
        for key in fc_percent:
            fc_percent[key] = round((self.columnsize + (fc_percent[key])/100)/self.columnsize, 2)
        self.flow_rate_correction = fc_percent
    
    def getPumpTimes(self, protocol_times):
        """Add the purging time and the cleanup time to the pump times"""
        purging_time = 5
        cleanup_time = 20
        protocol_times.insert(0,purging_time*60)
        protocol_times.append(cleanup_time*60)
        return protocol_times

    def checkEmptyQLines(self, qline_wdjs: list):
        """Loops through all the line widgets and throws error if any field is empty"""
        for q in qline_wdjs:
            if q.text() is '':
                self._emptyQLineMsg()
                return False
        return True

    def _emptyQLineMsg(self):
        """Displays error if one of the boxes are empty"""
        msg = QMessageBox()
        msg.setText('Error! Fields cannot be empty!')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()                 

    ################################
    ## Fraction Collector Methods ##
    ################################

    def setFlowPath(self, flow_id, pathway, volume, frac_wdw = True):
        """Configures the flow pathway for the selected step
        flow_id: The unique id used to characterize the step
        pathway: Either one of the wastes or one of the collectors
        volume: The volume going through the pathway in CV
        frac_wdw: Used to determine whether or not to display the fraction collector window
        Return
        -------------
        whether the fraction collector was updated or not, the widgets are enabled/disabled 
        based on answer
        """
        enable_widgets = True
        pathway_rejected = False
        # set the column limit in mL:
        #  1mL/5mL for fraction collector with 1mL/5mL columns, 50mL for FLOW regardless of column size 
        col_limit = self.columnsize if pathway == 'FRACCOL' else 50
        self.flowpathwayClicked(flow_id, col_limit)
        self.fractionCollectorUnsel(flow_id)
        if pathway == 'FRACCOL' or pathway == 'FLOWCOL':
            max_vol = self.okay_vol_checker(volume*self.columnsize, col_limit)
            if max_vol == -1:
                # volume is okay
                selected_columns = self.fractionCollectorSel(flow_id, volume*self.columnsize, col_limit)
                if frac_wdw:
                    self._dispFracFlow(selected_columns)
                enable_widgets = False
            else:
                self.vol_exceeds_msg(max_vol)
                pathway_rejected = True
        return enable_widgets, pathway_rejected
    
    def _dispFracFlow(self, selected_columns):
        """Display the fraction collector window"""
        self.frac_wdw = QMainWindow()
        self.frac_ui = Ui_FractionColumn(self.frac_wdw)
        self.frac_wdw.show()
        self.frac_ui.correct_frac_col_design()
        self.frac_ui.display_selected(selected_columns)

    def init_fraction_collector_params(self):
        self.frac_col_sel = [0]*10
        self.flow_col_sel = [0]*4
        self.fracflow_objs = {}

    def flowpathwayClicked(self, id, col_limit):
        """id: unique identifier for the step selecting the flowpathway"""
        if id not in self.fracflow_objs:
            self.fracflow_objs.update({id: FractionsSelected(id, col_limit)})

    def fractionCollectorSel(self, id, vol, col_limit):
        """id: unique identifier for the step selecting fraction collector
        vol: the volume flowing through the fraction collector in mL
        col_limit: The max volume each column can handle"""
        pathway_array = self.flow_col_sel if col_limit == 50 else self.frac_col_sel
        num_needed = ceil(vol/col_limit)
        # The volume for the last collector may be less than the col_limit
        # The last volume is recorded in CV
        last_volume = (vol - (col_limit*(num_needed-1)))/self.columnsize
        # the col limit is fixed 50mL for the flow through 
        # for fraction collector the column limit is dep on the column size
        if col_limit == 50:
            col_limit_cv = 50 if self.columnsize == 1 else 10
        else:
            col_limit_cv = 1
        pathway_array = self.fracflow_objs[id].add_path(pathway_array, col_limit_cv, num_needed, last_volume)
        return self.fracflow_objs[id].selectedList

    def okay_vol_checker(self, vol, col_limit):
        """Checks if the volume exceeds the maximum
        vol: The volume in mL to check
        col_limit: The max volume each column can handle
        Return
        ---------------------
        -1 : There is available space left in the collector
        > 0 : Max volume that is left in the collector (in mL)
        """
        vol_array = self.flow_col_sel if col_limit == 50 else self.frac_col_sel
        if vol_array.count(0) >= ceil(vol/col_limit):
            return -1
        return col_limit*(vol_array.count(0))
    
    def vol_exceeds_msg(self, limit):
        """Throws error if the capacity of the pathway is reached"""
        msg = QMessageBox()
        msg.setText("Error! Exceeds Capacity!")
        msg.setInformativeText('Volume available in selected pathway is {} mL'.format(limit))
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
    def __init__(self, id, col_limit):
        """id: Unique identifier of the step
        selectedList: [0,50,0,0] The list of fractions selected
        and the volume to fraction for the step
        col_limit: The limit for each of the pathway (in mL)
        is_frac: Stores if the last flowpath was the fraction or the flow through"""
        self.id = id
        self._created_emptySelList(col_limit)
        self.is_frac = None
    
    def _created_emptySelList(self, col_limit):
        """Create the empty selectedList. The length can change based on the dropdown selection
        Accepts column limit in either mL or CV"""
        # if col_limit > 5 it means the flow path is the flow through column
        array_len = 4 if col_limit > 5 else 10
        self.selectedList = [0]*array_len
        self.is_flow = True if array_len == 4 else False

    def add_path(self, current_path, col_limit_cv, num_needed, last_volume):
        """current_path: [50,0,0,0] The fractions that are already occupied
        col_limit_cv: Either 1, 50 or 10 depending on the pathway and column size
        num_needed: The number of fractions needed to be added
        last_volume: The volume in the last fraction (might be less than the column limit) in CV

        Updates 2 lists:
        1. The current path to display in the fraction collector window
        2. The complete path including other selections of the fraction collector, to keep track of the 
        overall volume left

        Return
        --------------------------
        The fractions for the current path -> used to display in the fraction collector window
        """
        self._created_emptySelList(col_limit_cv)
        num_filled = 0
        for i in range(len(current_path)):
            if current_path[i] == 0:
                num_filled +=1
                if num_filled == num_needed:
                    current_path[i] = last_volume
                    self.selectedList[i] = last_volume
                else:
                    current_path[i] = col_limit_cv
                    self.selectedList[i] = col_limit_cv
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