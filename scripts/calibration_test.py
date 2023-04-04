#!/usr/bin/env python
import logging
from czpurifier.ui import UICommands

logging.basicConfig(level=logging.INFO)

# Setup
ui = UICommands()
ui.connect('1mL', 'pure1.local', 2)

# Purge bubbles from lines
ui.pump(1)
ui.closePreColumnWaste()
ui.pump(1)
ui.closePostColumnWaste()

ui.selectFraction("Frac1")
ui.pump(1)
ui.selectFraction("Flow1")
ui.pump(5)

ui.selectFraction("Safe")
ui.disconnect()
