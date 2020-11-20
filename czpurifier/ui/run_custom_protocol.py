import logging
from time import sleep
from signal import SIGUSR1
from os import kill
from command_wrappers import UICommands

class RunCustomProtocol():
    def __init__(self, input_param, calib_list, fractions, buffer_calib, ip, gui_pid):
        """input_param = [[4, '1mL', 1], [2, 6, 0], [None, 1, 0], [2, 12, 2]]
        input_param[0] = [num_columns, column_size, num_repeats]
        input_param[1:] = [none:load 0/1/2/3: buffer, volume, flow_path]"""
        
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        # Setup
        self.gui_pid = gui_pid
        self.ui = UICommands()
        self.ui.connect(input_param[0][1], ip, input_param[0][0], calib_list)

        self.buffers = ['WASH', 'LOAD_BUFFER', 'ELUTION', 'BASE']
        self.waste_close_cmds = [self.ui.closePreColumnWaste, self.ui.closePostColumnWaste]
        self.waste_open_cmds = [self.ui.openPreColumnWaste, self.ui.openPostColumnWaste]
        self.buffer_calib = buffer_calib
        self.per_column_calib = calib_list
        self.num_pumps = input_param[0][0]

        self._purge_bubbles()
        kill(gui_pid, SIGUSR1)
        self._run_process(input_param[1:], fractions, input_param[0][2])
        self._run_cleanup()
        logging.info('Purification Complete')
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

    def _run_process(self, input_params, fractions, rep):
        """Runs the process rep times"""
        for i in range(rep):
            for step, f in zip(input_params, fractions):
                self._run_step(step, f)
                kill(self.gui_pid, SIGUSR1)
        
    def _run_step(self, step_param, frac):
        """Runs the process for each step"""
        # 1. Select either buffer or load
        #  If buffer select the port
        if step_param[0] is None:
            self.ui.selectLoad()
            # correction called to reset back to the original per column calibration
            # per column calibration is done using the LOAD
            self.ui.flowRateCorrection(self.per_column_calib)
        else:
            self.ui.selectBuffers()
            p_name = self.buffers[step_param[0]]
            self.ui.selectPort(p_name)
            # multiply the buffer calibration factor with the per column calibration factor
            # to set the new flow rate to incorporate both calibration rates
            correction_factor = [i*self.buffer_calib[p_name] for i in self.per_column_calib]
            self.ui.flowRateCorrection(correction_factor)
        
        # 2. If fraction/flow, run the stage
        # If waste: open waste, run pump, close waste
        if step_param[2] > 1:
            self._run_frac_collector(frac)
        else:
            self.waste_open_cmds[step_param[2]]
            self.ui.pump(step_param[1])
            self.waste_close_cmds[step_param[2]]
    
    def _run_frac_collector(self, fraction_param):
        col_type = 'Frac' if len(fraction_param) > 4 else 'Flow'
        for i in range(len(fraction_param)):
            if fraction_param[i] != 0:
                self.ui.selectFraction('{0}{1}'.format(col_type, i+1))
                self.ui.pump(fraction_param[i])
        self.ui.selectFraction('Safe')

    def _run_cleanup(self):
        # Run cleanup
        self.ui.openPostColumnWaste()
        self.ui.selectPort('BASE')
        self.ui.pump(10)
        self.ui.selectPort('LOAD_BUFFER')
        self.ui.pump(10)
        self.ui.closePostColumnWaste()