"""Protein purifier device communication and execution script."""
import zmq
from pkg_resources import Requirement, resource_filename
from czpurifier.hardware import HardwareController
import logging
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class DeviceInterface():
    """Device interface of protein purifier.

    Parameters
    ----------
    ip_address : str
        Address to send and receive data.
    timeout_recv : float
        Number of seconds to wait for data.

    """

    def __init__(self, ip_address='127.0.0.1', timeout_recv=1):
        # Set sockets for receiving and transmitting data.
        context = zmq.Context()
        self.socket_availability = context.socket(zmq.PUSH)
        self.socket_availability.bind("tcp://" + ip_address + ":5000")
        self.socket_data_in = context.socket(zmq.PULL)
        self.socket_data_in.bind("tcp://" + ip_address + ":5100")
        self.socket_data_out = context.socket(zmq.PUSH)
        self.socket_data_out.bind("tcp://" + ip_address + ":5200")

        # Set other class parameters.
        self._device_id = None
        self.timeout_recv = timeout_recv
        self.hardware_config_file = resource_filename(Requirement.parse("czpurifier"), "autopurifier_hardware.config")
        self.cmd_dict = {'connect': self.connect,
                         'disconnect': self.disconnect,
                         'loadConfig': self.loadConfig,
                         }

    def autorun(self):
        """Wait for data and execute. Signal if device is available."""
        while True:
            self.signalAvailability()
            data_in = ['None']
            data_in = self.receiveData()
            if data_in != 'None':
                resp = self.executeCall(data_in)
                self.sendData(resp)

    def connect(self, device_id):
        """Make device unavailable by granting it a device ID.

        Parameters
        ----------
        device_id : str
            Identity of device. Used for transimtting data and availability.
        """
        self._device_id = device_id

    def disconnect(self):
        """Make device available."""
        self._device_id = None

    def executeCall(self, input):
        """Convert arguments and execute command.

        Parameters
        ----------
        input : list
            command and arugments written as strings.
        """
        cmd = input[0]
        args = input[1:]
        num_args = len(args)
        arg = []

        # For each argument, attempt to convert to int or leave as string.
        for i in range(num_args):
            if i != '':
                try:
                    arg.append(int(args[i]))

                except ValueError:
                    arg.append(args[i])
            else:
                num_args = 0

        if cmd in self.cmd_dict and num_args == 0:
            resp = self.cmd_dict[cmd]
        elif cmd in self.cmd_dict and num_args == 1:
            resp = self.cmd_dict[cmd](arg[0])
        elif cmd in self.cmd_dict and num_args == 2:
            resp = self.cmd_dict[cmd](arg[0], arg[1])
        else:
            resp == 'cmd_unknown'

        if resp is None:
            resp = 'OK'

        return resp

    def loadConfig(self, config_mode: str):
        """Update command list with settings defined in config file.

        Parameters
        ----------
        config_mode : str
            Configuration option listed in config file.

        """
        Hardware = HardwareController(self.hardware_config_file, config_mode)
        self.cmd_dict.update({'reportFracCollectorPositions': Hardware.reportFracCollectorPositions,
                              'moveFracCollector': Hardware.moveFracCollector,
                              'homeFracCollector': Hardware.homeFracCollector,
                              'setInputValves': Hardware.setInputValves,
                              'setWasteValves': Hardware.setWasteValves,
                              'getInputValves': Hardware.getInputValves,
                              'getWasteValves': Hardware.getWasteValves,
                              'reportRotaryPorts': Hardware.reportRotaryPorts,
                              'getCurrentPort': Hardware.getCurrentPort,
                              'renameRotaryPort': Hardware.renameRotaryPort,
                              'moveRotaryValve': Hardware.moveRotaryValve,
                              'homeRotaryValve': Hardware.homeRotaryValve,
                              'getPumpStatus': Hardware.getPumpStatus,
                              'getFlowRate': Hardware.getFlowRate,
                              'setFlowRate': Hardware.setFlowRate,
                              'startPumping': Hardware.startPumping,
                              'stopPumping': Hardware.stopPumping,
                              'getFractionDuration': Hardware.getFractionDuration,
                              })

    def receiveData(self):
        """Temporarily wait for data in receive buffer and split it."""
        data_waiting = self.socket_data_in.poll(timeout=self.timeout_recv * 1000)
        if data_waiting:
            data = self.socket_data_in.recv_string().split(',')
            logging.debug('Received data: '.join(data))
            return data

    def sendData(self, data):
        """Transmit data with device ID prefix.

        Parameters
        ----------
        data
            A python object to be transmitted.
        """
        self.socket_data_out.send_pyobj([self._device_id, data])
        logging.debug('Transmitting data: %s', str(data))

    def signalAvailability(self):
        """Put data on 'availability' socket if device not in use."""
        if self._device_id is None:
            self.socket_availability.send_string('')
            logging.debug('Signalled availability.')
