"""Hardware peripheral initialization."""

from enum import Enum, auto
import logging
from logging import NullHandler
from time import sleep
from .hardware_setup import PurifierHardwareSetup
from .pump_controller import PumpController
from .valve_controller import ValveController
from pyconfighandler import validateConfig

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class MockHardwareSetup(PurifierHardwareSetup):
    """Setup hardware controllers as described by a config file."""

    @staticmethod
    def _initializeRotaryValve(config, config_mode):
        num_ports = int(config[config_mode]['ROTARY_NUM_PORTS'])
        port_names = ['NONE'] * num_ports
        for i in range(0, num_ports):
            try:
                port_names[i] = config[config_mode]['ROTARY_PORT_%s' % str(i + 1)]
            except Exception:
                pass
        rotary = RotaryController()
        rotary_valves = {'ROTARY': rotary, 'PORTS': port_names, 'NUM_PORTS': num_ports, }
        return rotary_valves

    @staticmethod
    def _initializePumps(config, config_mode):
        num_columns = int(config[config_mode]['NUM_COLUMNS'])
        vol_rev = float(config[config_mode]['PUMP_VOL_REV'])
        time_unit = config[config_mode]['PUMP_TIME_UNIT']
        flowrate = float(config[config_mode]['FLOWRATE'])

        pumps = []

        for i in range(0, num_columns):
            pumps.append(PumpControllerSim(vol_rev, time_unit, flowrate))

        pumps = {'PUMPS': pumps, 'NUM_COLS': num_columns, }

        return pumps

    @staticmethod
    def _initializeValves(config, config_mode):
        initial_in = int(config[config_mode]['INIT_IN_STATES'])
        initial_waste = int(config[config_mode]['INIT_WASTE_STATES'])

        v_in = ValveControllerSim()
        v_waste = ValveControllerSim()

        v_in.valve_states = initial_in
        v_waste.valve_states = initial_waste

        valves = {'VALVES_IN': v_in, 'VALVES_WASTE': v_waste, }

        return valves

    @staticmethod
    def _initializeFracCol(config, config_mode):
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

        stage = FractionCollectorSim()
        position_map = {}
        for i in range(0, num_frac):
            position_map['Frac' + str(i + 1)] = pos_frac1 + offset_frac * i

        for i in range(0, num_flwthru):
            position_map['Flow' + str(i + 1)] = pos_flwthru1 + offset_flwthru * i

        position_map['Safe'] = pos_safe

        stage.setIndexedPositions(positionMap=position_map)
        frac_collector = {'FRAC_COLLECTOR': stage, 'FRAC_HOME_DIR': frac_home_dir, 'VOL_FRAC': vol_frac, 'VOL_FLOWTHRU': vol_flwthru, }

        return frac_collector

class RotaryController():
    """
    Updates the current port based on where it is desired to go
    """
    def __init__(self):
        self.current_port = -1
        log.debug('Rotary controller initialized.')
    def moveToPort(self, port_num):
        """
        TODO: Make sure the port number exists
        Updates the current port to the new port
        """
        sleep(2)
        self.current_port = port_num
        log.debug('Moved port to {}'.format(port_num))
    def home(self):
        sleep(2)
        self.current_port = 0
        log.debug('Homed Rotary Pump')
        
class PumpControllerSim(PumpController):

    def _updateVelocity(self, revs_per_second):
        logging.debug('Updating Pump Velocity')

    def _stop(self):
        logging.debug('Stoping Pump')

class ValveControllerSim(ValveController):
    def _write(self):
        logging.debug('Updated Valve State')

class FractionCollectorSim():
    def __init__(self):
        self._indexedPositions = []
        self._currentPosition = None
        self._ticStepper = TicStepperSim()

    def setIndexedPositions(self, positionMap):
        self._indexedPositions = positionMap
        logging.debug('Set all the indexed positions')

    def getIndexedPositions(self):
        return self._indexedPositions

    def moveToIndexedPosition(self, position, open_loop_assert):
        self._currentPosition = position
        logging.debug('New position is set to {}'.format(position))
    
class TicStepperSim():
    def __init__(self):
        self.home_loc = None
    
    def home(self, home_dir):
        self.home_loc = home_dir
    
    def isHomed(self):
        sleep(3)
        return True