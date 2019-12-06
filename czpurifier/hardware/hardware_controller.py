"""Methods for controlling purifier hardware."""

from .hardware_setup import PurifierHardwareSetup
import logging
from logging import NullHandler
from time import sleep

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class HardwareController():
    """Hardware master control class.

    Parameters
    ----------
    hw_config_file_path : str
        String indicating system path to hardware config file
    config_mode : str
        Config section to load in addition to 'DEFAULT'

    """

    def __init__(self, hw_config_file_path, config_mode):

        setup = PurifierHardwareSetup()
        self.subunits = {}
        self.collector_homed = False
        self.rotary_homed = False
        error = False

        try:
            setup.configValidation(hw_config_file_path)
        except KeyError as e:
            log.warning('Configuration file `%s` is missing a required field.', hw_config_file_path)
            log.warning(str(e))
            error = True
        except ValueError:
            log.warning('`%s` is not a valid file.', hw_config_file_path)
            error = True

        try:
            subunits = setup.initializeConfig(config_mode)
        except ValueError as e:
            log.warning(str(e))
            error = True

        if error:
            log.warning('Hardware subunit initialization unsuccessful.')
        else:
            self.subunits = subunits

    def reportFields(self):
        """Return names of subunits and constants system is configured with."""
        return self.subunits.keys()

    ###############################
    # FRACTION COLLECTOR COMMANDS #
    ###############################

    def reportFracCollectorPositions(self):
        """Return positions indexed on the fraction collector."""
        return self.subunits['FRAC_COLLECTOR'].getIndexedPositions()

    def moveFracCollector(self, position: str):
        """Move the fraction collector to an indexed position.

        Parameters
        ----------
        position : str
            Name of indexed position to travel to.
        """
        if self.collector_homed:
            if position in self.reportCollectorPositions():
                self.subunits['FRAC_COLLECTOR'].moveToIndexedPosition(position)
                log.info('Fraction collector moved to indexed position `%s`', position)
            else:
                log.warning('Index position `%s` not valid.', position)
        else:
            log.warning('Home fraction collector before moving to indexed position.')

    def homeFracCollector(self):
        """Home the fraction collector."""
        self.subunits['FRAC_COLLECTOR']._ticStepper.home(self.subunits['FRAC_HOME_DIR'])
        while not self.subunits['FRAC_COLLECTOR']._ticStepper.isHomed():
            sleep(0.01)  # Calling isHomed too frequently can crash the I2C bus
        self.collector_homed = True
        log.info('Fraction collector homed.')

    ###########################
    # SOLENOID VALVE COMMANDS #
    ###########################

    def setInputValves(self, states: int):
        """Set multiple input valve states at once with an integer.

        Parameters
        ----------
        states : int
            A decimal representation of the binary valve states.
        """
        self.subunits['VALVES_IN'].valve_states = states
        log.info('Input valves set to %s.', str(states))

    def setWasteValves(self, states: int):
        """Set multiple waste valves states at once with an integer.

        Parameters
        ----------
        states : int
            A decimal representation of the binary valve states.
        """
        self.subunits['VALVES_IN'].valve_states = states
        log.info('Waste valves set to %s.', str(states))

    def getInputValves(self):
        """Return input valve states."""
        return self.subunits['VALVES_IN'].valve_states

    def getWasteValves(self):
        """Return waste valve states."""
        return self.subunits['VALVES_WASTE'].valve_states

    #########################
    # ROTARY VALVE COMMANDS #
    #########################

    def reportRotaryPorts(self):
        """Return aliases of rotary ports."""
        return self.subunits['PORTS']

    def getCurrentPort(self):
        """Return alias of currently selected port."""
        port = self.subunits['ROTARY'].current_port
        if port == -1:
            port_name = 'Unknown'
        else:
            port_name = self.subunits['PORTS'][port]
        return port_name

    def renameRotaryPort(self, port_num: int, name: str):
        """Change the alias of a port.

        Parameters
        ----------
        port_num : int
            Port number on rotary valve to be renamed (First port is `0`)
        name : str
            Alias to give the selected port
        """
        self.subunits['PORTS'][port_num] = name
        log.info('Rotary port %s aliased as %s.', str(port_num), name)

    def moveRotaryValve(self, id):
        """Move to a rotary port as specified by port number or alias.

        Parameters
        ----------
        id : str or int
            Alias or port number to travel to
        """
        if self.rotary_homed:
            if type(id) == int & id >= 0 & id <= self.subunits['NUM_PORTS']:
                port_num = id
            elif type(id) == str & id in self.subunits['PORTS']:
                port_num = self.subunits['PORTS'].index(id)
            else:
                log.warning('Port ID `%s` not valid. Use port number or name.')
                return
            self.subunits['ROTARY'].moveToPort(port_num)
            log.info('Moved to rotary port `%s`.', id)
        else:
            log.warning('Home rotary valve before use.')

    def homeRotaryValve(self):
        """Home the rotary valve."""
        self.subunits['ROTARY'].home()
        self.rotary_homed = True
        log.info('Rotary valve homed.')

    #################
    # PUMP COMMANDS #
    #################
    def getPumpStatus(self, pump=-1):
        """Return the operational status of the pump (running/not running).

        Parameters
        ----------
        pump : int
            Pump number beginning with `0` for the first pump. -1 is all pumps.
        """
        running = []
        cols = self.subunits['NUM_COLS']
        if pump >= cols:
            log.warning('Pump index out of range. Choose pump between 0 and %s.', str(cols - 1))
        else:
            if pump < 0:
                for i in range(0, cols):
                    running.append(self.subunits['PUMPS'][i].running)
            else:
                running.append(self.subunits['PUMPS'][pump].running)
        return running

    def getFlowRate(self, pump=-1):
        """Return the flow rate of a single pump or all pumps.

        Parameters
        ----------
        pump : int
            Pump number beginning with `0` for the first pump. -1 is all pumps.
        """
        rate = []
        cols = self.subunits['NUM_COLS']
        if pump >= cols:
            log.warning('Pump index out of range. Choose pump between 0 and %s.', str(cols - 1))
        else:
            if pump < 0:
                for i in range(0, cols):
                    rate.append(self.subunits['PUMPS'][i].flow_rate)
            else:
                rate.append(self.subunits['PUMPS'][pump].flow_rate)
        return rate

    def setFlowRate(self, flow_rate, pump=-1):
        """Change the flow rate of a single pump or all pumps.

        Parameters
        ----------
        flow_rate : float
            Flow rate to set the targeted pump to
        pump : int
            Pump number beginning with `0` for the first pump. -1 is all pumps.
        """
        cols = self.subunits['NUM_COLS']
        if pump >= cols:
            log.warning('Pump index out of range. Choose pump between 0 and %s.', str(cols - 1))
        else:
            if pump < 0:
                for i in range(0, cols):
                    self.subunits['PUMPS'][i].flow_rate = flow_rate
            else:
                self.subunits['PUMPS'][pump].flow_rate = flow_rate

    def startPumping(self, pump=-1):
        """Start a single pump or all pumps.

        Parameters
        ----------
        pump : int
            Pump number beginning with `0` for the first pump. -1 is all pumps.
        """
        cols = self.subunits['NUM_COLS']
        if pump >= cols:
            log.warning('Pump index out of range. Choose pump between 0 and %s.', str(cols - 1))
        else:
            if pump < 0:
                for i in range(0, cols):
                    self.subunits['PUMPS'][i].start()
            else:
                self.subunits['PUMPS'][pump].start()

    def stopPumping(self, pump=-1):
        """Stop a single pump or all pumps.

        Parameters
        ----------
        pump : int
            Pump number beginning with `0` for the first pump. -1 is all pumps.
        """
        cols = self.subunits['NUM_COLS']
        if pump >= cols:
            log.warning('Pump index out of range. Choose pump between 0 and %s.', str(cols - 1))
        else:
            if pump < 0:
                for i in range(0, cols):
                    self.subunits['PUMPS'][i].stop()
            else:
                self.subunits['PUMPS'][pump].stop()

    def getFractionDuration(self):
        """Time to fill fractions at the current flow rates."""
        times = []
        for i in range(0, self.subunits['NUM_COLS']):
            times.append(self.subunits['VOL_FRAC'] / self.getFlowRate(i) * self.subunits['PUMP'][i]._UNIT_TIME)
        return times
