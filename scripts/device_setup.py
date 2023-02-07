#!/usr/bin/env python
import logging
from logging.config import fileConfig
import socket
from czpurifier.middleware import DeviceInterface

fileConfig(fname="/home/pi/ProteinPurifier/config/logger_server.config", disable_existing_loggers=False)
logger = logging.root
#logging.basicConfig(filename='/home/pi/ProteinPurifier/purifier.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s [%(name)s]', level=logging.INFO, datefmt='%H:%M:%S')

logging.info("Beginning purifier port configuration.")
current_address = socket.gethostbyname(socket.getfqdn() + '.local')
di = DeviceInterface(ip_address=current_address)
logging.info("Purifier server awaiting connections.")
di.autorun()
