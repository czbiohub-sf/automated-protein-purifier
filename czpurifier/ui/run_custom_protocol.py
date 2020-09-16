import logging
from time import sleep
from signal import SIGUSR1, SIGUSR2
from os import kill
from command_wrappers import UICommands

class RunCustomProtol():
    def __init__(self, input_param, fractions, ip, gui_pid):
        """[[4, 1, 10],[None, 200, 0],[2, 100, 1],....]"""

        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        # Setup
        input_param[0][1] = '1mL' if input_param[0][1] == 1 else '5mL'
        self.ui = UICommands()
        self.ui.connect(input_param[0][1], ip, input_param[0][0])

        self.buffers = ['WASH', 'LOAD_BUFFER', 'ELUTION', 'BASE']
        self.waste_close_cmds = [self.ui.closePreColumnWaste, self.ui.closePostColumnWaste]
        self.waste_open_cmds = [self.ui.openPreColumnWaste, self.ui.openPostColumnWaste]

        self._purge_bubbles()
        #kill(gui_pid, SIGUSR1)
        self._run_process(input_param[1:], input_param[0][2])
        logging.info('Purification Complete')
        #kill(gui_pid, SIGUSR2)
        self._run_cleanup()

    def _purge_bubbles(self):
        # Purge bubbles from lines
        self.ui.selectLoad()
        self.ui.pump(1)
        self.ui.selectBuffers()
        self.ui.selectPort('BASE')
        self.ui.pump(1)
        self.ui.selectPort('ELUTION')
        self.ui.pump(1)
        self.ui.selectPort('WASH')
        self.ui.pump(1)
        self.ui.selectPort('LOAD_BUFFER')
        self.ui.pump(1)
        self.ui.closePreColumnWaste()

    def _run_process(self, input_params, rep):
        """Runs the process rep times"""
        for _ in rep:
            for step in input_params:
                _run_step(step)
        
    def _run_step(self, step_param):
        """Runs the process for each step"""
        # 1. Select either buffer or load
        #  If buffer select the port
        if step_param[0] is None:
            self.ui.selectLoad()
        else:
            self.ui.selectBuffers()
            self.ui.selectPort(self.buffers[step_param[0]])
        
        # 2. If fraction/flow, run the stage
        # If waste: open waste, run pump, close waste
        if step[2] > 1:
            self._run_frac_collector()
        else:
            self.waste_open_cmds[step[2]]
            self.ui.pump(step[1])
            self.waste_close_cmds[step[2]]
    
    def _run_frac_collector(self):
        """TODO: Implement run fraction collector"""
        pass

    def _run_cleanup(self):
        # Run cleanup
        ui.selectPort('BASE')
        ui.pump(10)
        ui.selectPort('LOAD_BUFFER')
        ui.pump(10)