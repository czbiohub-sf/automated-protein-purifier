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
ui.selectBuffers()
ui.selectPort('ELUTION')
ui.pump(1,[0])

# note: in future will use a separate buffer 'DESALT_BUFFER' for Column 2
ui.selectPort('LOAD_BUFFER')
ui.pump(1,[0])
ui.closePreColumnWaste()

ui.selectPort('ELUTION')
ui.pump(7,[0])
ui.selectPort('LOAD_BUFFER')
ui.pump(10,[0])

ui.selectFraction('Safe')


