from time import sleep
from enum import Enum, auto
from signal import signal, SIGQUIT, SIGSTOP
from os import kill, getpid
from czpurifier.middleware import ControllerInterface


class UICommands():
    """Command wrappers for purifier ControllerInterface."""

    def __init__(self, timeout: int = 20000):
        self.ci = ControllerInterface(timeout)
        self.pumps = 0
        self.alias = ''

        # Assign signals and handlers
        self._pause_flag = False
        self._pumps_are_paused = False
        signal(SIGQUIT, self._raisePauseFlag)

    def __del__(self):
        if self.alias:
            self.disconnect()

    ##################
    #   CONNECTION   #
    ##################
    def connect(self, config_mode: str, address: str, pumps=4, alias='purifier'):
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
                self.pumps = pumps
            except:
                self.disconnect()

    def disconnect(self):
        """Stop machine and disconnect."""
        self.setStandby()
        self.ci.disconnect(self.alias)
        self.alias = ''
        self.pumps = 0

    def getMachineStatus(self):
        """Retreive machine states."""
        self.ci.getPorts()
        self.ci.getCurrentPort()
        self.ci.getPositions()
        self.ci.getFlowRates()
        self.ci.getPumpStatus()
        self.ci.getInputStates()
        self.ci.getWasteStates()

    def resetConnection(self, address: str):
        """Device network connection if unable to connect."""
        self.ci.hardConnect(address)
        self.ci.disconnect()

    def resetMachine(self):
        """Set machine to a known state."""
        self.setStandby()
        self.ci.homeFrac()
        self.ci.moveFracTo('Safe')
        self.ci.homePorts()

    def setStandby(self):
        """Set machine to a standby state."""
        self.getMachineStatus()
        self.ci.stopPumping()
        self.openAllWaste()
        self.selectBuffers()

    ####################
    #   WASTE VALVES   #
    ####################
    def openAllWaste(self):
        """Open pre- and postcolumn waste valves."""
        self.ci.setWasteStates(0)

    def openPreColumnWaste(self):
        """Open precolumn waste valves."""
        precol_valves = 15
        self.ci.getWasteStates()
        target_states = self.ci.waste_states & ~precol_valves
        self.ci.setWasteStates(target_states)

    def openPostColumnWaste(self):
        """Open postcolumn waste valves."""
        postcol_valves = 240
        self.ci.getWasteStates()
        target_states = self.ci.waste_states & ~postcol_valves
        self.ci.setWasteStates(target_states)

    def closeAllWaste(self):
        """Close all waste valves."""
        self.ci.setWasteStates(255)

    def closePreColumnWaste(self):
        """Close precolumn waste valves."""
        precol_valves = 15
        self.ci.getWasteStates()
        target_states = self.ci.waste_states | precol_valves
        self.ci.setWasteStates(target_states)

    def closePostColumnWaste(self):
        """Close postcolumn waste valves."""
        postcol_valves = 240
        self.ci.getWasteStates()
        target_states = self.ci.waste_states | postcol_valves
        self.ci.setWasteStates(target_states)

    ####################
    #   INPUT VALVES   #
    ####################
    def selectBuffers(self):
        """Close load valves."""
        self.ci.setInputStates(0)

    def selectLoad(self):
        """Open load valves."""
        self.ci.setInputStates(15)

    def selectPort(self, port_name: str):
        """Move rotary valve to specified position."""
        self.ci.selectPort(port_name)

    ##########################
    #   FRACTION COLLECTOR   #
    ##########################
    def selectFraction(self, frac_name: str):
        """Move fraction collector to specified position."""
        self.ci.moveFracTo(frac_name)

    #############
    #   PUMPS   #
    #############
    def pump(self, col_vol: float):
        """
        Run pumps for the specified column volumes.
        Check for the pause flag before and after pumping is started
        If the pause flag is up, the script it suspended in the location,
        the pumps are closed, till resume signal is recieved
        """
        if self._pause_flag:
            self._pausePump()
        for pump in range(self.pumps):
            self.ci.startPumping(pump)
        for _ in range(col_vol * 60):
            if self._pause_flag:
                self.ci.stopPumping()
                self._pumps_are_paused = True
                self._pausePump()
            if self._pumps_are_paused:
                self._pumps_are_paused = False
                for pump in range(self.pumps):
                    self.ci.startPumping(pump)
            sleep(1)
        self.ci.stopPumping()

    ####################
    # SIGNAL HANDLERS #
    ###################
    def _raisePauseFlag(self, signalNumber, frame):
        """Raise pause flag if SIGQUIT recieved"""
        self._pause_flag = True
        return
    
    def _pausePump(self):
        """Suspend script at location if pause flag is up"""
        self._pause_flag = False
        kill(getpid(), SIGSTOP)
        
     