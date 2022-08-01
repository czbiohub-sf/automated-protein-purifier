import logging
from time import sleep
from czpurifier.ui import UICommands

logging.basicConfig(filename='/home/pi/ProteinPurifier/purifier_client.log', filemode='a', format='%(asctime)s %(levelname)s: %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')

#Setup connection
ui = UICommands()
ci = ui.ci  # controller interface for precise peripheral control
ui.connect('1mL','pure1.local')

logging.warn('Beginning input valve evaluation. SOLENOIDS NOT CONNECTED!')
for j in range(2000):
    ui.selectBuffers()
    ui.selectLoad()

logging.warn('Beginning waste valve evaluation. SOLENOIDS NOT CONNECTED!')
for j in range(1000):
    ui.openPreColumnWaste()
    ui.openPostColumnWaste()
    ui.closePreColumnWaste()
    ui.closePostColumnWaste()
    ui.openAllWaste()
    ui.closeAllWaste()

#Evaluate pumps independently starting with pump closest to Pi
logging.warn('Beginning pump evaluation. Cycling pumps in order of proximity to Pi.')
for i in [3,2,1,0]:
    logging.warn('Pump #%s',str(i))
    for j in range(1000):
        ci.startPumping(i)
        sleep(4)
        ci.stopPumping()
        sleep(1)

logging.warn('Running all 4 pumps simultaenously.')
for j in range(1000):
    ci.startPumping()
    sleep(2)
    ci.stopPumping()
    sleep(2)

logging.warn('Beginning frac collector/rotary valve eval. Alternating to reduce inductive effects and heating rate.')
for j in range(500):
    ui.selectFraction('Frac10')
    ui.selectPort('ELUTION')
    ui.selectFraction('Frac8')
    ui.selectPort('LOAD_BUFFER')

ui.disconnect()

logging.warning('Evaluation complete!')