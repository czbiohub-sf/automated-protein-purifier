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
#ui.pump(.5)
ui.closePreColumnWaste()
#ui.pump(.5)
ui.closePostColumnWaste()
ui.selectFraction("Flow4")
ui.pump(2)
