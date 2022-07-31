#!/usr/bin/env python
import logging
import socket
from czpurifier.middleware import DeviceInterface

logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')
logging.info("Beginning purifier server setup.")
current_address = socket.gethostbyname(socket.getfqdn() + '.local')
di = DeviceInterface(ip_address=current_address)
logging.debug("Beginning autorun.")
di.autorun()
