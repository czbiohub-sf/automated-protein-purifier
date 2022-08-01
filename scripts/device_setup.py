#!/usr/bin/env python
import logging
import socket
from czpurifier.middleware import DeviceInterface

logging.basicConfig(filename='/home/pi/ProteinPurifier/purifier.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s [%(name)s]', level=logging.INFO, datefmt='%H:%M:%S')

logging.info("Beginning purifier port configuration.")
current_address = socket.gethostbyname(socket.getfqdn() + '.local')
di = DeviceInterface(ip_address=current_address)
logging.info("Purifier server awaiting connections.")
di.autorun()
