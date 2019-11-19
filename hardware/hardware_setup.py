"""Hardware peripheral initialization."""

from enum import Enum, auto
import logging
from logging import NullHandler
from pump_controller import PumpControllerTic
from rotary_controller import RotaryControllerTic
from valve_controller import ValveControllerI2c
from pyconfighandler import validateConfig
from pymotors import TicStepper, TicStage

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class DefaultConfigFields(Enum):
    NUM_COLUMNS = auto()
    SELECT_STEPS_REV = auto()
    SELECT_MICROS = auto()
    SELECT_HOME = auto()
    SELECT_POTS = auto()
    PUMP_STEPS_REV = auto()
    PUMP_MICROS = auto()
    SELECT_ADDR_START = auto()
    VALVES_ADDR_IN = auto()
    VALVES_ADDR_WASTE = auto()
    PUMP_ADDR = auto()
    PUMP_MOTOR_CURR = auto()
    SELECT_MOTOR_CURR = auto()


class PurifierHardwareSetup():
    """Setup hardware controllers as described by a config file."""

    def __init__(self):
        self._config = None
        self.config_options = None
        self.config_valid = False

        self.rot_valve = []
        self.pumps = []
        self.sol_valves = []
        self.frac_collector = []

        self.rot_v_standby = False
        self.pumps_standby = False
        self.sol_v_standby = False
        self.frac_c_standby = False
        log.debug('Hardware configuration object initialized.')

    def configValidation(self, path_to_config, required_config_fields):
        """Validate configuration file before use.

        Parameters
        ----------
        path_to_config : str
            System path to configuration file.
        required_config_fields : Enum
            Matches required fields to config file.
        """
        self._config, self.config_options = validateConfig(path_to_config, required_config_fields)
        self.config_valid = True

    def initializeConfig(self, config_mode: str):
        """Use configuration options to initialize peripherals.

        Parameters
        ----------
        config_mode : str
            Collects values for config options in the `DEFAULT` and
            `config_mode` sections of the configuration file.

        Returns
        -------
        subunits : dict
            A dictionary containing control objects for peripherals and
            relevant constants.
        """
        log.info('Initializing config file with option `%s`.', config_mode)
        if self.config_valid is False:
            log.warning('Validate configuration file before initializing.')
            return

        if config_mode not in self.config_options:
            raise ValueError('Config option `%s` not found.' % config_mode)

        if self.rot_v_standby is False:
            log.debug('Initializing rotary valve.')
            self.rot_valve = self._initializeRotaryValve(self._config, config_mode)
            self.rot_v_standby = True

        if self.pumps_standby is False:
            log.debug('Initializing pumps.')
            self.pumps = self._initializePumps(self._config, config_mode)
            self.pumps_standby = True

        if self.sol_v_standby is False:
            log.debug('Initializing solenoid valves.')
            self.sol_valves = self._initializeValves(self._config, config_mode)
            self.sol_v_standby = True

        if self.frac_c_standby is False:
            log.debug('Initializing fraction collector.')
            self.frac_collector = self._initializeFracCol(self._config, config_mode)
            self.frac_c_standby = True

        subunits = {**self.rot_valve,
                    **self.pumps,
                    **self.sol_valves,
                    **self.frac_collector,
                    }
        return subunits

    def reset(self):
        """Wipe configuration settings and peripherals."""
        log.debug('Resetting hardware configuration object.')
        self.__init__()

    @staticmethod
    def _initializeRotaryValve(config, config_mode):
        steps_rev = int(config[config_mode]['SELECT_STEPS_REV'])
        micros = int(config[config_mode]['SELECT_MICROS'])
        motor_current = int(config[config_mode]['SELECT_MOTOR_CURR'])
        home_dir = config[config_mode].getboolean('SELECT_HOME')
        encoder_pin = config[config_mode]['SELECT_ENCODE_PIN']
        num_ports = int(config[config_mode]['SELECT_PORTS'])
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['SELECT_ADDR'])

        port_names = ['NONE'] * num_ports

        for i in range(0, num_ports):
            try:
                port_names[i] = config[config_mode]['SELECT_%s' % str(i+1)]
            except Exception:
                pass

        motor = TicStepper(com_type='I2C', port_params=bus, address=addr, input_steps_per_rev=steps_rev)
        motor.microsteps = 1 / micros
        motor.setCurrentLimit(motor_current)

        rotary = RotaryControllerTic(MotorObj=motor, home_fwd=home_dir, analog_pin=encoder_pin)
        rotary_valves = {'ROTARY': rotary, 'PORTS': port_names, }
        return rotary_valves

    @staticmethod
    def _initializePumps(config, config_mode):
        num_columns = int(config[config_mode]['NUM_COLUMNS'])
        steps_rev = int(config[config_mode]['PUMP_STEPS_REV'])
        micros = int(config[config_mode]['PUMP_MICROS'])
        motor_current = int(config[config_mode]['PUMP_MOTOR_CURR'])
        vol_rev = float(config[config_mode]['PUMP_VOL_REV'])
        time_unit = config[config_mode]['PUMP_TIME_UNIT']
        flowrate = config[config_mode]['FLOWRATE']
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['PUMP_ADDR_START'])

        pumps = []

        for i in range(0, num_columns):
            motor = TicStepper(com_type='I2C', port_params=bus, address=addr+i, input_steps_per_rev=steps_rev)
            motor.microsteps = 1 / micros
            motor.setCurrentLimit(motor_current)
            pumps.append(PumpControllerTic(MotorObj=motor, vol_per_rev=vol_rev, unit_of_time=time_unit, initial_flowrate=flowrate))

        return {'PUMPS': pumps}

    @staticmethod
    def _initializeValves(config, config_mode):
        num_columns = int(config[config_mode]['NUM_COLUMNS'])
        bus = int(config[config_mode]['BUS'])
        input_addr = int(config[config_mode]['VALVES_ADDR_IN'])
        waste_addr = int(config[config_mode]['VALVES_ADDR_WASTE'])

        v_in = ValveControllerI2c(device_info=[bus, input_addr])
        v_waste = ValveControllerI2c(device_info=[bus, waste_addr])

        valves = {'VALVES_IN': v_in, 'VALVES_WASTE': v_waste, }

        return valves

    @staticmethod
    def _initializeFracCol(config, config_mode):
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['FRAC_ADDR'])
        steps_rev = int(config[config_mode]['PUMP_STEPS_REV'])
        micros = int(config[config_mode]['PUMP_MICROS'])
        motor_current = int(config[config_mode]['PUMP_MOTOR_CURR'])
        pos_frac1 = int(config[config_mode]['POSITION_FRAC1'])
        pos_flwthru1 = int(config[config_mode]['POSITION_FLWTHRU1'])
        offset_frac = int(config[config_mode]['OFFSET_FRACTIONS'])
        offset_flwthru = int(config[config_mode]['OFFSET_FLWTHRU'])
        num_frac = int(config[config_mode]['NUM_FRACTIONS'])
        num_flwthru = int(config[config_mode]['NUM_FLWTHRU'])
        vol_frac = int(config[config_mode]['VOLUME_FRAC'])
        vol_flwthru = int(config[config_mode]['VOLUME_FLWTHRU'])

        motor = TicStepper(com_type='I2C', port_params=bus, address=addr, input_steps_per_rev=steps_rev)
        motor.setCurrentLimit(motor_current)
        stage = TicStage(ticStepper=motor, microStepFactor=micros)

        position_map = {}
        for i in range(0, num_frac):
            position_map['Frac' + str(i)] = pos_frac1 + offset_frac * i

        for i in range(0, num_flwthru):
            position_map['Flow' + str(i)] = pos_flwthru1 + offset_flwthru * i

        stage.setIndexedPositions(positionMap=position_map)
        frac_collector = {'FRAC_COLLECTOR': stage, 'VOL_FRAC': vol_frac, 'VOL_FLOWTHRU': vol_flwthru, }

        return frac_collector
