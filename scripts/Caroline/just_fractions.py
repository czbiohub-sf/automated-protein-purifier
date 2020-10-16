# Instrument setup (do not change)
#!/usr/bin/env python

import logging
from time import sleep
from czpurifier.ui import UICommands
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# Asks user for the number of times to run and makes sure that the input is valid
#run_times = input('Please type the number of times to run protocol and hit enter: ')
#while True:
#    try:
#        run = int(run_times)
#        run = abs(run)
#        break
#    except ValueError:
#        run_times = input('Invalid input, please try again: ')

# Define columns (type and number)
ui = UICommands()
ui.connect('5mL', 'pure2.local', 4,[25/20.35,25/22.09,25/21.60,25/21.80])
ui.closePreColumnWaste()
ui.closePostColumnWaste()
# Purge bubbles from lines
ui.selectBuffers()
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

# Run cleanup

