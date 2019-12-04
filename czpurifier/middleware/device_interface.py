"""Protein purifier device communication and execution script."""
import time
import zmq
from pkg_resources import Requirement, resource_filename
from ..hardware_controller.hardware_setup import HardwareController


def executeDevice(input, cmd_dict):
    """Break input string into command and argument and execute command."""

    split_input = input.split(',')
    cmd = split_input[0]
#    cmd, init_arg = input.split(',')
    args = split_input[1:]
    num_args = len(args)
    arg = []

    for i in range(num_args):
        if i != '':
            try:
                arg.append(int(args[i]))

            except ValueError:
                arg.append(args[i])
        else:
            num_args = 0

    if cmd in cmd_dict and num_args == 0:
        resp = cmd_dict[cmd]

    elif cmd in cmd_dict and num_args == 1:
        resp = cmd_dict[cmd](arg[0])

    elif cmd in cmd_dict and num_args == 2:
        resp = cmd_dict[cmd](arg[0], arg[1])

    if resp is None:
        resp = 'OK'

    elif cmd == 'disconnect':
        resp = cmd

    else:
        resp == 'cmd_unknown'

    return resp


if __name__ == '__main__':

    context = zmq.Context()
    socket_availability = context.socket(zmq.PUSH)
    socket_availability.bind("tcp://localhost:5000")
    socket_data_in = context.socket(zmq.PULL)
    socket_data_in.bind("tcp://localhost:5100")
    socket_data_out = context.socket(zmq.PUSH)
    socket_data_out.bind("tcp://localhost:5200")

    hardware_file = resource_filename(Requirement.parse("czpurifier"), "autopurifier_hardware.config")
    Hardware = []

    while True:
        t_last_contact = 0
        device_id = None
        data_in = ''
        socket_availability.send_string('')  # device availability heartbeat
        data_waiting = socket_data_in.poll(timeout=1000)

        if data_waiting:
            data_in = socket_data_in.recv_string().split(',')

        if data_in[0] == 'load_config':
            try:
                Hardware = HardwareController(hardware_file, data_in[1])
                cmd_dict = {'reportFracCollectorPositions': Hardware.reportFracCollectorPositions,
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
                            }
                t_last_contact = time.monotonic()
            finally:
                socket_data_out.send_pyobj('')  # Error reporting goes here

        elif data_in[0] == 'connect':
            device_id = data_in[1]
            t_last_contact = time.monotonic()

        while (time.monotonic() - t_last_contact < 10):  # timeout after 10s
            data_waiting = socket_data_in.poll(timeout=50)

            if data_waiting:
                input = socket_data_in.recv_string()
                resp = executeInput(input, cmd_dict)
                t_last_contact = time.monotonic()
                socket_data_out.send_pyobj([device_id, resp])
                if resp == 'disconnect':
                    break


    # Psuedocode
    #
    # r = ''
    # availability (P5000)
    # p = poll(P5100, 50ms)
    # if p:
    #   r = read(P5100)
    # if r == 'load':
    #   config = read(5100)
    #   hardware = HardwareController(path, config)
    #   t_contact = now
    # elif r == 'reconnect' & hardware not None:
    #   t_contact = now
    # while(now - t_contact < 10):
    #   p = poll(P5100, 50ms)
    #   if p:
    #       cmd = pull(P5100)
    #       parse command and execute
    #       push(P5200)
    #       t_contact = now
    # sleep(1)
