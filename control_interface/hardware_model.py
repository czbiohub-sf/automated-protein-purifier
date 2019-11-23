"""Control-side representation of the hardware."""
import zmq
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class HardwareModel():

    def __init__(self):
        self.config_mode = []
        self.devices = {}
        self.last_resp = {}
        self.pumps = []
        self.frac_collector = []
        self.rotary = []
        self.valves = []
        context = zmq.Context()
        self._socket_availablility = context.socket(zmq.PULL)
        self._socket_data_out = context.socket(zmq.PUSH)
        self._socket_data_in = context.socket(zmq.PULL)

    def connect(self, address: str, alias: str = 'device'):
        """Connect to a preconfigured device.

        Parameters
        ----------
        address : str
            IPv4 address of the target system.
        alias : str
            Alias to give to the system when connected.
        """
        if not self.devices[alias]:
            protocol_address = 'tcp://' + address
            self._socket_availablility.connect(protocol_address + ':5000')
            available = self._socket_availablility.poll(timeout=1500)
            self._socket_availability.disconnect(protocol_address + ':5000')

            if available:
                self._socket_data_out.connect(protocol_address + ':5100')
                self._socket_data_in.connect(protocol_address + ':5200')
                self.devices[alias] = address
                data_out = 'connect,' + alias
                self._send(data_out)

    def disconnect(self, alias: str = 'device'):
        """Disconnect from a currently connected device.

        Parameters
        ----------
        alias : str
            Alias of device given when connecting.
        """
        self.socket.data_out.send_string('disconnect')
        protocol_address = 'tcp://' + self.devices[alias]
        self.socket_data_out.disconnect(protocol_address + ':5100')
        self.socket_data_in.disconnect(protocol_address + ':5200')
        del self.devices[alias]

    def loadConfig(self):
        """Load a configuration on all connected devices."""
        for device in self.devices:
            address = self.devices[device]
            self.disconnect(device)
            self.connect(address, device)
        self._send('load_config' + self.config_mode)

    def _send(self, data_out: str):
        self.socket_data_out.send_string(data_out)

    def _recv(self, t_out=1000):
        for resp_num, _ in enumerate(self.devices):
            resp_waiting = self._socket_data_in(timeout=t_out)
            if resp_waiting:
                resp = self._socket_data_in.recv_pyobj()
                self.last_resp[resp[0]] = resp[1]
            else:
                log.error('Failed to receive response #%s out of %s.', str(resp_num), str(len(self.devices)))


#    def _pollHardware(self):
#        try:
#            self._send()


class FracCollectorModel():

    def __init__(self):
        self.index_list = []
        self.curr_position = 'Unknown'

class PumpModel():

    def __init__(self):
        self.state = 'Unknown'
        self.num_pumps =
