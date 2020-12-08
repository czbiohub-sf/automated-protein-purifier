from PyQt5 import QtCore, QtGui, QtWidgets
from buffer_parameters import BackEnd_BuffersWindow
from single_step import BackEnd_StepWidget
from czpurifier.gui.frontend import Ui_CustomWindow
from czpurifier.gui.frontend import Ui_StepWidget
from czpurifier.gui.control import GUI_Controller
from os import chdir, path
from signal import signal, SIGUSR1
from time import sleep


class BackEnd_CustomWindow(Ui_CustomWindow):
    def __init__(self, CustomWindow, dev_process, columnsize, percolumncalib):
        self.CustomWindow = CustomWindow
        self.columnsize = columnsize
        self.percolumncalib = percolumncalib
        signal(SIGUSR1, self.startProgressBar)
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.gui_controller.columnsize = 1 if columnsize == '1mL' else 5
        super().setupUi(self.CustomWindow)
        self.initEvents()

    def initEvents(self):
        """Initializes all on click actions"""
        # counts the current step: Needed for adding and removing steps
        self.step_counter = -1
        # Contains the parent widget for a step
        # len(step_widgets) = number of steps
        self.step_widgets = [] #Qt widget object
        self.step_widget_objs = [] # AddStep class object (used to extract input params)
        self.close_btn.clicked.connect(self.onClickClose)
        self.add_step_btn.clicked.connect(self.onClickAddStep)
        self.remove_step.clicked.connect(self.onClickRemoveStep)
        self.remove_step.setEnabled(False)
        self.rep_num_slider.valueChanged.connect(lambda: self.slider_changed(self.rep_num_slider.value(),
                                                    self.rep_num_lbl))
        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.stop_btn.clicked.connect(self.onClickStop)
        self.num_col_combo_box.setCurrentIndex(3)

        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.hold_btn.setEnabled(False)
        self.start_btn.setEnabled(False)

        # Logger initialized to display the steps
        self.log_update_timer = QtCore.QTimer()
        self.log_update_timer.timeout.connect(self.log_timer_handler)
        self.log_update_timer.start(1000)
        self.log_output_txtbox.setReadOnly(True)
        self.log_output = None

        # Timer for widget scroll down once a new widget is added
        self.widgetscroller_timer = QtCore.QTimer()
        self.widgetscroller_timer.timeout.connect(self.update_scoller)

        # Timer for updating the current status
        self.status_timer = QtCore.QTimer()
        self.status_timer.timeout.connect(self.status_timer_handler)

        #Timer for a delay between on start window pop up and checking result
        self.check_is_sure_timer = QtCore.QTimer()
        self.check_is_sure_timer.timeout.connect(self.check_is_sure_timer_handler)

        #Step display
        self.current_step = 0
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)

        self.progressBar.setValue(0)
        self.pbar_timer = QtCore.QTimer()
        self.pbar_timer.timeout.connect(self.progress_bar_handler)

        #Update Total Time Remaining
        self.total_time_timer = QtCore.QTimer()
        self.total_time_timer.timeout.connect(self.total_time_handler)

    def startProgressBar(self, signalNumber, frame):
        """Start the timer to display the status once purging is completed
        Enable the pause/hold buttons after purging is completed"""  
        try:
            self.current_step += 1
            self.current_step_display_btn.setText(self.step_output[self.current_step])
            self.status_timer.stop()
            self.status_timer.start(self.step_times[self.current_step]*1000)
            self.progressBar.setValue(0)
        except IndexError:
            # Reached the final step
            self._finish_protocol()
        self._set_actionbtn_enable(True, False)

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.CustomWindow.close()

    def onClickAddStep(self):
        """Creates a new widget to add the input parameters"""
        self.start_btn.setEnabled(True)
        self.step_counter += 1
        self.step_widgets.append(QtWidgets.QWidget(self.scrollAreaWidgetContents))
        self.step_widget_objs.append(BackEnd_StepWidget(self.step_widgets[self.step_counter], 
                                self.step_counter, self.gui_controller))
        self.verticalLayout_5.addWidget(self.step_widgets[self.step_counter])
        self.gui_controller.flowpathwayClicked(self.step_counter, 1)
        self.remove_step.setEnabled(True)
        self.widgetscroller_timer.start(50)

    def onClickRemoveStep(self):
        """Removes the last step that was added"""
        self.step_widgets[self.step_counter].setParent(None)
        self.step_widgets.pop()
        self.step_widget_objs.pop()
        self.gui_controller.fractionCollectorUnsel(self.step_counter)
        self.gui_controller.fracflow_objs.pop(self.step_counter)
        self.step_counter -= 1
        if self.step_counter < 0:
            self.remove_step.setEnabled(False)
            self.start_btn.setEnabled(False)
    
    def update_scoller(self):
        end = self.scrollArea.verticalScrollBar().maximum()
        self.scrollArea.verticalScrollBar().setValue(end)
        self.widgetscroller_timer.stop()

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))
    
    def _generate_run_parameters(self):
        """Generates an array of the run parameters

        Return
        ----------------------------------
        [[4, 1, 10],[None, 200, 0],[2, 100, 1],....]"""
        input_params = []
        rep = int(self.rep_num_lbl.text())
        input_params.append([self.num_col_combo_box.currentIndex()+1, self.columnsize, rep])
        for c in self.step_widget_objs:
            inp = []
            if c.port_combo_box.isEnabled():
                inp.append(c.port_combo_box.currentIndex())
            else:
                inp.append(None)
            inp.append(int(c.volume_val_lbl.text()))
            inp.append(c.flowpath_combo_box.currentIndex())
            input_params.append(inp)
        
        # Create the per column calibration factor list
        calibfactor = []
        for i in range(self.num_col_combo_box.currentIndex()+1):
            calibfactor.append(self.percolumncalib[i])

        return input_params, calibfactor

    def get_step_qlines(self):
        """Returns a list of all the qline widgets on display. Used to check that no field is empty"""
        return [c.volume_val_lbl for c in self.step_widget_objs]
    
    def protocol_buffers(self):
        """Create a dic of all the buffers used and the volume of each"""
        total_buffers = {}
        for c in self.step_widget_objs:
            key_name = str(c.port_combo_box.currentText()) if c.port_combo_box.isEnabled() else 'LOAD'
            if key_name in total_buffers:
                total_buffers[key_name] = total_buffers[key_name] + int(c.volume_val_lbl.text())
            else:
                total_buffers.update({key_name: int(c.volume_val_lbl.text())})
        return total_buffers
    
    def pump_times(self):
        """Get all the pump times for each step"""
        pump_times = []
        for c in self.step_widget_objs:
            pump_times.append(int(c.volume_val_lbl.text())*60)
        # Multiply it with the number of reps so that the pump times repeat for each rep
        pump_times = pump_times*int(self.rep_num_lbl.text())
        self.step_times = self.gui_controller.getPumpTimes(pump_times)

    ## Action Button Event Handlers ##

    def _set_param_enable(self, is_enabled):
        """Enables/Disables all input parameters"""
        self.num_col_combo_box.setEnabled(is_enabled)
        self.rep_num_slider.setEnabled(is_enabled)
        for w in self.step_widgets:
            w.setEnabled(is_enabled)
        self.add_step_btn.setEnabled(is_enabled)
        self.remove_step.setEnabled(is_enabled)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """Either enables or disables the action buttons"""
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    def onClickStart(self):
        """
        1. Pop up to confirm you want to start
        The following actions are performed after 1s by the check_is_sure_timer handler
        2. Enable stop and close (other action btns enabled after purging)
        3. Disable everything that can be edited
        4. Call _generate_run_parameters() to create the array to pass to controller
        5. Start the logging and timers for estimated time
        6. Update the step display
        7. Run the process
        """
        if self.gui_controller.checkEmptyQLines(self.get_step_qlines()):
            col_size = 1 if self.columnsize == '1mL' else 5
            self.gui_controller.columnsize = col_size
            self.startbufferWdw()
            self.check_is_sure_timer.start(1000)
    
    def startbufferWdw(self):
        self.bufferwdw = QtWidgets.QMainWindow()
        self.bufferwdw_ui = BackEnd_BuffersWindow(self.bufferwdw, self.gui_controller, self.protocol_buffers())
        self.bufferwdw.show()

    def onClickPauseHold(self, is_pause):
        """
        Enables Start button to resume
        Calls pause_clicked/hold that sends a pause/hold signal to 
        the process running the purification
        """
        msg = 'pause' if is_pause else 'hold'
        self.gui_controller.areYouSureMsg(msg)
        if self.gui_controller.is_sure:
            self.stop_btn.setEnabled(False)
            total_remaining = self.total_time_timer.remainingTime()
            self.total_time_timer.stop()
            self.total_time_timer.setInterval(total_remaining)
            self.gui_controller.is_sure = None
            self._set_actionbtn_enable(False, True)
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.onClickResume)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(
                self.gui_controller.status_display_stylsheet.format(
                self.gui_controller.status_display_color_halt))
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

    def onClickResume(self):
        """
        Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        """
        self._set_actionbtn_enable(True, False)
        self.stop_btn.setEnabled(True)
        self.gui_controller.resume_clicked()
        self.total_time_timer.start()
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.status_timer.start()

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

    def status_timer_handler(self):
        """Starts the timer on the current step"""
        # Reached the final step
        self.status_timer.stop()

    def create_step_label(self):
        """Create the text output for the status bar"""
        step_list = [i for i in range(len(self.step_widget_objs))]
        num_reps = int(self.rep_num_lbl.text())
        step_list = step_list*num_reps
        rep_list = []
        for i in range(num_reps):
            rep_list += [i+1]*len(self.step_widget_objs)
        self.step_output = ['Step# {} Rep# {}'.format(i,j) for i,j in zip(step_list, rep_list)]
        self.step_output.insert(0, 'Setup and Purging')
        self.step_output.append('Clean Up')


    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display"""
        percen_comp = self.progressBar.value()
        if percen_comp < 100 and self.status_timer.isActive():
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/self.step_times[self.current_step]))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
            self.progressLabel.setText('{:.1f}%'.format(percen_comp))

        if self.total_time_timer.isActive():
            lbl = 'Estimated Time: {0:.2f} min(s) remaining'.format(self.total_time_timer.remainingTime()/(1000*60))
            self.estimated_time_remaining_lbl.setText(lbl)

    def total_time_handler(self):
        self.total_time_timer.stop()
        lbl = 'Less than a minute remaining'
        self.estimated_time_remaining_lbl.setText(lbl)
        
    def check_is_sure_timer_handler(self):
        """Runs the start protocol after the 1s timeout"""
        if self.gui_controller.is_sure:
            init_params, calib_list = self._generate_run_parameters()
            self.gui_controller.is_sure = None
            self.stop_btn.setEnabled(True)
            self.start_btn.setEnabled(False)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            self.gui_controller.run_purification_script(False, init_params, calib_list)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.current_step_display_btn.setEnabled(True)
            self.pump_times()
            self.total_time_timer.start(sum(self.step_times)*1000)
            self.create_step_label()
            self.pbar_timer.start(2000)
            self.current_step_display_btn.setText(self.step_output[self.current_step])
            self.status_timer.start(self.step_times[self.current_step]*1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomWindow = QtWidgets.QMainWindow()
    ui = Ui_CustomWindow()
    ui.setupUi(CustomWindow)
    CustomWindow.show()
    sys.exit(app.exec_())
