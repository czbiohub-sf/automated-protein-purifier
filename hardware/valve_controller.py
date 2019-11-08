"""General purpose valve controller classes."""
try:  # Import I2C module
    from smbus2 import SMBus, i2c_msg
except ImportError:
    print('Unable to import smbus2 for I2C communication.')


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
        self.valve_states = self._valve_states

    def valve_activate(self, valve_number):
        """
        Activate a single valve.

        Parameters
        ----------
        valve_number : int
            The valve to activate.

        """
        self.valve_states = self.valve_states | 1 << valve_number
        self._write()

    def valve_deactivate(self, valve_number):
        """
        Deactivate a single valve.

        Parameters
        ----------
        valve_number : int
            The valve to deactivate.

        """
        inverse = ~self.valve_states + 1
        off_inverse = inverse | 1 << valve_number
        self.valve_states = ~off_inverse + 1
        self._write()

    def _write(self):
        """Write valve binary states to hardware."""
        raise NotImplementedError()

    @property
    def valve_states(self):
        """
        Read the current states of all valves.

        Returns
        -------
        _valve_states : int
            Integer representation of binary valve states.
        """
        return self._valve_states

    @valve_states.setter
    def valve_states(self, states):
        """
        Overwrite the states of all valves at once.

        Parameters
        ----------
        states : int
            Integer representation of the desired binary valve states.

        """
        self._valve_states = states
        self._write()


class ValveControllerI2c(ValveController):
    """Valve controller with I2C support.

    Parameters
    ----------
    device_info : list
        A list specifying the I2C bus and the device address on the bus.
    """

    def __init__(self, device_info: list, init_valve_states: int = 0):
        bus = device_info[0]
        self.address = device_info[1]
        self.bus = SMBus(bus)
        super().__init__(init_valve_states)

    def _write(self):
        i2c_msg.write(self.address, self.valve_states)
