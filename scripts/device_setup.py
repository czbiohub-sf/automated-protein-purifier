#!/usr/bin/env python
import logging
import socket
from czpurifier.middleware import DeviceInterface

current_address = socket.gethostbyname(socket.getfqdn() + '.local')
logging.basicConfig(level=logging.INFO)
di = DeviceInterface(ip_address=current_address)
di.autorun()
