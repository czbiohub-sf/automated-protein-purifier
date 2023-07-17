#!/usr/bin/env python

# DO NOT DELETE!
# USED TO RUN THE PURIFIER SOFTWARE AS A SERVICE

import logging
from logging.config import fileConfig
import socket
from czpurifier.middleware import DeviceInterface


fileConfig(fname="/home/pi/ProteinPurifier/config/logger_server.config", disable_existing_loggers=False)
logger = logging.root

logging.info("Beginning purifier port configuration.")
current_address = socket.gethostbyname(socket.getfqdn() + '.local')
di = DeviceInterface(ip_address=current_address)
logging.info("Purifier server awaiting connections.")
di.autorun()
