#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Setup
ui = UICommands()
ui.connect('5mL', 'pure1.local', 2)

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)
ui.selectBuffers()
ui.selectPort('ELUTION')
ui.pump(1)
ui.selectPort('WASH')
ui.pump(1)
ui.selectPort('LOAD_BUFFER')
ui.pump(1)
ui.closePreColumnWaste()

# Run purification protocol
#ui.selectPort('BASE')
#ui.pump(5)
ui.selectPort('LOAD_BUFFER')
ui.pump(15)

ui.selectLoad()
ui.pump(220)

ui.selectBuffers()
ui.selectPort('WASH')
ui.pump(70)
ui.closePostColumnWaste()
ui.selectPort('ELUTION')
ui.selectFraction('Flow1')
ui.pump(10)
ui.selectFraction('Safe')

# Run cleanup
#ui.selectPort('BASE')
#ui.pump(10)
#ui.selectPort('LOAD_BUFFER')
#ui.pump(10)
