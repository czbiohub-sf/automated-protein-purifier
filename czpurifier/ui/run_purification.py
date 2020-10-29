import logging
from time import sleep
from signal import SIGUSR1
from os import kill
from command_wrappers import UICommands

class RunPurification():
    def __init__(self, input_param, fractions, buffer_calib, ip, gui_pid):
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        # Setup
        self.ui = UICommands()
        self.ui.connect(input_param[1], ip, input_param[0])
        self.buffer_calib = buffer_calib
        self.num_pumps = input_param[0]

        self.waste_close_cmds = [self.ui.closePreColumnWaste, self.ui.closePostColumnWaste]
        self.waste_open_cmds = [self.ui.openPreColumnWaste, self.ui.openPostColumnWaste]

        self._purge_bubbles()
        kill(gui_pid, SIGUSR1)
        self._run_process('EQUILIBRATE', [input_param[2], input_param[3]], fractions[0])
        kill(gui_pid, SIGUSR1)
        self._run_process('LOAD', [input_param[4], input_param[5]], fractions[1])
        kill(gui_pid, SIGUSR1)
        self._run_process('WASH', [input_param[6], input_param[7]], fractions[2])
        kill(gui_pid, SIGUSR1)
        self._run_process('ELUTION', [input_param[8], input_param[9]], fractions[3])
        kill(gui_pid, SIGUSR1)
        logging.info('Purification Complete')
        self._run_cleanup()
        kill(gui_pid, SIGUSR1)

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

    def _run_process(self, process_name, parameters, fraction_param):
        """
        Run Equilibrate, Load, Wash and Elution
        1. Select the right port based on the process name (either buffer or load)
        2. If waste: 
            - Open the desired waste
            - Pump for the input volume
            - Close the opened waste
        Input Parameters
        ----------------------------
        process_name = 'EQUILIBRATE'/'LOAD'/'WASH'/'ELUTION'
        parameters = [total_vol, flow_path]
        fraction_param = []*10 or []*4 or None. Each index contains the volume to fraction 
        """
        if process_name == 'LOAD':
            # Load line does not need calibration
            self.ui.selectLoad()
            # correction still called to reset the flow rate to 1, incase prev step reqs a different factor
            self.ui.flowRateCorrection([1]*self.num_pumps)
        else:
            p_name = process_name if process_name == 'WASH' or process_name == 'ELUTION' else 'LOAD_BUFFER'
            self.ui.selectBuffers()
            self.ui.selectPort(p_name)
            # get the num of active pumps and the flowRateCorrection() needs a list of the correction factor
            # calling this everytime even if the factor is 1 because if the rate is changed it needs
            # to be reset for the next buffer
            correction_factor = [self.buffer_calib[p_name]]*self.num_pumps
            self.ui.flowRateCorrection(correction_factor)

        if parameters[1] == 2:
            self._run_fraction_col(fraction_param)
        else:
            # Open the waste 
            # pump out the vol 
            # close the waste
            self.waste_open_cmds[parameters[1]]()
            self.ui.pump(parameters[0])
            self.waste_close_cmds[parameters[1]]()
        
    def _run_fraction_col(self, fraction_param):
        """
        Runs each pump for the volume specified by the fraction_param index
        If len(fraction_param) is 4 use the flow through columns, otherwise
        use the 1ml/5ml fraction collector columns
        """
        col_type = 'Frac' if len(fraction_param) > 4 else 'Flow'
        for i in range(len(fraction_param)):
            if fraction_param[i] != 0:
                self.ui.selectFraction('{0}{1}'.format(col_type, i+1))
                skip_pressed = self.ui.pump(fraction_param[i])
                if skip_pressed:
                    break
        self.ui.selectFraction('Safe')

    def _run_cleanup(self):
        # Run cleanup
        self.ui.openPostColumnWaste()
        self.ui.selectPort('BASE')
        self.ui.pump(10)
        self.ui.selectPort('LOAD_BUFFER')
        self.ui.pump(10)
        self.ui.closePostColumnWaste()

if __name__ == "__main__":
    run = RunPurification([2, 5, 5, 1, 4, 1, 5, 1], '127.0.0.1')