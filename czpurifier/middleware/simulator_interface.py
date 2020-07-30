#!/Users/samia.sama/Documents/Protein_Purifier/venv/bin/python
"""Interfaces between communication layer and psuedo hardware (used for testing)"""
import logging
from time import sleep
from czpurifier.middleware import DeviceInterface
from czpurifier.hardware import HardwareController 
from logging import NullHandler
from signal import signal, SIGUSR1
from os import kill, getpid

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class SimulatorInterface(DeviceInterface):
    """Device interface of protein purifier.
    """
    def __init__(self, ip_address='127.0.0.1', timeout_recv=1):
        super().__init__(ip_address, timeout_recv)
        signal(SIGUSR1, self._fake_socket_availability)
    
    def _fake_socket_availability(self, signalNumber, frame):
        """Fake device is up for the controller interface availability check"""
        for _ in range(5):
            sleep(1)
            self.socket_availability.send_pyobj('')

    def loadConfig(self, config_mode: str):
        """Update command list with settings defined in config file.

        Parameters
        ----------
        config_mode : str
            Configuration option listed in config file.
        """
        Hardware = HardwareController(self.hardware_config_file, config_mode, True)
        self.cmd_dict.update({'reportFracCollectorPositions': Hardware.reportFracCollectorPositions,
                              'moveFracCollector': Hardware.moveFracCollector,
                              'homeFracCollector': Hardware.homeFracCollector,
                              'setInputValves': Hardware.setInputValves,
                              'setWasteValves': Hardware.setWasteValves,
                              'getInputValves': Hardware.getInputValves,
                              'getWasteValves': Hardware.getWasteValves,
                              'reportRotaryPorts': Hardware.reportRotaryPorts,
                              'getCurrentPort': Hardware.getCurrentPort,
                              'renameRotaryPort': Hardware.renameRotaryPort,
                              'moveRotaryValve': Hardware.moveRotaryValve,
                              'homeRotaryValve': Hardware.homeRotaryValve,
                              'getPumpStatus': Hardware.getPumpStatus,
                              'getFlowRate': Hardware.getFlowRate,
                              'setFlowRate': Hardware.setFlowRate,
                              'startPumping': Hardware.startPumping,
                              'stopPumping': Hardware.stopPumping,
                              'getFractionDuration': Hardware.getFractionDuration,
                              })

if __name__ == "__main__":
    #current_address = socket.gethostbyname(socket.getfqdn() + '.local')
    logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
    si = SimulatorInterface()
    si.autorun()