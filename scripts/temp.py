#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Setup
ui = UICommands()
ui.connect('5mL', 'pure1.local', 3)

# Purge bubbles from lines
ui.selectBuffers()
ui.closePreColumnWaste()

# Run base wash
ui.selectLoad()
ui.selectBuffers()
ui.selectPort('BASE')
ui.selectPort('ELUTION')
ui.selectPort('WASH')
ui.selectPort('LOAD_BUFFER')

