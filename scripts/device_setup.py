#!/usr/bin/env python
import logging
import socket
from czpurifier.middleware import DeviceInterface

current_address = socket.gethostbyname(socket.getfqdn() + '.local')
logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
di = DeviceInterface(ip_address=current_address)
di.autorun()
