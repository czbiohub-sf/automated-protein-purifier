# Instrument setup (do not change)
#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Define columns (type and number)
ui = UICommands()
ui.connect('5mL', 'pure2.local', 4)

# Purge bubbles from lines

ui.selectBuffers()
#ui.selectPort('BASE')
#ui.pump(1)

ui.closePreColumnWaste()
ui.selectPort('LOAD_BUFFER')
ui.pump(1)

#ui.selectPort('ELUTION')
#ui.pump(1)


# Run purification protocol
ui.closePostColumnWaste()

#ui.selectFraction('Flow1')
#ui.pump(10)

#ui.selectPort('BASE')
#ui.selectFraction('Flow2')
#ui.pump(10)

ui.selectFraction('Flow3')
ui.pump(10)

ui.selectFraction('Safe')


