#!/Users/samia.sama/Documents/Protein_Purifier/venv/bin/python
"""Interfaces between communication layer and psuedo hardware (used for testing)"""
import zmq
import logging
from time import sleep
from pkg_resources import Requirement, resource_filename
from czpurifier.hardware import HardwareControllerSimulator
from logging import NullHandler

log = logging.getLogger(__name__)
log.addHandler(NullHandler())


class SimulatorInterface():
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
        self._disconnect = False
        self.timeout_recv = timeout_recv
        self.hardware_config_file = resource_filename(Requirement.parse("czpurifier"), "config/autopurifier_hardware.config")
        print(self.hardware_config_file)
        self.cmd_dict = {}
        self.initCmdDict()
        print("Completed Initialization")

    def autorun(self):
        """Loop > Wait for data and execute. Signal if device is available."""
        # Send signal for 5s that the fake device is up
        # Controller Interface checks to make sure that the device is running
        for _ in range(5):
            sleep(1)
            self.socket_availability.send_pyobj('Transmitting')
        while True:
            #self.signalAvailability()
            data_in = self.receiveData()
            if data_in is not None:
                #print(data_in)
                resp = self.executeCall(data_in)
                self.sendData(resp)
                if self._disconnect:
                    self._device_id = None
                    self._disconnect = False
    
    def initCmdDict(self):
        """Set cmd_dict to initialized state."""
        self.cmd_dict = {'connect': self.connect,
                         'disconnect': self.disconnect,
                         'loadConfig': self.loadConfig,
                         }
    
    def loadConfig(self, config_mode: str):
        """Update command list with settings defined in config file.

        Parameters
        ----------
        config_mode : str
            Configuration option listed in config file.
        """
        Hardware = HardwareControllerSimulator(self.hardware_config_file, config_mode)
        #Hardware = HardwareSimulator(self.hardware_config_file, config_mode)
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
        self._disconnect = True
        self.initCmdDict()

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

        # For each argument, attempt to convert to int or float before string.
        for i in range(num_args):
            if i != '':
                try:
                    arg.append(int(args[i]))

                except ValueError:
                    try:
                        arg.append(float(args[i]))
                    except ValueError:
                        arg.append(args[i])
            else:
                num_args = 0
        if cmd in self.cmd_dict and num_args == 0:
            resp = self.cmd_dict[cmd]()
        elif cmd in self.cmd_dict and num_args == 1:
            resp = self.cmd_dict[cmd](arg[0])
        elif cmd in self.cmd_dict and num_args == 2:
            resp = self.cmd_dict[cmd](arg[0], arg[1])
        else:
            resp = 'cmd_unknown'

        if resp is None:
            resp = 'OK'

        return resp

    def receiveData(self):
        """Temporarily wait for data in receive buffer and split it."""
        data_waiting = self.socket_data_in.poll(timeout=self.timeout_recv * 1000)
        if data_waiting:
            data = self.socket_data_in.recv_string().split(',')
            logging.debug('Received data: ' + str(data))
            return data

    def sendData(self, data):
        """Transmit data with device ID prefix.

        Parameters
        ----------
        data
            A python object to be transmitted.
        """
        self.socket_data_out.send_pyobj([self._device_id, data])
        logging.debug('Transmitted data: %s', str(data))

    def signalAvailability(self):
        """Put data on 'availability' socket if device not in use."""
        if self._device_id is None:
            self.socket_availability.send_string('')
            logging.debug('Signalled availability.')

if __name__ == "__main__":
    #current_address = socket.gethostbyname(socket.getfqdn() + '.local')
    logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
    si = SimulatorInterface()
    si.autorun()