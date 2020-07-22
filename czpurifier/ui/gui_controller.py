import logging
from logging import NullHandler
import socket
from multiprocessing import Process
from czpurifier.middleware import SimulatorInterface, DeviceInterface

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def connect_to_device(self):
        """
        Try to connect to the device if it is available 
        Return True if connection is successful
        """
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        try:
            current_address = socket.gethostbyname(socket.getfqdn() + '.local')
            device = Process(target=self._connect_device, args=(current_address,))
            device.start()
            return True
        except OSError:
            return False
    
    def _connect_device(self, current_address):
        current_address = socket.gethostbyname(socket.getfqdn() + '.local')
        di = DeviceInterface(ip_address=current_address)
        di.autorun()
    
    def connect_to_simulator(self):
        sim = Process(target=self._connect_simulator)
        sim.start()

    def _connect_simulator(self):
        si = SimulatorInterface()
        si.autorun()
    
    

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()