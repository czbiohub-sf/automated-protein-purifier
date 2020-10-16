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
ui.connect('5mL', 'pure2.local', 4,[25/18.20,25/20.94,25/21.23,25/20.54])

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
for i in range(2):
#    logging.info('Run Number: {}'.format(i+1))
    ui.selectLoad()
    ui.selectFraction('Flow1')
    ui.pump(5)
    ui.selectFraction('Flow2')
    ui.pump(5)
    ui.selectFraction('Flow3')
    ui.pump(5)
    ui.selectFraction('Flow4')
    ui.pump(5)
    ui.selectFraction('Safe')
    ui.openPostColumnWaste()
    ui.pump(5)
    ui.closePostColumnWaste()
    #To wait between runs uncomment next line and adjust time
    #sleep(4)

# Run purification protocol: WASH
for i in range(2):
#    logging.info('Run Number: {2}'.format(i+1))
    ui.selectBuffers()
    ui.selectPort('WASH')
    ui.selectFraction('Flow1')
    ui.pump(5)
    ui.selectFraction('Flow2')
    ui.pump(5)
    ui.selectFraction('Flow3')
    ui.pump(5)
    ui.selectFraction('Flow4')
    ui.pump(5)
    ui.selectFraction('Safe')
    ui.openPostColumnWaste()
    ui.pump(5)
    ui.closePostColumnWaste()

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
ui.selectFraction('Safe')
ui.openPostColumnWaste()

# Run cleanup
ui.selectPort('BASE')
ui.pump(10)
ui.selectPort('LOAD_BUFFER')
ui.pump(10)

