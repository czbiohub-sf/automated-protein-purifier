import zmq
import logging
from logging import NullHandler
import socket
from multiprocessing import Process
from czpurifier.middleware import SimulatorInterface, DeviceInterface
from os import chdir, path
from json import load
from run_purification import RunPurification

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def __init__(self):
        self.device_process = None
        self.controller_ip = None
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
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.start()
        self.controller_ip = '127.0.0.1'

    def _connect_simulator(self):
        si = SimulatorInterface()
        si.autorun()

    def close_connection(self):
        if self.device_process is not None:
            # Close the process after the connection is terminated
            # Temporary -> send cmd from controller interface to disconnect
            # Throws zmq error now as the connection is not closed properly
            self.device_process.join()
    
    def run_purification_script(self, parameters):
        ctrl_proc = Process(target=RunPurification, args=(parameters, self.controller_ip,))
        ctrl_proc.start()

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()