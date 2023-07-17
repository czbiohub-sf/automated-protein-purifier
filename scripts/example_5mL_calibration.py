#!/usr/bin/env python
import logging
from logging.config import fileConfig
from time import sleep
from czpurifier.ui import UICommands

fileConfig(fname="/home/pi/ProteinPurifier/config/logger_client.config", disable_existing_loggers=False)
logger = logging.root

# Setup
ui = UICommands()
ui.connect('5mL', 'pure1.local', 2)  # Only calibrating 2 channels

# Purge bubbles from lines
ui.selectBuffers()
ui.selectPort('WASH')
ui.pump(2)
ui.closePreColumnWaste()
ui.closePostColumnWaste()  
ui.selectFraction("Flow1")  # Dispense 25 mL into Flow1
ui.pump(5)
ui.selectFraction("Flow2")  # Dispense 5 mL into Flow2 (calibration sample)
ui.pump(1)
