from time import sleep
from enum import Enum, auto
from czpurifier.middleware import ControllerInterface


class UICommands():
    """Command wrappers for purifier ControllerInterface."""

    def __init__(self, timeout: int):
        self.ci = ControllerInterface(timeout)
        self.alias = ''

    def openAllWaste(self):
        """Open pre- and postcolumn waste valves."""
        self.ci.setWasteStates(0)

    def openPreColumnWaste(self):
        """Open precolumn waste valves."""
        precol_valves = 15
        self.ci.getWasteStates()
        target_states = self.ci.waste_states | precol_valves
        self.ci.setWasteStates(target_states)

    def openPostColumnWaste(self):
        """Open postcolumn waste valves."""
        postcol_valves = 240
        self.ci.getWasteStates()
        target_states = self.ci.waste_states | postcol_valves
        self.ci.setWasteStates(target_states)

    def closeAllWaste(self):
        """Close all waste valves."""
        self.ci.setWasteStates(255)

    def closePreColumnWaste(self):
        """Close precolumn waste valves."""
        precol_valves = 15
        self.ci.getWasteStates()
        target_states = self.ci.waste_states & ~precol_valves
        self.ci.setWasteStates(target_states)

    def closePostColumnWaste(self):
        """Close postcolumn waste valves."""
        postcol_valves = 240
        self.ci.getWasteStates()
        target_states = self.ci.waste_states & ~postcol_valves
        self.ci.setWasteStates(target_states)

    def selectLoad(self):
        """Open load valves."""
        self.ci.setInputStates(15)

    def selectBuffers(self):
        """Close load valves."""
        self.ci.setInputStates(0)

    def connect(self, config_mode: str, address: str, alias='Purifier1'):
        """Connect to machine at specified address and load config mode.

        Parameters
        ----------
        config_mode : str
            Configuration mode selected from hardware config file.
        address : str
            IP address of target machine.
        alias : str
            Alias to give machine for communication purposes.
        """
        self.ci.connect(address, alias)
        if self.ci.devices:
            self.alias = alias
            try:
                self.ci.config_mode = config_mode
                self.ci.loadConfig()
                self.resetMachine()
                self.getMachineStatus()
            except:
                self.disconnect()

    def disconnect(self):
        """Stop machine and disconnect."""
        self.resetMachine()
        self.ci.disconnect(self.alias)
        self.alias = ''

    def resetMachine(self):
        """Set machine to a known state."""
        self.ci.getMachineStatus()
        self.ci.stopPumping()
        self.openAllWaste()
        self.selectBuffers()
        self.ci.homeFrac()
        self.ci.moveFracTo('Safe')
        self.ci.homePorts()

    def getMachineStatus(self):
        """Retreive machine states."""
        self.ci.getPorts()
        self.ci.getCurrentPort()
        self.ci.getPositions()
        self.ci.getFlowRates()
        self.ci.getPumpStatus()
        self.ci.getInputStates()
        self.ci.getWasteStates()

    def selectFraction(self, frac_name: str):
        """Move fraction collector to specified position."""
        self.ci.moveFracTo(frac_name)

    def selectPort(self, port_name: str):
        """Move rotary valve to specified position."""
        self.ci.selectPort(port_name)

    def pump(self, col_vol: int):
        """Run pumps for the specified column volumes."""
        self.ci.startPumping()
        sleep(col_vol * 60)
        self.ci.stopPumping()
