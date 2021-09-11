# Instrument setup (do not change)
#!/usr/bin/env python

import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('1mL', 'pure1.local', 4,[40/35.4,40/34.3,40/32.3,40/32])

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)
ui.selectBuffers()
#ui.selectPort('BASE')
#ui.pump(1)
ui.selectPort('ELUTION')
ui.pump(1)
ui.selectPort('WASH')
ui.pump(1)
ui.selectPort('LOAD_BUFFER')
ui.pump(1)
ui.closePreColumnWaste()


#LOAD
ui.selectPort('LOAD_BUFFER')
ui.pump(15)
#ui.closePostColumnWaste()

# Run purification protocol: LOAD 1 Liter
ui.selectLoad()
ui.pump(200)

# Run purification protocol: WASH
ui.selectBuffers()
ui.selectPort('WASH')
ui.pump(60)
ui.closePostColumnWaste()

# Run purification protocol: ELUTION
ui.selectPort('ELUTION')
ui.selectFraction('Flow1')
ui.pump(8)
ui.selectFraction('Safe')
#ui.openPostColumnWaste()

# Run cleanup
#ui.selectPort('BASE')
#ui.pump(5)
#ui.selectPort('LOAD_BUFFER')
#ui.pump(10)

