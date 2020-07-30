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
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        try:
            current_address = socket.gethostbyname(socket.getfqdn() + '.local')
            self.device_process = Process(target=self._connect_device, args=(current_address,))
            self.device_process.start()
            self.controller_ip = 'pure1'
            return True
        except OSError:
            return False
    
    def _connect_device(self, current_address):
        current_address = socket.gethostbyname(socket.getfqdn() + '.local')
        di = DeviceInterface(ip_address=current_address)
        di.autorun()
    
    def connect_to_simulator(self):
        self.connecting_to_sim = True
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.start()
        self.controller_ip = '127.0.0.1'

    def _connect_simulator(self):
        si = SimulatorInterface()
        si.autorun()
    
    def run_purification_script(self, parameters):
        if self.connecting_to_sim:
            kill(self.device_process.pid, SIGUSR1)
        self.ctrl_proc = Process(target=RunPurification, args=(parameters, self.controller_ip, getpid(),))
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

    def stop_clicked(self):
        """Sends SIGTERM signal to disconnect controller interface"""
        self._needs_connection = False
        kill(self.controller_interface_PID, SIGTERM)
        self.ctrl_proc.join()
    
    def close_device(self):
        """Sends SIGTERM signal to disconnect simulator interface
        TODO: what do we do when connected to device??"""
        if self.connecting_to_sim:
            kill(self.device_process.pid, SIGTERM)
            self.device_process.join()

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()