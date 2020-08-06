#!/usr/bin/env python
import logging
from czpurifier.ui import UICommands

logging.basicConfig(level=logging.INFO)

# Setup
ui = UICommands()
ui.connect('5mL', 'pure2.local', 4)

# Purge bubbles from lines
ui.pump(1)
ui.closePreColumnWaste()
ui.pump(1)
ui.closePostColumnWaste()

ui.selectFraction("Frac1")
ui.pump(1)
ui.selectFraction("Frac2")
ui.pump(1)
ui.selectFraction("Frac3")
ui.pump(1)

ui.selectFraction("Safe")
ui.disconnect()
