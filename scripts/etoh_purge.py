#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands


logging.basicConfig(level=logging.INFO)

# Setup
ui = UICommands()
ui.connect('1mL', 'pure1', 1)

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)
ui.selectBuffers()
ui.selectPort('LOAD_BUFFER')
ui.pump(1)
sleep(30)

ui.selectPort('WASH')
ui.pump(1)
ui.selectPort('ELUTION')
ui.pump(1)
sleep(30)

ui.selectPort('BASE')
ui.pump(1)
ui.closePreColumnWaste()
ui.pump(10)
