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
ui.connect('5mL', 'pure2.local', 4,[25/18.08,25/23.58,25/22.37,25/22.06])

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
ui.pump(5)
ui.closePostColumnWaste()

# Run purification protocol: LOAD
for i in range(1):
#    logging.info('Run Number: {1}'.format(i+1))
    ui.selectLoad()
    ui.selectFraction('Flow1')
    ui.pump(5)
    ui.selectFraction('Safe')
    #To wait between runs uncomment next line and adjust time
    #sleep(4)

# Run purification protocol: WASH
for i in range(1):
#    logging.info('Run Number: {1}'.format(i+1))
    ui.selectBuffers()
    ui.selectPort('WASH')
    ui.openPostColumnWaste()
    ui.pump(5)
    ui.closePostColumnWaste()
    ui.selectFraction('Flow2')
    ui.pump(5)
    ui.selectFraction('Safe')

# Run purification protocol: ELUTION
for i in range(1):
#    logging.info('Run Number: {1}'.format(i+1))
    ui.selectBuffers()
    ui.selectPort('ELUTION')
    ui.openPostColumnWaste()
    ui.pump(5)
    ui.closePostColumnWaste()
    ui.selectFraction('Flow3')
    ui.pump(5)
    ui.selectFraction('Safe')

# Run purification protocol: 20% Ethanol
for i in range(1):
#    logging.info('Run Number: {1}'.format(i+1))
    ui.selectBuffers()
    ui.selectPort('BASE')
    ui.openPostColumnWaste()
    ui.pump(5)
    ui.closePostColumnWaste()
    ui.selectFraction('Flow4')
    ui.pump(5)
    ui.selectFraction('Safe')
