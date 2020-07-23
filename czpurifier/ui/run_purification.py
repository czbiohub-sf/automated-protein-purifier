import logging
from time import sleep
from command_wrappers import UICommands

class RunPurification():
    def __init__(self, input_param, ip):
        logging.basicConfig(level=logging.INFO)
        # Setup
        self.input_param = input_param
        self.input_param[1] = '1mL' if self.input_param[1] == 1 else '5mL'
        self.ui = UICommands()
        self.ui.connect(self.input_param[1], ip, self.input_param[0])

        self.waste_close_cmds = [self.ui.closePreColumnWaste, self.ui.closePostColumnWaste]
        self.waste_open_cmds = [self.ui.openPreColumnWaste, self.ui.openPostColumnWaste]

        #self._purge_bubbles()
        self._run_process('EQUILIBRATE', [self.input_param[2], self.input_param[3]])
        #self._run_process('LOAD', [self.input_param[4], self.input_param[5]])
        #self._run_process('WASH', [self.input_param[6], self.input_param[7]])
        #self._run_process('ELUTE', [self.input_param[8], self.input_param[9]])

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

    def _run_process(self, process_name, parameters, fraction_param = None):
        """
        Run Equilibrate, Load, Wash and Elute
        1. Select the right port based on the process name (either buffer or load)
        2. If waste: 
            - Open the desired waste
            - Pump for the input volume
            - Close the opened waste
        Input Parameters
        ----------------------------
        process_name = 'EQUILIBRATE'/'LOAD'/'WASH'/'ELUTE'
        parameters = [total_vol, flow_path]
        fraction_param = []*10 
        """
        if process_name == 'LOAD':
            self.ui.selectLoad()
        elif process_name == 'WASH' or process_name == 'ELUTE':
            self.ui.selectBuffers()
            self.ui.selectPort(process_name)
        if parameters[1] == 2:
            self._run_fraction_col(fraction_param)
        else:
            # Open the waste 
            # pump out the vol 
            # close the waste
            self.waste_open_cmds[parameters[1]]()
            self.ui.pump(parameters[0])
            self.waste_close_cmds[parameters[1]]()

if __name__ == "__main__":
    run = RunPurification([2, 5, 5, 1, 4, 1, 5, 1], '127.0.0.1')