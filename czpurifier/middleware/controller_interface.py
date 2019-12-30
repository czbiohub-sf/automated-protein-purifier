"""Control-side representation of the hardware."""
import zmq
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class ControllerInterface():
    """Hardware communication interface and virutal hardware objects."""

    def __init__(self):
        # Hardware states
        self.position_names = []
        self.port_names = []
        self.curr_port = 'Unknown'
        self.pump_status = []
        self.flow_rates = []
        self.input_states = []
        self.waste_states = []

        # System parameters
        self.config_mode = []
        self.devices = {}

        # Communication interface
        context = zmq.Context()
        self._socket_availability = context.socket(zmq.PULL)
        self._socket_data_out = context.socket(zmq.PUSH)
        self._socket_data_in = context.socket(zmq.PULL)

    ######################
    # Hardware Interface #
    ######################

    def connect(self, address: str, alias: str = 'device'):
        """Connect to a preconfigured device.

        Parameters
        ----------
        address : str
            IPv4 address of the target system.
        alias : str
            Alias to give to the system when connected.
        """
        if alias not in self.devices:
            protocol_address = 'tcp://' + address
            self._socket_availability.connect(protocol_address + ':5000')
            available = self._socket_availablility.poll(timeout=1500)
            self._socket_availability.disconnect(protocol_address + ':5000')

            if available:
                self._socket_data_out.connect(protocol_address + ':5100')
                self._socket_data_in.connect(protocol_address + ':5200')
                self.devices[alias] = address
                data_out = 'connect,' + alias
                self.send(data_out)

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
        self.send('load_config' + self.config_mode)

    def send(self, command, response_func):
        """Transmit and receive data.

        Parameters
        ----------
        command : str
            Command to transmit
        response_func : function
            Function that receives and parses the command output.
        """
        self._tx(command)
        for dev, _ in enumerate(self.devices):
            resp = self._rx()
            if resp[0] in self.devices:
                resp_valid = response_func(resp[1])
                if not resp_valid:
                    log.error('Command `%s` generated invalid response `%s` from device `%s`', command, str(resp[1]), resp[0])
                else:
                    log.debug('Command `%s` generated response `%s` from device `%s`', command, str(resp[1]), resp[0])
            else:
                log.error('Response unknown: %s', str(resp))

    def _tx(self, data_out: str):
        self._socket_data_out.send_string(data_out)

    def _rx(self, t_out=1000):
        resp = []
        resp_waiting = self._socket_data_in(timeout=t_out)
        if resp_waiting:
            resp = self._socket_data_in.recv_pyobj()
        else:
            resp = ['Response not received']
        return resp

    def _okayResponseChecker(resp: str):
        ok = False
        if resp == 'OK':
            ok = True
        return ok

    ###############################
    # FRACTION COLLECTOR COMMANDS #
    ###############################

    def getPositions(self):
        cmd_to_send = 'reportFracCollectorPositions,'
        send_response_to = self._updatePositions
        self.send(cmd_to_send, send_response_to)

    def moveFracTo(self, indexed_position: str):
        if indexed_position in self.position_names:
            cmd_to_send = 'moveFracCollector,' + indexed_position
            send_response_to = self._okayResponseChecker
            self.send(cmd_to_send, send_response_to)

    def homeFrac(self):
        cmd_to_send = 'homeFracCollector,'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def _updatePositions(self, new_positions):
        resp = False
        if type(new_positions) is list:
            self.position_names = new_positions
            resp = True
        return resp

    #########################
    # ROTARY VALVE COMMANDS #
    #########################

    def getPorts(self):
        cmd_to_send = 'reportRotaryPorts,'
        send_response_to = self._updatePorts
        self.send(cmd_to_send, send_response_to)

    def getCurrentPort(self):
        cmd_to_send = 'getCurrentPort,'
        send_response_to = self._updateCurrPort
        self.send(cmd_to_send, send_response_to)

    def moveToPort(self, indexed_port: str):
        cmd_to_send = 'moveRotaryValve,' + indexed_port
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def homePorts(self):
        cmd_to_send = 'homeRotaryValve,'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def renamePort(self, port_num, port_name):
        cmd_to_send = 'renameRotaryPort,' + str(port_num) + ',' + port_name
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def _updatePorts(self, new_ports: list):
        resp = False
        if type(new_ports) is list:
            self.port_names = new_ports
            resp = True
        return resp

    def _updateCurrPort(self, curr_port: str):
        resp = False
        if type(curr_port) is str:
            self.curr_port = curr_port
            resp = True
        return resp

    #################
    # PUMP COMMANDS #
    #################

    def getPumpStatus(self):
        cmd_to_send = 'getPumpStatus,'
        send_response_to = self._updatePumpStatus
        self.send(cmd_to_send, send_response_to)

    def getFlowRates(self):
        cmd_to_send = 'getFlowRate,'
        send_response_to = self._updateFlowRates
        self.send(cmd_to_send, send_response_to)

    def setFlowRates(self, flow_rate):
        cmd_to_send = 'setFlowRate,' + str(flow_rate)
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def startPumping(self):
        cmd_to_send = 'startPumping,'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def stopPumping(self):
        cmd_to_send = 'stopPumping,'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def _updatePumpStatus(self, pump_status: list):
        resp = False
        if type(pump_status) is list:
            self.pump_status = pump_status
            resp = True
        return resp

    def _updateFlowRates(self, flow_rates: list):
        resp = False
        if type(flow_rates) is list:
            self.flow_rates = flow_rates
            resp = True
        return resp

    ###########################
    # SOLENOID VALVE COMMANDS #
    ###########################

    def getInputStates(self):
        cmd_to_send = 'getInputValves,'
        send_response_to = self._updateInput
        self.send(cmd_to_send, send_response_to)

    def getWasteStates(self):
        cmd_to_send = 'getWasteValves,'
        send_response_to = self._updateWaste
        self.send(cmd_to_send, send_response_to)

    def setInputStates(self, target_states: int):
        cmd_to_send = 'setInputValves,' + str(target_states)
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def setWasteStates(self, target_states: int):
        cmd_to_send = 'setWasteValves,' + str(target_states)
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def _updateInput(self, states: int):
        resp = False
        if type(states) is int:
            self.input_states = states
            resp = True
        return resp

    def _updateWaste(self, states: int):
        resp = False
        if type(states) is int:
            self.waste_states = states
            resp = True
        return resp
