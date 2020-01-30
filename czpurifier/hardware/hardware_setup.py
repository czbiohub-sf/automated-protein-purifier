"""Hardware peripheral initialization."""

from enum import Enum, auto
import logging
from logging import NullHandler
from .pump_controller import PumpControllerTic
from .rotary_controller import RotaryControllerTic
from .valve_controller import ValveControllerMCP23017
from pyconfighandler import validateConfig
from pymotors import TicStepper, TicStage

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class DefaultConfigFields(Enum):
    NUM_COLUMNS = auto()
    ROTARY_STEPS_REV = auto()
    ROTARY_MICROS = auto()
    ROTARY_HOME_DIR = auto()
    PUMP_STEPS_REV = auto()
    PUMP_MICROS = auto()
    ROTARY_ADDR = auto()
    VALVES_ADDR_IN = auto()
    VALVES_ADDR_WASTE = auto()
    PUMP_ADDR_START = auto()
    PUMP_MOTOR_CURR = auto()
    ROTARY_MOTOR_CURR = auto()


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

    def configValidation(self, path_to_config, required_config_fields=DefaultConfigFields):
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
        steps_rev = int(config[config_mode]['ROTARY_STEPS_REV'])
        micros = int(config[config_mode]['ROTARY_MICROS'])
        motor_current = int(config[config_mode]['ROTARY_MOTOR_CURR'])
        home_dir = config[config_mode]['ROTARY_HOME_DIR']
        encoder_pin = config[config_mode]['ROTARY_ENCODE_PIN']
        num_ports = int(config[config_mode]['ROTARY_NUM_PORTS'])
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['ROTARY_ADDR'], 16)

        port_names = ['NONE'] * num_ports

        for i in range(0, num_ports):
            try:
                port_names[i] = config[config_mode]['ROTARY_PORT_%s' % str(i + 1)]
            except Exception:
                pass

        motor = TicStepper(com_type='I2C', port_params=bus, address=addr, input_steps_per_rev=steps_rev, input_rpm=60)
        motor.microsteps = 1 / micros

        rotary = RotaryControllerTic(MotorObj=motor, home_dir=home_dir, analog_pin=encoder_pin, motor_current=motor_current)
        rotary_valves = {'ROTARY': rotary, 'PORTS': port_names, 'NUM_PORTS': num_ports, }
        return rotary_valves

    @staticmethod
    def _initializePumps(config, config_mode):
        num_columns = int(config[config_mode]['NUM_COLUMNS'])
        steps_rev = int(config[config_mode]['PUMP_STEPS_REV'])
        micros = int(config[config_mode]['PUMP_MICROS'])
        motor_current = int(config[config_mode]['PUMP_MOTOR_CURR'])
        vol_rev = float(config[config_mode]['PUMP_VOL_REV'])
        time_unit = config[config_mode]['PUMP_TIME_UNIT']
        flowrate = float(config[config_mode]['FLOWRATE'])
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['PUMP_ADDR_START'], 16)

        pumps = []

        for i in range(0, num_columns):
            motor = TicStepper(com_type='I2C', port_params=bus, address=addr + i, input_steps_per_rev=steps_rev, input_rpm=500)
            motor.microsteps = 1 / micros
            motor.setCurrentLimit(motor_current)
            motor.enable = True
            pumps.append(PumpControllerTic(MotorObj=motor, vol_per_rev=vol_rev, unit_of_time=time_unit, initial_flowrate=flowrate))

        pumps = {'PUMPS': pumps, 'NUM_COLS': num_columns, }

        return pumps

    @staticmethod
    def _initializeValves(config, config_mode):
        bus = int(config[config_mode]['BUS'])
        input_addr = int(config[config_mode]['VALVES_ADDR_IN'], 16)
        waste_addr = int(config[config_mode]['VALVES_ADDR_WASTE'], 16)
        initial_in = int(config[config_mode]['INIT_IN_STATES'])
        initial_waste = int(config[config_mode]['INIT_WASTE_STATES'])

        v_in = ValveControllerMCP23017(device_info=[bus, input_addr])
        v_waste = ValveControllerMCP23017(device_info=[bus, waste_addr])

        v_in.valve_states = initial_in
        v_waste.valve_states = initial_waste

        valves = {'VALVES_IN': v_in, 'VALVES_WASTE': v_waste, }

        return valves

    @staticmethod
    def _initializeFracCol(config, config_mode):
        bus = int(config[config_mode]['BUS'])
        addr = int(config[config_mode]['FRAC_ADDR'], 16)
        steps_rev = int(config[config_mode]['FRAC_STEPS_REV'])
        micros = int(config[config_mode]['FRAC_MICROS'])
        motor_current = int(config[config_mode]['FRAC_MOTOR_CURR'])
        rpm = int(config[config_mode]['FRAC_RPM'])
        frac_home_dir = config[config_mode]['FRAC_HOME_DIR']
        pos_frac1 = int(config[config_mode]['POSITION_FRAC1'])
        pos_flwthru1 = int(config[config_mode]['POSITION_FLWTHRU1'])
        pos_safe = int(config[config_mode]['POSITION_SAFE'])
        offset_frac = int(config[config_mode]['OFFSET_FRACTIONS'])
        offset_flwthru = int(config[config_mode]['OFFSET_FLWTHRU'])
        num_frac = int(config[config_mode]['NUM_FRACTIONS'])
        num_flwthru = int(config[config_mode]['NUM_FLWTHRU'])
        vol_frac = int(config[config_mode]['VOLUME_FRAC'])
        vol_flwthru = int(config[config_mode]['VOLUME_FLWTHRU'])

        motor = TicStepper(com_type='I2C', port_params=bus, address=addr, input_steps_per_rev=steps_rev, input_rpm=rpm)
        motor.setCurrentLimit(motor_current)
        stage = TicStage(ticStepper=motor, microStepFactor=micros)
        stage.enable()

        position_map = {}
        for i in range(0, num_frac):
            position_map['Frac' + str(i)] = pos_frac1 + offset_frac * i

        for i in range(0, num_flwthru):
            position_map['Flow' + str(i)] = pos_flwthru1 + offset_flwthru * i

        position_map['Safe'] = pos_safe

        stage.setIndexedPositions(positionMap=position_map)
        frac_collector = {'FRAC_COLLECTOR': stage, 'FRAC_HOME_DIR': frac_home_dir, 'VOL_FRAC': vol_frac, 'VOL_FLOWTHRU': vol_flwthru, }

        return frac_collector
