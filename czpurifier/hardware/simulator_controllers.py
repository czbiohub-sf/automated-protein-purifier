"""Rotary Valve Tic Simulator"""
from .rotary_controller import RotaryController

class RotaryControllerSimulator(RotaryController):
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

    def __init__(self):
        super().__init__()

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
            print('Moving forward with velocity')
        else:
            print('Going back')
        sleep(4)
        print('Reached position')

    def home(self):
        """Reset the position index of the selector valve to match the encoder.

        This is used for returning to a known location near Port0. The position
        of Port0 will still need to be discovered after homing.
        """
        print('going home')
