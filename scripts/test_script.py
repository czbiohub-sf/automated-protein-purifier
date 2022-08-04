#!/usr/bin/env python
import logging
from logging.config import fileConfig
from czpurifier.ui import UICommands

fileConfig(fname="/home/pi/ProteinPurifier/scripts/logger_client.config", disable_existing_loggers=False)
logger = logging.root

#logging.basicConfig(filename='/home/pi/ProteinPurifier/purifier_client.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')

# Setup
ui = UICommands()
ui.connect('1mL', 'pure1.local')

# Purge bubbles from lines
ui.selectLoad()
ui.pump(1)
ui.selectBuffers()
ui.selectPort('BASE')
#ui.pump(1)
ui.selectPort('ELUTION')
#ui.pump(1)
ui.selectPort('WASH')
#ui.pump(1)
ui.selectPort('LOAD_BUFFER')
#ui.pump(1)
ui.closePreColumnWaste()

# Run purification protocol
#ui.pump(1)
ui.selectLoad()
#ui.pump(1)
ui.selectBuffers()
ui.selectPort('WASH')
#ui.pump(1)
ui.selectPort('ELUTION')
ui.selectFraction('Frac1')
#ui.pump(1)
ui.selectFraction('Frac2')
#ui.pump(1)
ui.selectFraction('Frac3')
#ui.pump(1)
ui.selectFraction('Frac4')
#ui.pump(1)
ui.selectFraction('Frac5')
#ui.pump(1)
ui.selectFraction('Frac6')
#ui.pump(1)
ui.selectFraction('Frac7')
#ui.pump(1)
ui.selectFraction('Frac8')
#ui.pump(1)
ui.selectFraction('Frac9')
#ui.pump(1)
ui.selectFraction('Frac10')
#ui.pump(1)
ui.openPostColumnWaste()
ui.selectFraction('Safe')

# Run cleanup
ui.selectPort('BASE')
ui.pump(1)

ui.disconnect()