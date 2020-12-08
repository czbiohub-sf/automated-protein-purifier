from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_PurificationWindow
from buffer_parameters import BackEnd_BuffersWindow
from os import chdir, path, getpid, kill
from signal import signal, SIGUSR1
from time import sleep
from math import ceil
from czpurifier.gui.control import GUI_Controller


class BackEnd_Purification(Ui_PurificationWindow):
    def __init__(self, Purification, dev_process, columnsize, percolumncalib):
        """
        Contains the initialization and functionality of the purification tab
        The lists in this class are indexed as such:
        0 - Equilibrate step
        1 - Load step
        3 - Wash step
        4 - Elute step

        Parameters
        ------------------------------------------------
        Purification: The QtWindow that is created to display the purification window
        dev_process: Either a process object, if in simulator mode, or None. Used 
        to ping the simulator process in the controller class
        """
        self.columnsize = columnsize
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.gui_controller.columnsize = 1 if columnsize == '1mL' else 5
        self.percolumncalib = percolumncalib
        signal(SIGUSR1, self.startProgressBar)
        self.Purification = Purification
        super().setupUi(self.Purification)
        self.initEvents()

    def initEvents(self):
        """Initializes all on click actions
        Creates additional class attributes"""
        # Parsed when start is clicked to determine the input parameters for run purification
        # Key: Name of the widget, Value: True = textbox widget, False = combobox widget
        self.input_param = {self.num_col_combo_box: False, self.columnsize: None,
                            self.equil_vol_val: True, self.equil_flowpath: False, 
                            self.load_vol_val: True, self.load_flowpath: False,
                            self.wash_vol_val: True, self.wash_flowpath: False,
                            self.elute_vol_val: True, self.elute_flowpath: False}
        # Useful groups of widgets for easier access
        self.vol_vals = [self.equil_vol_val, self.load_vol_val, self.wash_vol_val, self.elute_vol_val]
        self.vol_sliders = [self.equil_vol_slider, self.load_vol_slider, self.wash_vol_slider, self.elute_vol_slider]
        self.flowpath_combo = [self.equil_flowpath, self.load_flowpath, self.wash_flowpath, self.elute_flowpath]

        self.columnsize_int = 1 if self.columnsize == '1mL' else 5
        # Widget setup and activation on start
        self._set_actionbtn_enable(False, True)
        self.setDefaultParam()
        self.equil_flowpath.activated.connect(lambda: self.onClickFlowPath(0))
        self.load_flowpath.activated.connect(lambda: self.onClickFlowPath(1))
        self.wash_flowpath.activated.connect(lambda: self.onClickFlowPath(2))
        self.elute_flowpath.activated.connect(lambda: self.onClickFlowPath(3))
        self.close_btn.clicked.connect(self.onClickClose)
        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.skip_btn.clicked.connect(self.onClickSkip)
        self.stop_btn.clicked.connect(self.onClickStop)
        self.equil_vol_slider.valueChanged.connect(lambda: self.slider_changed(0))
        self.load_vol_slider.valueChanged.connect(lambda: self.slider_changed(1))
        self.wash_vol_slider.valueChanged.connect(lambda: self.slider_changed(2))
        self.elute_vol_slider.valueChanged.connect(lambda: self.slider_changed(3))
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)

        # Set decimal validators for all text box
        self.equil_vol_val.setValidator(QtGui.QDoubleValidator())
        self.load_vol_val.setValidator(QtGui.QDoubleValidator())
        self.wash_vol_val.setValidator(QtGui.QDoubleValidator())
        self.elute_vol_val.setValidator(QtGui.QDoubleValidator())
        
        # Create all the flowpathway objects on init
        for i in range(4):
            self.gui_controller.flowpathwayClicked(i, 1)
        
        # Timers initialized
        # Timer for updating the current status
        self.protocol_step = 0
        self.status_timer = QtCore.QTimer()
        self.status_timer.timeout.connect(self.status_timer_handler)
        self.progressBar.setValue(0)
        self.pbar_timer = QtCore.QTimer()
        self.pbar_timer.timeout.connect(self.progress_bar_handler)

        # Logger initialized to display the steps
        self.log_update_timer = QtCore.QTimer()
        self.log_update_timer.timeout.connect(self.log_timer_handler)
        self.log_update_timer.start(2000)
        self.log_output_txtbox.setReadOnly(True)
        self.log_output = None

        #Timer for a delay between on start window pop up and checking result
        self.check_is_sure_timer = QtCore.QTimer()
        self.check_is_sure_timer.timeout.connect(self.check_is_sure_timer_handler)

        #Timer to track the total time remaining
        self.total_time_timer = QtCore.QTimer()
        self.total_time_timer.timeout.connect(self.total_time_handler)

        self.fraction_collector_window_on = True

    def setDefaultParam(self):
        """Sets the default input parameters that are on the json file"""
        self.num_col_combo_box.setCurrentIndex(self.gui_controller.default_param[0]-1)
        self.elute_vol_slider.setMaximum(10)
        self.equil_vol_val.setText(str(self.gui_controller.default_param[1]))
        self.load_vol_val.setText(str(self.gui_controller.default_param[2]))
        self.wash_vol_val.setText(str(self.gui_controller.default_param[3]))
        self.elute_vol_val.setText(str(self.gui_controller.default_param[4]))
        self.equil_vol_slider.setSliderPosition(self.gui_controller.default_param[1])
        self.load_vol_slider.setSliderPosition(self.gui_controller.default_param[2])
        self.wash_vol_slider.setSliderPosition(self.gui_controller.default_param[3])
        self.elute_vol_slider.setSliderPosition(self.gui_controller.default_param[4])
        self.last_flowpath = [0]*4

        self.fraction_collector_window_on = False
        self.equil_flowpath.setCurrentIndex(1)
        self.load_flowpath.setCurrentIndex(1)
        self.wash_flowpath.setCurrentIndex(1)
        self.elute_flowpath.setCurrentIndex(3)
        # Auto click the combo boxes on start to initialize all the fraction objs
        for i in range(4):
            self.onClickFlowPath(i)
    
    def startProgressBar(self, signalNumber, frame):
        """Start the timer to display the status once purging is completed
        Enable the pause/hold buttons after purging is completed"""  
        try:
            self.protocol_step += 1
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.stop()
            self.status_timer.start(self.step_times[self.protocol_step]*1000)
            self.progressBar.setValue(0)
        except IndexError:
            # Reached the final step
            self._finish_protocol()
        self._set_actionbtn_enable(True, False)

    ## Input Parameter Widget Actions ##

    def onClickFlowPath(self, step_index):
        """
        Control the enable/disable of widgets based on path selected
        Call the fraction collector methods to display the selected fractions if pathway is 3
        Parameters
        ---------------------------------------
        step_index: The index of the step, used to determine whether to use fraction/flow column
        and which text box to use to get the volume to flow
        """
        flow_path_map = {0: 'PRECOLUMNWASTE', 1: 'POSTCOLUMNWASTE', 2: 'FLOWCOL', 3: 'FRACCOL'}
        curIndex = self.flowpath_combo[step_index].currentIndex()
        # ensure that reclicking the same flowpath twice does not mess the fraction collector pathway
        if self.last_flowpath[step_index] != curIndex:
            self.last_flowpath[step_index] = curIndex
            vol = int(self.vol_vals[step_index].text())
            enable_widgets, rejected = self.gui_controller.setFlowPath(step_index, flow_path_map[curIndex], 
                                                vol, self.fraction_collector_window_on)
            self.fraction_widgets_enabler(step_index, enable_widgets)
            if rejected:
                self.flowpath_combo[step_index].setCurrentIndex(0)
                self.last_flowpath[step_index] = 0
    
    def fraction_widgets_enabler(self, step_index, is_enabled):
        """Enable/Disable widgets related to the fraction collector pathway"""
        self.vol_vals[step_index].setEnabled(is_enabled)
        self.vol_sliders[step_index].setEnabled(is_enabled)

    def slider_changed(self, step_index):
        """Updates text label beside the slider when slider is moved
        Parameter
        -------------------------------
        step_index: Used to determine the slider and text widget to use
        """
        self.vol_vals[step_index].setText('{}'.format(self.vol_sliders[step_index].value()))

    def _init_run_param(self):
        """Parse through all the input parameters and return
         an array to pass to controller to run purification"""
        run_param = []
        for widget in self.input_param:
            if self.input_param[widget]:
                # Handle text inputs
                run_param.append(int(widget.text()))
            elif self.input_param[widget] is None:
                # handle the columnsize
                run_param.append(widget)
            else:
                # Handle combo box
                run_param.append(widget.currentIndex())
        # +1 needs to be added to the number of pumps
        run_param[0] = run_param[0] + 1

        # Make the per column calibration list
        calib_list = []
        for i in range(run_param[0]):
            calib_list.append(self.percolumncalib[i])

        return run_param, calib_list

    def calc_step_times(self):
        """Calculates an estimate time for each step"""
        step_times = [int(self.equil_vol_val.text()), int(self.load_vol_val.text()),
                    int(self.wash_vol_val.text()), int(self.elute_vol_val.text())]
        step_times = [i*60 for i in step_times]
        self.step_times = self.gui_controller.getPumpTimes(step_times)

    def protocol_buffers(self):
        """Returns the volume of buffers used. The vol is in CV so to convert
        it in mL need to multiply by the column size"""
        return  {'LOAD_BUFFER': int(self.equil_vol_val.text()),
                'WASH': int(self.wash_vol_val.text()),
                'ELUTION': int(self.elute_vol_val.text()), 'LOAD': int(self.load_vol_val.text())}

    ## Enable/Disable Widgets On GUI ##

    def _set_param_enable(self, state):
        """Enables/Disables all the widgets that allow initializing input parameters
        Used to disable inputting parameters when purifier is running"""
        for widget in self.input_param:
            if self.input_param[widget] is not None:
                widget.setEnabled(state)
        self.equil_vol_slider.setEnabled(state)
        self.load_vol_slider.setEnabled(state)
        self.wash_vol_slider.setEnabled(state)
        self.elute_vol_slider.setEnabled(state)
        self.label.setEnabled(state)
        self.label_2.setEnabled(state)
        self.label_6.setEnabled(state)
        self.label_7.setEnabled(state)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """Either enables or disables the action buttons"""
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.skip_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    ## Action Buttons Event Handlers ##

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.log_update_timer.stop()
        self.Purification.close()
    
    def onClickStart(self):
        """
        First check and make sure text boxes are not empty
        1. Pop up to confirm you want to start
        The following actions are performed after 1s by the check_is_sure_timer handler
        2. Enable stop and close (other action btns enabled after purging)
        3. Disable everything that can be edited
        4. Call _init_run_param() to create the array to pass to controller
        5. Start the logging and timers for estimated time
        6. Update the step display
        7. Run the process
        """
        if self.gui_controller.checkEmptyQLines(self.vol_vals):
            self.gui_controller.columnsize = self.columnsize_int
            self.startbufferWdw()
            self.check_is_sure_timer.start(1000)
    
    def startbufferWdw(self):
        self.bufferwdw = QtWidgets.QMainWindow()
        self.bufferwdw_ui = BackEnd_BuffersWindow(self.bufferwdw, self.gui_controller, self.protocol_buffers())
        self.bufferwdw.show()

    def onClickPauseHold(self, is_pause):
        """
        1. Enables Start button to resume
        2. Calls pause_clicked/hold that sends a pause/hold signal to 
        3. the process running the purification
        4. Update the step display from running to pause/hold
        5. Stops the timer and the progress bar updates
        """
        msg = 'pause' if is_pause else 'hold'
        self.gui_controller.areYouSureMsg(msg)
        if self.gui_controller.is_sure:
            self.stop_btn.setEnabled(False)
            self.gui_controller.is_sure = None
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

            total_remaining = self.total_time_timer.remainingTime()
            self.total_time_timer.stop()
            self.total_time_timer.setInterval(total_remaining)
            self._set_actionbtn_enable(False, True)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(
                self.gui_controller.status_display_stylsheet.format(
                self.gui_controller.status_display_color_halt))
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.onClickResume)

    def onClickResume(self):
        """
        1. Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        2. Updates the status display back to running
        3. Resumes the timer and the progress bar update
        """
        self._set_actionbtn_enable(True, False)
        self.stop_btn.setEnabled(True)
        self.status_timer.start()
        self.total_time_timer.start()
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.gui_controller.resume_clicked()

    def onClickSkip(self):
        """
        1. Stops pumping and goes to the next step
        2. Restarts the progress bar timer for skip to the next bar
        """
        self.gui_controller.areYouSureMsg('skip to next step')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.gui_controller.skip_clicked()

    def onClickStop(self):
        """Signals the script that stop was clicked, to home the device"""
        self.gui_controller.areYouSureMsg('stop')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.current_step_display_btn.setText('STOPPED')
            self.gui_controller.stop_clicked()
            self._finish_protocol()
    
    def _finish_protocol(self):
        """Common protocols between when stop is pressed and once the purification
        process completes. The window is closed and returned to the main_window"""
        self.close_btn.setEnabled(True)
        self._set_actionbtn_enable(False, False)
        msg = QtWidgets.QMessageBox()
        msg.setText('Protocol Completed/Stopped')
        msg.setInformativeText('Click Ok to close the window')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = msg.exec()
        if ret == QtWidgets.QMessageBox.Ok:
            self.close_btn.click()
    

    ## Timer Related Events ##

    def status_timer_handler(self):
        """Stops the timer on the current step"""
        # Reached the final step
        self.status_timer.stop()

    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display"""
        percen_comp = self.progressBar.value()
        if percen_comp < 100 and self.status_timer.isActive():
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/self.step_times[self.protocol_step]))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
            self.progressLabel.setText('{:.1f}%'.format(percen_comp))

        # Disable skip to next on clean up
        if self.protocol_step == 5:
            self.skip_btn.setEnabled(False)

        if self.total_time_timer.isActive():
            lbl = 'Estimated Time: {0:.2f} min(s) remaining'.format(self.total_time_timer.remainingTime()/(1000*60))
            self.estimated_time_remaining_lbl.setText(lbl)

    def get_current_step(self):
        """Used to display the step that is currently running"""
        return ['Setup and Purging','Equilibrate', 'Load', 'Wash', 'Elute', 'Running Clean Up']

    def log_timer_handler(self):
        """Update the logger to display the messages
        TODO: Move the purifer.log reading to controller (all file reads should be in controller)"""
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'r') as f:
            output = f.read()
        if self.log_output is None or self.log_output != output:
            self.log_output_txtbox.setText(output)
            log_end = self.log_output_txtbox.verticalScrollBar().maximum()
            self.log_output_txtbox.verticalScrollBar().setValue(log_end)
        self.log_output = output
    
    def total_time_handler(self):
        self.total_time_timer.stop()
        lbl = 'Less than a minute remaining'
        self.estimated_time_remaining_lbl.setText(lbl)
    
    def check_is_sure_timer_handler(self):
        """Timer is ran after start button is clicked. There needs to be a short delay
        to allow for the buffer window to display before checking for is_sure = True
        to start the protocol"""
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            init_params, calib_list = self._init_run_param()
            self.calc_step_times()
            self.total_time_timer.start(sum(self.step_times)*1000)
            self.current_step_display_btn.setEnabled(True)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.gui_controller.run_purification_script(True, init_params, calib_list)
            self.pbar_timer.start(2000)
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.start(self.step_times[self.protocol_step]*1000)