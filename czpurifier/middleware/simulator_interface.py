#!/Users/samia.sama/Documents/Protein_Purifier/venv/bin/python
"""Interfaces between communication layer and psuedo hardware (used for testing)"""
import logging
from time import sleep
from czpurifier.hardware import HardwareControllerSimulator
from czpurifier.middleware import DeviceInterface
from czpurifier.hardware import HardwareController 
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class SimulatorInterface(DeviceInterface):
    """Device interface of protein purifier.
    """
    def autorun(self):
        """Loop > Wait for data and execute. Signal if device is available."""
        # Send signal for 5s that the fake device is up
        # Controller Interface checks to make sure that the device is running
        for _ in range(5):
            sleep(1)
            self.socket_availability.send_pyobj('Transmitting')
        super().autorun()
    
    def loadConfig(self, config_mode: str):
        """Update command list with settings defined in config file.

        Parameters
        ----------
        config_mode : str
            Configuration option listed in config file.
        """
        Hardware = HardwareSimulator(self.hardware_config_file, config_mode)
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

class HardwareSimulator(HardwareController):
    def reportFracCollectorPositions(self):
        pass
    def moveFracCollector(self):
        pass
    def homeFracCollector(self):
        pass
    def setInputValves(self):
        pass
    def setWasteValves(self):
        pass
    def getInputValves(self):
        pass
    def getWasteValves(self):
        pass
    #def reportRotaryPorts(self):
    #    pass
    def getCurrentPort(self):
        pass
    def renameRotaryPort(self):
        pass
    def moveRotaryValve(self):
        pass
    def homeRotaryValve(self):
        pass
    def getPumpStatus(self):
        pass
    def getFlowRate(self):
        pass
    def setFlowRate(self):
        pass
    def startPumping(self):
        pass
    def stopPumping(self):
        pass
    def getFractionDuration(self):
        pass

if __name__ == "__main__":
    #current_address = socket.gethostbyname(socket.getfqdn() + '.local')
    logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
    si = SimulatorInterface()
    si.autorun()