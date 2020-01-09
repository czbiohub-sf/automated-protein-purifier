"""Interface between UI and communication layers."""
import zmq
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class ControllerInterface():
    """Hardware communication interface and virutal hardware objects.

    Parameters
    ----------
    timeout : int
        Maximum number of milliseconds to wait for device response.
    """

    def __init__(self, timeout=10000):
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
        self.timeout = timeout
        # Communication interface
        context = zmq.Context()
        self._socket_availability = context.socket(zmq.PULL)
        self._socket_data_out = context.socket(zmq.PUSH)
        self._socket_data_in = context.socket(zmq.PULL)

    ######################
    # Hardware Interface #
    ######################

    def connect(self, address: str, alias: str = 'device'):
        """Connect to a device if available.

        Parameters
        ----------
        address : str
            IPv4 address of the target system.
        alias : str
            Alias to give to the system when connected.
        """
        if alias not in self.devices:
            available = self.pollDeviceAvailability(address)
            if available:
                logging.info("Device at `%s` is available.", address)
                self.hardConnect(address, alias)
            else:
                logging.info("Device at `%s` not available.", address)

    def hardConnect(self, address: str, alias: str = 'device'):
        """Connect to sockets at address and save address.

        Parameters
        ----------
        address : str
            Address to connect to.
        alias : str
            Name to assign to device. Device will respond with alias.
        """
        protocol_address = 'tcp://' + address
        self._socket_data_out.connect(protocol_address + ':5100')
        self._socket_data_in.connect(protocol_address + ':5200')

        self.devices[alias] = address
        data_out = 'connect,' + alias
        self.send(data_out, self._okayResponseChecker)
        logging.info("Device at `%s` connected as `%s`.", address, alias)

    def disconnect(self, alias: str = 'device'):
        """Disconnect from a currently connected device.

        Parameters
        ----------
        alias : str
            Alias of device given when connecting.
        """
        try:
            self.send('disconnect', self._okayResponseChecker)
            protocol_address = 'tcp://' + self.devices[alias]
            self._socket_data_out.disconnect(protocol_address + ':5100')
            self._socket_data_in.disconnect(protocol_address + ':5200')
            logging.info("Device with alias `%s` has been disconnected.", alias)
            del self.devices[alias]
        except KeyError:
            log.warning('Device with alias `%s` is not connected.', alias)

    def flushBuffer(self):
        """Discard anything that is in the receive buffer.

        Parameters
        ----------
        timeout : int
            Milliseconds to wait for data while polling.
        """
        while self._socket_data_in.poll(timeout=10):
            self._socket_data_in.recv_pyobj()

    def loadConfig(self):
        """Load a configuration on all connected devices."""
        if self.config_mode:
            logging.info("Loading configuration `%s`.", self.config_mode)
            self.send('loadConfig,' + self.config_mode, self._okayResponseChecker)
        else:
            logging.warning("Set config_mode parameter before calling.")

    def send(self, command, response_func):
        """Transmit and receive data.

        Parameters
        ----------
        command : str
            Command to transmit
        response_func : function
            Function that receives and parses the command output.
        """
        self.flushBuffer()
        if self.devices:
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
        else:
            log.warning('Device must be connected prior to issuing commands.')

    def pollDeviceAvailability(self, ip_address: str):
        """Poll the availability socket of device at address.

        Parameters
        ----------
        ip_address : str
            Address to poll for device availability.
        """
        log.info("Polling device at `%s` for availability.", ip_address)
        protocol_address = 'tcp://' + ip_address
        self._socket_availability.connect(protocol_address + ':5000')
        available = self._socket_availability.poll(timeout=1500)
        self._socket_availability.disconnect(protocol_address + ':5000')
        return available

    def _tx(self, data_out: str):
        self._socket_data_out.send_string(data_out)
        logging.debug('Transmitted data: %s', data_out)

    def _rx(self):
        resp = []
        resp_waiting = self._socket_data_in.poll(timeout=self.timeout)
        if resp_waiting:
            resp = self._socket_data_in.recv_pyobj()
            logging.debug('Received data: %s', str(resp))
        else:
            resp = ['Response not received']
        return resp

    @staticmethod
    def _okayResponseChecker(resp: str):
        ok = False
        if resp == 'OK':
            ok = True
        return ok

    ###############################
    # FRACTION COLLECTOR COMMANDS #
    ###############################

    def getPositions(self):
        """Request fraction collector position names."""
        logging.info("Updating position labels from fraction collector.")
        cmd_to_send = 'reportFracCollectorPositions'
        send_response_to = self._updatePositions
        self.send(cmd_to_send, send_response_to)

    def moveFracTo(self, indexed_position: str):
        """Move fraction collector to indexed position.

        Parameters
        ----------
        indexed_position : str
            Position name to travel to.
        """
        logging.info("Moving fraction collector to position `%s`.", indexed_position)
        if indexed_position in self.position_names:
            cmd_to_send = 'moveFracCollector,' + indexed_position
            send_response_to = self._okayResponseChecker
            self.send(cmd_to_send, send_response_to)
        else:
            logging.warning("Position `%s` is not recognized.", indexed_position)

    def homeFrac(self):
        """Home the fraction collector."""
        logging.info("Homing fraction collector.")
        cmd_to_send = 'homeFracCollector'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def _updatePositions(self, new_positions):
        resp = False
        if type(new_positions) is dict:
            self.position_names = list(new_positions.keys())
            resp = True
        return resp

    #########################
    # ROTARY VALVE COMMANDS #
    #########################

    def getPorts(self):
        """Request port names of the rotary valve."""
        logging.info("Updating port names of rotary valve.")
        cmd_to_send = 'reportRotaryPorts'
        send_response_to = self._updatePorts
        self.send(cmd_to_send, send_response_to)

    def getCurrentPort(self):
        """Request port name of current port."""
        logging.info("Updating current port.")
        cmd_to_send = 'getCurrentPort'
        send_response_to = self._updateCurrPort
        self.send(cmd_to_send, send_response_to)

    def selectPort(self, indexed_port: str):
        """Move rotary valve to the indicated port.

        Parameters
        ----------
        indexed_port : str
            Port to move to.
        """
        logging.info("Moving to port `%s`.", indexed_port)
        cmd_to_send = 'moveRotaryValve,' + indexed_port
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def homePorts(self):
        """Home the rotary valve."""
        cmd_to_send = 'homeRotaryValve'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def renamePort(self, port_num: int, port_name: str):
        """Rename a specified port position.

        Parameters
        ----------
        port_num : int
            Port position to be renamed.
        port_name : str
            Name to give specified port position.
        """
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
        """Request current status of pumps."""
        cmd_to_send = 'getPumpStatus'
        send_response_to = self._updatePumpStatus
        self.send(cmd_to_send, send_response_to)

    def getFlowRates(self):
        """Request current flow rates of pumps."""
        cmd_to_send = 'getFlowRate'
        send_response_to = self._updateFlowRates
        self.send(cmd_to_send, send_response_to)

    def setFlowRates(self, flow_rate):
        """Set flow rates of all pumps."""
        cmd_to_send = 'setFlowRate,' + str(flow_rate)
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def startPumping(self):
        """Start pumping all pumps."""
        cmd_to_send = 'startPumping'
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def stopPumping(self):
        """Stop all pumps."""
        cmd_to_send = 'stopPumping'
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
        """Request current states of input solenoid valves."""
        cmd_to_send = 'getInputValves'
        send_response_to = self._updateInput
        self.send(cmd_to_send, send_response_to)

    def getWasteStates(self):
        """Request current states of waste solenoid valves."""
        cmd_to_send = 'getWasteValves'
        send_response_to = self._updateWaste
        self.send(cmd_to_send, send_response_to)

    def setInputStates(self, target_states: int):
        """Set states of input solenoid valves."""
        cmd_to_send = 'setInputValves,' + str(target_states)
        send_response_to = self._okayResponseChecker
        self.send(cmd_to_send, send_response_to)

    def setWasteStates(self, target_states: int):
        """Set states of waste solenoid valves."""
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
