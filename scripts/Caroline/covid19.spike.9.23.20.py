# Instrument setup (do not change)
#!/usr/bin/env python

import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('5mL', 'pure2.local', 4,[50/41.16,50/40.88,50/42.40,50/40.41])

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


#LOAD
ui.selectPort('LOAD_BUFFER')
ui.pump(15)
ui.closePostColumnWaste()

# Run purification protocol: LOAD
ui.selectLoad()
ui.selectFraction('Flow1')
ui.pump(10)
ui.selectFraction('Flow2')
ui.pump(10)
ui.selectFraction('Flow3')
ui.pump(10)
ui.selectFraction('Flow4')
ui.pump(10)

# Run purification protocol: WASH
ui.selectBuffers()
ui.selectPort('WASH')
ui.openPostColumnWaste()
ui.pump(60)
ui.closePostColumnWaste()

# Run purification protocol: ELUTION
ui.selectPort('ELUTION')
ui.selectFraction('Frac1')
ui.pump(1)
ui.selectFraction('Frac2')
ui.pump(1)
ui.selectFraction('Frac3')
ui.pump(1)
ui.selectFraction('Frac4')
ui.pump(1)
ui.selectFraction('Frac5')
ui.pump(1)
ui.selectFraction('Frac6')
ui.pump(1)
ui.selectFraction('Frac7')
ui.pump(1)
ui.selectFraction('Frac8')
ui.pump(1)
ui.selectFraction('Frac9')
ui.pump(1)
ui.selectFraction('Frac10')
ui.pump(1)
ui.selectFraction('Safe')
#ui.openPostColumnWaste()

# Run cleanup
#ui.selectPort('BASE')
#ui.pump(5)
#ui.selectPort('LOAD_BUFFER')
#ui.pump(10)

