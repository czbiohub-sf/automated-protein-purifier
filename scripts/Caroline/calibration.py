# Instrument setup (do not change)
#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('5mL', 'pure2.local', 4)

#Calibration
#ui.connect('1mL', 'pure1.local', 4,[10/9.02,10/9.29,10/8.75,10/9.53])

#ui.connect('1mL', 'pure1.local', 4,[10/8.54,10/9.81,10/10.12,10/9.34])

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)

ui.closePreColumnWaste()
ui.selectLoad()
ui.pump(1)

ui.closePostColumnWaste()
ui.selectLoad()
ui.selectFraction('Flow1')
ui.pump(10)

ui.openPostColumnWaste()
ui.selectFraction('Safe')


