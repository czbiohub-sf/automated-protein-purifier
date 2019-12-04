"""Rotary valve controller classes."""
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class RotaryController():
    """Base class for controlling a rotary valve."""

    def __init__(self):

        self._position_known = False
        self.current_port = -1
        log.info('Rotary controller initialized.')

    def moveToPort(self, port: int):
        """Travel to the desired port.

        Find the location of Port0 if it has not been previously discovered.
        Calculate the number of ports to travel and advance to the position one
        port at a time.

        Parameters
        ----------
        port : int
            Target port index, do not use negative numbers.
        """
        if not self._position_known:
            log.debug('Controller not homed. Homing now.')
            self.home()

        ports_to_move = port - self.current_port
        log.info('Moving %s ports away from current port #%s.', str(ports_to_move), str(self.current_port))
        if ports_to_move < 0:
            move_fwd = False
            decrement = 1
        else:
            move_fwd = True
            decrement = -1

        while abs(ports_to_move):
            self._seekPort(move_fwd)
            ports_to_move = ports_to_move + decrement
            self.current_port = self.current_port - decrement

    def _seekPort(self, move_fwd: bool):
        """Advance to the next port in the specified direction."""
        raise NotImplementedError()

    def home(self):
        """Move the rotary valve to a known location."""
        raise NotImplementedError()


class RotaryControllerTic(RotaryController):
    """Rotary valve controller dependent on a Tic stepper driver.

    Parameters
    ----------
    MotorObj : TicStepper
        The TicStepper object interfacing with the motor driver hardware.
    home_fwd : bool
        Homing will be in the forward direction if True
    analog_pin : str
        Pin to be used for reading the analog signal of the port encoder.
    thresh_lower : int
        16-bit ADC value indicating when a port is centered.
    thresh_upper : int
        16-bit ADC value indicating when a port is not aligned. Can't be 0xFFFF
        as the value is reserved for a "Cannot read" signal on the Tic board.
    seek_vel : int
        Velocity to use when searching for a neighboring port. Steps / 10000s
    """

    def __init__(self, MotorObj, home_fwd=True, analog_pin='TX',
                 thresh_lower=0x2000, thresh_upper=0xE000, seek_vel=2000000):
        super().__init__()
        if home_fwd:
            self._home_dir = 'fwd'
        else:
            self._home_dir = 'rev'
        self._analog_pin = analog_pin
        self._seek_vel = seek_vel
        self._thresh = [thresh_lower, thresh_upper]
        self._motor = MotorObj
        self._motor.enable = True

        if analog_pin == 'TX':
            self._analog = [self._motor._command_dict['gVariable'],
                            self._motor._variable_dict['analog_reading_TX']]
        elif analog_pin == 'RX':
            self._analog = [self._motor._command_dict['gVariable'],
                            self._motor._variable_dict['analog_reading_RX']]
        elif analog_pin == 'SCL':
            self._analog = [self._motor._command_dict['gVariable'],
                            self._motor._variable_dict['analog_reading_SCL']]
        elif analog_pin == 'SDA':
            self._analog = [self._motor._command_dict['gVariable'],
                            self._motor._variable_dict['analog_reading_SDA']]

    def __del__(self):
        self._motor.enable = False

    def _seekPort(self, move_fwd=True):
        """Advance to the next port.

        Set a target position beyond where the port is expected to reside. If
        the analog pin reads low (Active Low), continue moving until analog pin
        reads high. Continue moving until pin reads low and stop. Home during
        first call to set a known position.

        Parameters
        ----------
        move_fwd : bool
            Advance to the port in the forward direction if True.

        """
        if move_fwd:
            vel = self._seek_vel
        else:
            vel = -self._seek_vel
        self._motor.velocityControl(vel)
        while self._readAnalog() < self._thresh[1]:
            pass
        while self._readAnalog() > self._thresh[0]:
            pass
        self._motor.stop()

    def home(self):
        """Reset the position index of the selector valve to match the encoder.

        This is used for returning to a known location near Port0. The position
        of Port0 will still need to be discovered after homing.
        """
        self._motor.home(self._home_dir)
        while not self._motor.isHomed():
            pass
        self._position_known = True
        self.current_port = -1

    def _readAnalog(self):
        """Read the analog pin connected to the port encoder."""
        analog_reading = self._motor.com.send(self._analog[0], self._analog[1])
        return self._motor.bytesToInt(analog_reading)
