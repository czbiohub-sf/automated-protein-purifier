from time import sleep
from enum import Enum, auto
from signal import signal, SIGQUIT, SIGSTOP, SIGUSR1, SIGUSR2, SIGTERM, getsignal
from os import kill, getpid
from czpurifier.middleware import ControllerInterface
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class UICommands():
    """Command wrappers for purifier ControllerInterface."""

    def __init__(self, timeout: int = 20000):
        self.ci = ControllerInterface(timeout)
        self.pumps = 0
        self.alias = ''

        # Assign signals and handlers
        self._pause_flag = False
        self._pumps_are_paused = False
        self._hold_flag = False
        self._skip_flag = False
        self._SIGTERM_default = getsignal(SIGTERM)
        signal(SIGQUIT, self._raisePauseFlag)
        signal(SIGUSR1, self._raiseHoldFlag)
        signal(SIGUSR2, self._raiseSkipFlag)
        signal(SIGTERM, self._softStop)

    def __del__(self):
        if self.alias:
            self.disconnect()

    ##################
    #   CONNECTION   #
    ##################
    def connect(self, config_mode: str, address: str, pumps=4, correction=[], alias='purifier'):
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
                if len(correction) == self.pumps:
                    self.flowRateCorrection(correction)
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
        - Check for the pause flag before and after pumping is started
        If the pause flag is up, the script it suspended in the location,
        the pumps are closed, till resume signal is recieved
        - Check for the hold flag when pumps are running, if flag is up,
        the script suspends in position keeping the pumps running, till
        resume signal is recieved
        - Check for the skip flag, if flag is up, break out of the pump
        loop and finish pumping
        """
        if self._pause_flag:
            self._remainInPlace(True)
        for pump in range(self.pumps):
            self.ci.startPumping(pump)
        for c in range(col_vol * 60):
            if self._pause_flag:
                logging.info("Pausing pumps")
                self.ci.stopPumping()
                self._pumps_are_paused = True
                self._remainInPlace(True)
            if self._hold_flag:
                logging.info("Holding pumps")
                self._remainInPlace(False)
            if self._skip_flag:
                logging.info("Skipping to next step")
                self._skip_flag = False
                self.ci.stopPumping()
                return True
            if self._pumps_are_paused:
                logging.info("Restarting pumps")
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
    
    def _raiseHoldFlag(self, signalNumber, frame):
        """Raise hold flag if SIGUSR1 recieved"""
        self._hold_flag = True

    def _remainInPlace(self, is_pump):
        """Suspend script at location if pause/hold flag is up"""
        if is_pump:
            self._pause_flag = False
        else:
            self._hold_flag = False
        kill(getpid(), SIGSTOP)
    
    def _raiseSkipFlag(self, signalNumber, frame):
        self._skip_flag = True
        return

    def _softStop(self, signalNumber, frame):
        """Safely disconnects the interface when stop is called"""
        self.disconnect()
        signal(SIGTERM, self._SIGTERM_default)
        kill(getpid(), SIGTERM)
        
     
    def flowRateCorrection(self, corr_factor: list):
        """Apply correction factor to pump flow rates."""
        self.ci.getFlowRates()
        for pump in range(self.pumps):
            self.ci.setFlowRates(self.ci.flow_rates[pump] * corr_factor[pump], pump)
