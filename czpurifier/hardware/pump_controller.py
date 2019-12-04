from enum import Enum, auto
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class TimeUnits(Enum):
    """Supported units of time for the PumpController class."""

    s = auto()
    m = auto()
    h = auto()


class PumpController():
    """Pump controller base class.

    Parameters
    ----------
    vol_per_rev : int
        Volume displaced by one revolution of the pump.
    unit_of_time : str
        Units of time to use when calling the flowrate method.

    """

    def __init__(self, vol_per_rev, unit_of_time, initial_flowrate):
        if TimeUnits[unit_of_time] is TimeUnits.s:
            self._UNIT_TIME = 1
        elif TimeUnits[unit_of_time] is TimeUnits.m:
            self._UNIT_TIME = 60
        elif TimeUnits[unit_of_time] is TimeUnits.h:
            self._UNIT_TIME = 3600
        else:
            raise ValueError('Unit of time `%s` is not supported.', unit_of_time)
        self._VOL_PER_REV = vol_per_rev
        self._revs_per_second = initial_flowrate / (self._VOL_PER_REV * self._UNIT_TIME)
        self.running = False
        log.debug('Pump controller initialized.')

    def __del__(self):
        self.stop()

    @property
    def flow_rate(self):
        """Retrieve the target flow rate of the pump."""
        return self._VOL_PER_REV * self._revs_per_second * self._UNIT_TIME

    @flow_rate.setter
    def flow_rate(self, target_rate):
        """Set the target flow rate of the pump.

        Parameters
        ----------
        target_rate : float
            Target volume to output over the time period specified in init.
        """
        self._revs_per_second = target_rate / (self._VOL_PER_REV * self._UNIT_TIME)
        if self.running:
            self._updateVelocity(self._revs_per_second)
        log.info('Pump controller set to %s units per %s second(s).', str(target_rate), str(self._UNIT_TIME))

    def start(self):
        """Start the pump."""
        self.running = True
        self._updateVelocity(self._revs_per_second)
        log.info('Pump started.')

    def stop(self):
        """Stop the pump."""
        self._stop()
        self.running = False
        log.info('Pump stopped.')

    def _updateVelocity(self, revs_per_second):
        raise NotImplementedError()

    def _stop(self):
        raise NotImplementedError()


class PumpControllerTic(PumpController):
    """Pump controller class driven by a Tic stepper driver board.

    Parameters
    ----------
    MotorObj : TicStepper
        Object interfacing with the motor hardware.
    vol_per_rev : int
        Volume displaced by one revolution of the pump.
    unit_of_time : str
        Units of time to use when calling the flowrate method.
    """

    def __init__(self, MotorObj, vol_per_rev, unit_of_time, initial_flowrate):
        self._motor = MotorObj
        self._motor.enable = True
        super().__init__(vol_per_rev, unit_of_time, initial_flowrate)

    def __del__(self):
        self.stop()
        self._motor.enable = False

    def _updateVelocity(self, revs_per_second):
        """Set the velocity of the pump by converting flowrate to steps / 10000s."""
        steps_per_s = self._motor._microsteps_per_full_step * self._motor.steps_per_rev * revs_per_second
        self._motor.velocityControl(steps_per_s * 10000)

    def _stop(self):
        self._motor.halt()
