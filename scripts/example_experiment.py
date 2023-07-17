#!/Users/samia.sama/Documents/Protein_Purifier/venv/bin/python3.7
import logging
from logging.config import fileConfig
from czpurifier.ui import UICommands


fileConfig(fname="/home/pi/ProteinPurifier/config/logger_client.config", disable_existing_loggers=False)
logger = logging.root

# Setup
ui = UICommands()

# Use 1mL columns, machine IP address, 4 channels, and no flow rate correction
ui.connect('1mL', 'pure1.local', 4, correction=[1,1,1,1])

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
ui.pump(10)  # Exchange buffer in column
ui.selectLoad()
ui.pump(45)  # Load sample onto column
ui.selectBuffers()
ui.selectPort('WASH')
ui.pump(40)  # Wash column
ui.selectPort('ELUTION')
ui.closePreColumnWaste()
ui.pump(2)  # Purge buffer in line above column
ui.openPreColumnWaste()
ui.selectFraction('Frac1')
ui.pump(1)  # Elute
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
ui.openPostColumnWaste()
ui.selectFraction('Safe')

# Run cleanup
ui.selectPort('BASE')
ui.pump(10)