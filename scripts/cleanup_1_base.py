#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Setup
ui = UICommands()
ui.connect('5mL', 'pure1.local', 3)

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)
ui.selectBuffers()
ui.selectPort('BASE')
ui.pump(1)
ui.selectPort('ELUTION')
ui.pump(1)
ui.selectPort('WASH')
ui.pump(1)
ui.selectPort('LOAD_BUFFER')
ui.pump(1)
ui.closePreColumnWaste()

# Run base wash
ui.selectPort('BASE')
ui.pump(10)

