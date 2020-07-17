"""Methods for simulating purifier hardware."""

from .hardware_setup import PurifierHardwareSetup
from .hardware_controller import HardwareController
from .simulator_controllers import RotaryControllerSimulator
import logging
from logging import NullHandler
from time import sleep

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class HardwareSimulator(PurifierHardwareSetup):
    """
    Used to simulate hardware responses
    The static functions that are overwritten here
    """
    # All the methods are called here including the ones overwritten
    # to keep track. It can be deleted later
    # Deleted all calls to hardware drivers. TODO: Switch to getting feedback
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
        rotary = RotaryControllerSimulator()
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
            #TODO: Fake the motor
            #motor = TicStepper(com_type='I2C', port_params=bus, address=addr + i, input_steps_per_rev=steps_rev, input_rpm=500)
            #motor.microsteps = 1 / micros
            #motor.setCurrentLimit(motor_current)
            #motor.enable = True
            #pumps.append(PumpControllerTic(MotorObj=motor, vol_per_rev=vol_rev, unit_of_time=time_unit, initial_flowrate=flowrate))
            pumps.append('pump {}'.format(i))

        pumps = {'PUMPS': pumps, 'NUM_COLS': num_columns, }

        return pumps

    @staticmethod
    def _initializeValves(config, config_mode):
        bus = int(config[config_mode]['BUS'])
        input_addr = int(config[config_mode]['VALVES_ADDR_IN'], 16)
        waste_addr = int(config[config_mode]['VALVES_ADDR_WASTE'], 16)
        initial_in = int(config[config_mode]['INIT_IN_STATES'])
        initial_waste = int(config[config_mode]['INIT_WASTE_STATES'])

        #v_in = ValveControllerMCP23017(device_info=[bus, input_addr])
        #v_waste = ValveControllerMCP23017(device_info=[bus, waste_addr])

        #v_in.valve_states = initial_in
        #v_waste.valve_states = initial_waste

        valves = {'VALVES_IN': 'v_in', 'VALVES_WASTE': 'v_waste', }

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

        #motor = TicStepper(com_type='I2C', port_params=bus, address=addr, input_steps_per_rev=steps_rev, input_rpm=rpm)
        #motor.setCurrentLimit(motor_current)
        #stage = TicStage(ticStepper=motor, microStepFactor=micros)
        #stage.enable()

        position_map = {}
        for i in range(0, num_frac):
            position_map['Frac' + str(i + 1)] = pos_frac1 + offset_frac * i

        for i in range(0, num_flwthru):
            position_map['Flow' + str(i + 1)] = pos_flwthru1 + offset_flwthru * i

        position_map['Safe'] = pos_safe

        #stage.setIndexedPositions(positionMap=position_map)
        frac_collector = {'FRAC_COLLECTOR': 'stage', 'FRAC_HOME_DIR': frac_home_dir, 'VOL_FRAC': vol_frac, 'VOL_FLOWTHRU': vol_flwthru, }

        return frac_collector



class HardwareControllerSimulator(HardwareController):
    """
    Parameters
    ----------
    hw_config_file_path : str
        String indicating system path to hardware config file
    config_mode : str
        Config section to load in addition to 'DEFAULT'

    """
    pass