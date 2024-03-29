"""General purpose valve controller classes."""
try:  # Import I2C module
    from smbus2 import SMBus, i2c_msg
except ImportError:
    print('Unable to import smbus2 for I2C communication.')
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class ValveController():
    """Base class for controlling valve states.

    Parameters
    ----------
    valve_states : int
        Initial states of all valves controlled by the hardware.

    Attributes
    ----------
    valve_states : int
        Current state of all valves.

    """

    def __init__(self, init_valve_states: int = 0):
        self._valve_states = init_valve_states
        self.states = self._valve_states
        log.debug('Valve controller initialized.')

    def activate(self, valve_number):
        """
        Activate a single valve.

        Parameters
        ----------
        valve_number : int
            The valve to activate.

        """
        self.states = self.states | 1 << valve_number
        log.info('Valve activated: %s', str(valve_number))

    def deactivate(self, valve_number):
        """
        Deactivate a single valve.

        Parameters
        ----------
        valve_number : int
            The valve to deactivate.

        """
        self.states = self.states & ~(1 << valve_number)
        log.info('Valve deactivated: %s', str(valve_number))

    def _write(self):
        """Write valve binary states to hardware."""
        raise NotImplementedError()

    @property
    def states(self):
        """
        Read the current states of all valves.

        Returns
        -------
        _valve_states : int
            Integer representation of binary valve states.
        """
        return self._valve_states

    @states.setter
    def states(self, states):
        """
        Overwrite the states of all valves at once.

        Parameters
        ----------
        states : int
            Integer representation of the desired binary valve states.

        """
        self._valve_states = states
        self._write()
        log.info('Valve controller states set: %s', str(states))


class ValveControllerMCP23017(ValveController):
    """MCP23017 valve controller with I2C support.

    Parameters
    ----------
    device_info : list
        A list specifying the I2C bus and the device address on the bus.
    """

    def __init__(self, device_info: list, init_valve_states: int = 0):
        bus = device_info[0]
        self.address = device_info[1]
        self.bus = SMBus(bus)
        output_mode = i2c_msg.write(self.address, [0x00, 0x00])
        self.bus.i2c_rdwr(output_mode)
        log.debug('Valve controller I2C bus, address: %s, %s', str(bus), str(self.address))
        super().__init__(init_valve_states)

    def _write(self):
        msg = i2c_msg.write(self.address, [0x12, self._valve_states])
        self.bus.i2c_rdwr(msg)
