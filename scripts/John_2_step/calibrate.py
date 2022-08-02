# Instrument setup (do not change)
#!/usr/bin/env python

import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('1mL', 'pure1.local', 2,[10/10,7/1])

# Purge bubbles
ui.selectLoad()
ui.pump(1,[0,1])
ui.closePreColumnWaste()


ui.closePostColumnWaste()
ui.selectFraction('Flow1')
ui.pump(5,[0,1])

ui.selectFraction('Safe')


