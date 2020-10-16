# Instrument setup (do not change)
#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('1mL', 'pure2.local', 4)

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

# Run purification protocol
ui.selectPort('LOAD_BUFFER')
ui.pump(10)
ui.closePostColumnWaste()

ui.selectFraction('Flow1')
ui.pump(1)

ui.openPostColumnWaste()
ui.selectFraction('Safe')


