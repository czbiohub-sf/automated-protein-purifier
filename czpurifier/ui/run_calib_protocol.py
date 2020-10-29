import logging
from time import sleep
from signal import SIGUSR1
from os import kill
from command_wrappers import UICommands

class RunCalibrationProtocol():
    def __init__(self, columnsize, caliblist, ip, gui_pid):
        """
        columnsize: '1mL' or '5mL'
        ip: 'pure2.local'
        gui_pid: The pid used to signal when process is completed
        """

        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        self.ui = UICommands()
        self.ui.connect(columnsize, ip, 4, caliblist)
        
        pump_time = 10 if columnsize == '1mL' else 5
        self.run_calib(pump_time)
    
        kill(gui_pid, SIGUSR1)

    def run_calib(self, pump_time):
        """
        First purge bubbles from the line
        Run the pump for 10mins for 1mL col size, and for 5mins for 5mL col size
        """
        # Purge bubbles from lines
        self.ui.openPreColumnWaste()
        self.ui.selectLoad()
        self.ui.pump(1)
        self.ui.closePreColumnWaste()
        
        self.ui.openPostColumnWaste
        self.ui.selectLoad()
        self.ui.pump(1)
        self.ui.closePostColumnWaste()
        
        self.ui.selectLoad()
        self.ui.selectFraction('Flow1')
        self.ui.pump(pump_time)

        self.ui.openPostColumnWaste()
        self.ui.selectFraction('Safe')