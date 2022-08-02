# Instrument setup (do not change)
#!/usr/bin/env python
import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')# Define columns (type and number)
ui = UICommands()
ui.connect('1mL', 'pure1.local', 2,[10/10,7/1])# Purge bubbles
ui.selectLoad()
ui.pump(1,[0])
ui.selectBuffers()
ui.selectPort('ELUTION')
ui.pump(1,[0])# note: in future will use a separate buffer 'DESALT_BUFFER' for Column 2
ui.selectPort('LOAD_BUFFER')
ui.pump(1,[0])
ui.selectPort('BASE')
ui.pump(1,[1])
ui.closePreColumnWaste()# prepare to flush tubing connecting Col1 and Col2 with Elution buffer
ui.selectPort('ELUTION')
ui.pump(1,[0])
ui.serialFlowTo2ndColumn(True)
ui.serialOpen2ndPreColumnWaste()
ui.pump(1,[0])
ui.serialFlowTo2ndColumn(False)
ui.closePreColumnWaste()# equilibrate Col 1 and Col2 in Load_buffer. Will have separate Desalt_buffer in future
ui.selectPort('LOAD_BUFFER')
ui.pump(1,[0])
ui.selectPort('BASE')
ui.pump(1,[1])
# Run purification protocol: LOAD Col 1
ui.selectLoad()
ui.pump(1,[0])# Run purification protocol: WASH
ui.selectBuffers()
ui.selectPort('LOAD_BUFFER')
ui.pump(1,[0])
ui.closePostColumnWaste()# Run purification protocol: ELUTION 1st fraction
ui.selectPort('ELUTION')
ui.selectFraction('Frac1')
ui.pump(1,[0])# Fractions 2-4 sent to Col 2
ui.serialFlowTo2ndColumn(True)
ui.selectFraction('Flow1')
ui.pump(1,[0])
ui.serialFlowTo2ndColumn(False)
# Elute from desalt column
ui.selectPort('BASE')
ui.selectFraction('Flow2')
ui.pump(0.8,[1])
ui.selectFraction('Safe')
