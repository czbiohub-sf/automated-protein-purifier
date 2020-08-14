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

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def __init__(self):
        """Controls the communication between device and controller interface
        and the GUI"""
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        self.device_process = None
        self.connecting_to_sim = False
        self.controller_ip = None
        self.controller_interface_PID = None
        self.ctrl_proc = None
        chdir(path.dirname(path.realpath(__file__)))
        with open('purification_parameters.json', 'r') as f:
            self._p = load(f)
        self.default_param = [self._p['NUM_COL']['default'], self._p['COL_VOLUME']['default'],
                            self._p['EQUILIBRATE_VOLUME']['default'], self._p['LOAD_VOLUME']['default'],
                            self._p['WASH_VOLUME']['default'], self._p['ELUTE_VOLUME']['default']]

    def connect_to_device(self):
        """
        Try to connect to the device if it is available 
        Return True if connection is successful
        """
        try:
            current_address = socket.gethostbyname(socket.getfqdn() + '.local')
            self.device_process = Process(target=self._connect_device, args=(current_address,))
            self.device_process.start()
            self.controller_ip = 'pure2.local'
            return True
        except OSError:
            return False
    
    def _connect_device(self, current_address):
        """Method run in the new process generated to connect to the device"""
        current_address = socket.gethostbyname(socket.getfqdn() + '.local')
        di = DeviceInterface(ip_address=current_address)
        di.autorun()
    
    def connect_to_simulator(self):
        """Connect to the simulator by opening a pub/sub connection at local ip"""
        self.connecting_to_sim = True
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.start()
        self.controller_ip = '127.0.0.1'

    def _connect_simulator(self):
        """Method run in the new process generated to connect to the simulator"""
        si = SimulatorInterface()
        si.autorun()
    
    def run_purification_script(self, parameters, fractions):
        """
        Run the purification protocal on a new process
        If the protocol is run on the simulator a signal is sent to the simulator
        to be the device and pass the 'device is available check' on the controller
        """
        if self.connecting_to_sim:
            kill(self.device_process.pid, SIGUSR1)
        self.ctrl_proc = Process(target=RunPurification, args=(parameters, fractions, self.controller_ip, getpid(),))
        self.ctrl_proc.start()
        self.controller_interface_PID = self.ctrl_proc.pid

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
    
    def close_device(self):
        """Sends SIGTERM signal to disconnect simulator interface
        TODO: what do we do when connected to device??
        Signals do not work across different machines"""
        if self.connecting_to_sim:
            kill(self.device_process.pid, SIGTERM)
            self.device_process.join()

    def calc_step_times(self, parameters, fractions):
        """Calculates an estimate time for each step"""
        stage_moving_time = 10
        pump_vol_times = 60
        step_times = []
        i = 2
        for f in fractions:
            pump_total = parameters[i]*pump_vol_times
            if f is None:
                stage_total = 0
            else:
                stage_total = len(f)*stage_moving_time
            step_times.append(pump_total+stage_total)
            i +=2
        return step_times

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()