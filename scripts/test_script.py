#!/Users/samia.sama/Documents/Protein_Purifier/venv/bin/python3.7
import logging
from czpurifier.ui import UICommands

logging.basicConfig(level=logging.INFO)

# Setup
ui = UICommands()
ui.connect('1mL', '127.0.0.1')

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
ui.pump(10)
ui.selectLoad()
ui.pump(45)
ui.selectBuffers()
ui.selectPort('WASH')
ui.pump(40)
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
ui.openPostColumnWaste()
ui.selectFraction('Safe')

# Run cleanup
ui.selectPort('BASE')
ui.pump(10)