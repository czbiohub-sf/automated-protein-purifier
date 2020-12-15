from PyQt5 import QtCore, QtGui, QtWidgets
from buffer_parameters import BackEnd_BuffersWindow
from single_step import BackEnd_StepWidget
from czpurifier.gui.frontend import Ui_CustomWindow
from czpurifier.gui.frontend import Ui_StepWidget
from czpurifier.gui.control import GUI_Controller
from os import chdir, path
from signal import signal, SIGUSR1
from time import sleep
from typing import List, Tuple, Union, Dict


class BackEnd_CustomWindow(Ui_CustomWindow):
    """Runs the window to create custom protocols

    :param Ui_BuffersWindow: Frontend display of the custom window
    :type Ui_BuffersWindow: QMainWindow Class
    """

    def __init__(self, CustomWindow, dev_process: int, 
                columnsize: str, percolumncalib: List[float]):
        """Display the frontend and initialize the backend

        :param CustomWindow: The window displaying the Ui
        :type CustomWindow: QMainWindow
        :param dev_process: The process id running the device/simulator
        :type dev_process: int
        :param columnsize: 1mL or 5mL
        :type columnsize: str
        :param percolumncalib: The pump calibration factors
        :type percolumncalib: List[float]
        """
        
        self.CustomWindow = CustomWindow
        self.columnsize = columnsize
        self.percolumncalib = percolumncalib
        signal(SIGUSR1, self.step_finished_signal_handler)
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.gui_controller.columnsize = 1 if columnsize == '1mL' else 5
        super().setupUi(self.CustomWindow)
        self.init_events()

    def init_events(self):
        """Initialize the backend
        """

        # Writes to the purifier.log to create an empty log
        # The log file is read and displayed on the gui
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'w') as f:
            f.close()

        self.step_counter = -1  # counts the current step
        self.step_widgets = [] #Qt widget object (parent widget list for steps)
        self.step_widget_objs = [] # BackEnd_StepWidget object (used to extract input params)
        self.close_btn.clicked.connect(self.on_click_close)
        self.add_step_btn.clicked.connect(self.on_click_add_step)
        self.remove_step.clicked.connect(self.on_click_remove_step)
        self.remove_step.setEnabled(False)
        self.rep_num_slider.valueChanged.connect(lambda: self.slider_changed(self.rep_num_slider.value(),
                                                    self.rep_num_lbl))
        self.start_btn.clicked.connect(self.on_click_start)
        self.pause_btn.clicked.connect(lambda: self.on_click_pause_or_hold(True))
        self.hold_btn.clicked.connect(lambda: self.on_click_pause_or_hold(False))
        self.stop_btn.clicked.connect(self.on_click_stop)
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
        self.start_process_timer = QtCore.QTimer()
        self.start_process_timer.timeout.connect(self.start_timer_handler)

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

    def step_finished_signal_handler(self, signalNumber, frame):
        """Signal received after each step finishes, moves to next step

        :raises IndexError: If the current_step is larger than the number
                    of steps to complete, it means the process finished
        """

        try:
            self.current_step += 1
            self.current_step_display_btn.setText(self.step_output[self.current_step])
            self.status_timer_handler()
            self.status_timer.start(self.step_times[self.current_step]*1000)
            self.progressBar.setValue(0)
        except IndexError:  # Reached the final step
            self.finish_protocol()
        self.toggle_action_buttons(True, False)

    def on_click_close(self):
        """Closes the custom window when close is clicked
        """

        self.CustomWindow.close()

    def on_click_add_step(self):
        """Creates a new widget to add the input parameters
        """

        self.start_btn.setEnabled(True)
        self.step_counter += 1
        self.step_widgets.append(QtWidgets.QWidget(self.scrollAreaWidgetContents))
        self.step_widget_objs.append(BackEnd_StepWidget(self.step_widgets[self.step_counter], 
                                self.step_counter, self.gui_controller))
        self.verticalLayout_5.addWidget(self.step_widgets[self.step_counter])
        self.gui_controller.flowpathwayClicked(self.step_counter, 1)
        self.remove_step.setEnabled(True)
        self.widgetscroller_timer.start(50)

    def on_click_remove_step(self):
        """Removes the last step that was added
        """

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
        """Updates the scroller to point to the newest step added
        """

        end = self.scrollArea.verticalScrollBar().maximum()
        self.scrollArea.verticalScrollBar().setValue(end)
        self.widgetscroller_timer.stop()

    def slider_changed(self, value, lbl):
        """Used to update the repetition number text beside the slider
        """

        lbl.setText('{}'.format(value))

    def get_run_parameters(self):
        """Get the parameters to run the custom protocol script

        :return: A list of input parameters for each step. The first
                index has the setup parameters [no columns, column size, num repeats]
                The following index has a tuple [a, b, c]: a = buffer type 
                index/None for load, b = the volume to pump in CV, c = the flow path index
        :rtype: [[3, 1mL, 5], [None, 5.0, 0], [2, 2.0, 1], ...]
        """
        
        input_params = []
        rep = int(self.rep_num_lbl.text())
        input_params.append([self.num_col_combo_box.currentIndex()+1, 
                            self.columnsize, rep])
        for c in self.step_widget_objs:
            inp = []
            if c.port_combo_box.isEnabled():
                inp.append(c.port_combo_box.currentIndex())
            else:
                inp.append(None)
            inp.append(float(c.volume_val_lbl.text()))
            inp.append(c.flowpath_combo_box.currentIndex())
            input_params.append(inp)
        return input_params
    
    def get_pump_calibration_factor(self) -> List[float]:
        """Cut the calibration factor list to the number of column selected

        :return: The per column pump calibration factor
        :rtype: List[float]
        """

        end_point = self.num_col_combo_box.currentIndex()+1
        return self.percolumncalib[0:end_point]

    def get_step_qlines(self):
        """Returns a list of all the qline widgets on display.
        
        Used to check that no field is empty
        """

        return [c.volume_val_lbl for c in self.step_widget_objs]
    
    def protocol_buffers(self) -> Dict[str, float]:
        """Return a dict of all the reagents used and the volume of each

        :return: dict{a:b}: a = reagent name, b = volume in CV
        :rtype: Dict[str, float]
        """

        total_buffers = {}
        for c in self.step_widget_objs:
            if c.port_combo_box.isEnabled():
                key_name = str(c.port_combo_box.currentText())
            else:
                key_name = 'LOAD'
            if key_name in total_buffers:
                total_buffers[key_name] = total_buffers[key_name] + float(c.volume_val_lbl.text())
            else:
                total_buffers.update({key_name: float(c.volume_val_lbl.text())})
        return total_buffers
    
    def get_pump_times(self):
        """Get all the pump times for each step
        """

        pump_times = []
        for c in self.step_widget_objs:
            pump_times.append(float(c.volume_val_lbl.text())*60)
        # Multiply it with the number of reps so that the pump times repeat for each rep
        pump_times = pump_times*int(self.rep_num_lbl.text())
        self.step_times = self.gui_controller.getPumpTimes(pump_times)

    ## Action Button Event Handlers ##

    def toggle_parameter_widgets(self, is_enabled: bool):
        """Enables/Disables all input parameter widgets

        :param is_enabled: True: Enable the widget
        :type is_enabled: bool
        """

        self.num_col_combo_box.setEnabled(is_enabled)
        self.rep_num_slider.setEnabled(is_enabled)
        for w in self.step_widgets:
            w.setEnabled(is_enabled)
        self.add_step_btn.setEnabled(is_enabled)
        self.remove_step.setEnabled(is_enabled)
    
    def toggle_action_buttons(self, halt_state: bool, start_state: bool):
        """Enables/Disables all action buttons

        :param halt_state: True: enable pause, hold and stop buttons
        :type halt_state: bool
        :param start_state: True: enable start button
        :type start_state: bool
        """
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    def on_click_start(self):
        """Initiates starting the custom protocol

        Checks there are no empty text boxes and opens the buffer window
        """
    
        if self.gui_controller.checkEmptyQLines(self.get_step_qlines()):
            col_size = 1 if self.columnsize == '1mL' else 5
            self.start_buffer_window()
            self.start_process_timer.start(1000)  # Delay needed for popup to appear
    
    def start_buffer_window(self):
        """Opens the buffer parameters window
        """

        self.bufferwdw = QtWidgets.QMainWindow()
        self.bufferwdw_ui = BackEnd_BuffersWindow(self.bufferwdw, 
                                                self.gui_controller, 
                                                self.protocol_buffers())
        self.bufferwdw.show()

    def on_click_pause_or_hold(self, is_pause: bool):
        """Updates widgets and sends pause/hold signal to process

        :param is_pause: True: pause clicked, False: hold clicked
        :type is_pause: bool
        """

        msg = 'pause' if is_pause else 'hold'
        if self.gui_controller.areYouSureMsg(msg):
            self.stop_btn.setEnabled(False)
            
            # stop total timer and save timestamp
            total_remaining = self.total_time_timer.remainingTime()
            self.total_time_timer.stop()
            self.total_time_timer.setInterval(total_remaining)
            
            # switch start button to resume
            self.toggle_action_buttons(False, True)
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.on_click_resume)

            # send signal to the script running the protocol
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            
            # update the status display bar
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(
                self.gui_controller.status_display_stylsheet.format(
                self.gui_controller.status_display_color_halt))
            
            # stop the timer for the step and save timestamp
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

    def on_click_resume(self):
        """Updates widgets and sends resume command to script
        """

        self.toggle_action_buttons(True, False)
        self.stop_btn.setEnabled(True)
        self.gui_controller.resume_clicked()  # send signal
        self.total_time_timer.start()  # resume total timer
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.status_timer.start()  # resume status timer

    def on_click_stop(self):
        """Sends stop command to script
        """

        if self.gui_controller.areYouSureMsg('stop'):
            self.current_step_display_btn.setText('STOPPED')
            self.gui_controller.stop_clicked()
            self.finish_protocol()
    
    def finish_protocol(self):
        """Display that the protocol finished and close window
        """

        self.close_btn.setEnabled(True)
        self.toggle_action_buttons(False, False)
        self.total_time_timer.stop()
        self.status_timer.stop()
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
        """

        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'r') as f:
            output = f.read()
        if self.log_output is None or self.log_output != output:
            self.log_output_txtbox.setText(output)
            log_end = self.log_output_txtbox.verticalScrollBar().maximum()
            self.log_output_txtbox.verticalScrollBar().setValue(log_end)
        self.log_output = output

    def status_timer_handler(self):
        """Starts the timer on the current step
        """

        self.progressBar.setValue(99)
        self.status_timer.stop()

    def create_step_label(self):
        """Create the text output for the status bar
        """

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
        """Update the progress bar and estimated time remaining display
        """

        percen_comp = self.progressBar.value()
        if percen_comp < 100 and self.status_timer.isActive():
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/self.step_times[self.current_step]))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
            self.progressLabel.setText('{:.1f}%'.format(percen_comp))

        if self.total_time_timer.isActive():
            time = self.total_time_timer.remainingTime()/(1000*60)
            lbl = 'Estimated Time: {0:.2f} min(s) remaining'.format(time)
            self.estimated_time_remaining_lbl.setText(lbl)

    def total_time_handler(self):
        """If the total timer finishes before the final signal stop the timer
        """

        self.total_time_timer.stop()
        lbl = 'Less than a minute remaining'
        self.estimated_time_remaining_lbl.setText(lbl)
        
    def start_timer_handler(self):
        """Runs the start protocol after the 1s timeout
        """

        if self.gui_controller.start_protocol:
            self.gui_controller.start_protocol = None
            init_params = self.get_run_parameters()
            calib_list = self.get_pump_calibration_factor()
            self.stop_btn.setEnabled(True)
            self.start_btn.setEnabled(False)
            self.close_btn.setEnabled(False)
            self.toggle_parameter_widgets(False)
            self.gui_controller.run_purification_script(False, init_params, calib_list)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.current_step_display_btn.setEnabled(True)
            self.get_pump_times()
            self.total_time_timer.start(sum(self.step_times)*1000)
            self.create_step_label()
            self.pbar_timer.start(2000)
            self.current_step_display_btn.setText(self.step_output[self.current_step])
            self.status_timer.start(self.step_times[self.current_step]*1000)
