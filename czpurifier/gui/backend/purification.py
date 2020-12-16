from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_PurificationWindow
from buffer_parameters import BackEnd_BuffersWindow
from os import chdir, path, getpid, kill
from signal import signal, SIGUSR1
from time import sleep
from math import ceil
from czpurifier.gui.control import GUI_Controller
from typing import List, Dict

class BackEnd_Purification(Ui_PurificationWindow):
    """Runs the window to run basic protocols

    :param Ui_PurificationWindow: Frontend display of the basic protocol
    :type Ui_PurificationWindow: QMainWindow Class
    """

    def __init__(self, Purification, dev_process: int, 
                columnsize: str, percolumncalib: List[float]):
        """Display the frontend and initialize the backend

        :param Purification: The window displaying the Ui
        :type Purification: QMainWindow
        :param dev_process: The process id running the device/simulator
        :type dev_process: int
        :param columnsize: 1mL or 5mL
        :type columnsize: str
        :param percolumncalib: The pump calibration factors
        :type percolumncalib: List[float]
        """

        self.columnsize = columnsize
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.gui_controller.columnsize = 1 if columnsize == '1mL' else 5
        self.percolumncalib = percolumncalib
        signal(SIGUSR1, self.step_finished_handler)
        self.Purification = Purification
        super().setupUi(self.Purification)
        self.init_events()

    def init_events(self):
        """Initialize the backend
        """

        # Writes to the purifier.log to create an empty log
        # The log file is read and displayed on the gui
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'w') as f:
            f.close()

        # Parsed when start is clicked to determine the input parameters for run purification
        # Key: Name of the widget, Value: True = textbox widget, False = combobox widget
        self.input_param = {self.num_col_combo_box: False, self.columnsize: None,
                            self.equil_vol_val: True, self.equil_flowpath: False, 
                            self.load_vol_val: True, self.load_flowpath: False,
                            self.wash_vol_val: True, self.wash_flowpath: False,
                            self.elute_vol_val: True, self.elute_flowpath: False}
        # Useful groups of widgets for easier access
        self.vol_vals = [self.equil_vol_val, self.load_vol_val, 
                        self.wash_vol_val, self.elute_vol_val]
        self.vol_sliders = [self.equil_vol_slider, self.load_vol_slider, 
                            self.wash_vol_slider, self.elute_vol_slider]
        self.flowpath_combo = [self.equil_flowpath, self.load_flowpath, 
                                self.wash_flowpath, self.elute_flowpath]
        self.columnsize_int = 1 if self.columnsize == '1mL' else 5

        # Widget setup and activation on start
        self.toggle_action_buttons(False, True)
        self.set_default_parameters()
        self.equil_flowpath.activated.connect(lambda: self.on_click_flow_path(0))
        self.load_flowpath.activated.connect(lambda: self.on_click_flow_path(1))
        self.wash_flowpath.activated.connect(lambda: self.on_click_flow_path(2))
        self.elute_flowpath.activated.connect(lambda: self.on_click_flow_path(3))
        self.close_btn.clicked.connect(self.on_click_close)
        self.start_btn.clicked.connect(self.on_click_start)
        self.pause_btn.clicked.connect(lambda: self.on_click_pause_or_hold(True))
        self.hold_btn.clicked.connect(lambda: self.on_click_pause_or_hold(False))
        self.skip_btn.clicked.connect(self.on_click_skip)
        self.stop_btn.clicked.connect(self.on_click_stop)
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

    def set_default_parameters(self):
        """Sets the default input parameters that are on the json file
        """

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
            self.on_click_flow_path(i)
    
    def step_finished_handler(self, signalNumber, frame):
        """Run the progress bar for each step on signal
        """

        try:
            self.protocol_step += 1
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.stop()
            self.status_timer.start(self.step_times[self.protocol_step]*1000)
            self.progressBar.setValue(0)
        except IndexError:
            # Reached the final step
            self.finish_protocol()
        self.toggle_action_buttons(True, False)

    ## Input Parameter Widget Actions ##

    def on_click_flow_path(self, step_index: int):
        """Control enable/disable widgets based on path selected

        Call the fraction collector methods to display the selected fractions

        :param step_index: The index of the step, used to determine 
                        whether to use fraction/flow column and which text box 
                        to use to get the volume to flow
        :type step_index: int
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
    
    def fraction_widgets_enabler(self, step_index: int, is_enabled: bool):
        """Enable/Disable widgets related to the fraction collector pathway

        :param step_index: Used to determine the widget to enable/disable
        :type step_index: int
        :param is_enabled: True: enable
        :type is_enabled: bool
        """

        self.vol_vals[step_index].setEnabled(is_enabled)
        self.vol_sliders[step_index].setEnabled(is_enabled)

    def slider_changed(self, step_index: int):
        """Updates text label beside the slider when slider is moved

        :param step_index: Used to determine the slider and text widget to use
        :type step_index: int
        """
        
        self.vol_vals[step_index].setText('{}'.format(self.vol_sliders[step_index].value()))

    def get_run_parameters(self):
        """Creates the run parameters

        :return: List with the run parameters.
                [number of columns, column size, equil volume, equil flowpath,
                load vol, load flowpath, wash volume, wash flowpath, 
                elute vol, elute flowpath]
        :rtype: [2, '1mL', 50, 2, ...]
        """

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
        return run_param

    def get_pump_calibration_factor(self) -> List[float]:
        """Cut the calibration factor list to the number of column selected

        :return: The per column pump calibration factor
        :rtype: List[float]
        """

        end_point = self.num_col_combo_box.currentIndex()+1
        return self.percolumncalib[0:end_point]

    def calc_step_times(self):
        """Calculates an estimate time for each step
        """

        step_times = [int(self.equil_vol_val.text()), int(self.load_vol_val.text()),
                    int(self.wash_vol_val.text()), int(self.elute_vol_val.text())]
        step_times = [i*60 for i in step_times]
        self.step_times = self.gui_controller.getPumpTimes(step_times)

    def protocol_buffers(self) -> Dict[str, int]:
        """Return a dict of all the reagents used and the volume of each

        :return: dict{a:b}: a = reagent name, b = volume in CV
        :rtype: Dict[str, int]
        """

        return  {'LOAD_BUFFER': int(self.equil_vol_val.text()),
                'WASH': int(self.wash_vol_val.text()),
                'ELUTION': int(self.elute_vol_val.text()), 'LOAD': int(self.load_vol_val.text())}

    ## Enable/Disable Widgets On GUI ##

    def toggle_parameter_widgets(self, state: bool):
        """Enables/Disables all the widgets that allow initializing input parameters

        :param state: True: Enable widget
        :type state: bool
        """

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
    
    def toggle_action_buttons(self, halt_state: bool, start_state: bool):
        """Either enables or disables the action buttons
        
        :param halt_state: True: enable pause/hold/skip/stop buttons
        :type halt_state: bool
        :param start_state: True: enable start button
        :type start_state: bool
        """

        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.skip_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    ## Action Buttons Event Handlers ##

    def on_click_close(self):
        """Closes the purification window when close is clicked
        """

        self.log_update_timer.stop()
        self.Purification.close()
    
    def on_click_start(self):
        """Initiates starting the custom protocol

        Checks there are no empty text boxes and opens the buffer window
        """

        if self.gui_controller.checkEmptyQLines(self.vol_vals):
            self.gui_controller.columnsize = self.columnsize_int
            self.start_buffer_window()
            self.check_is_sure_timer.start(1000)
    
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
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

            total_remaining = self.total_time_timer.remainingTime()
            self.total_time_timer.stop()
            self.total_time_timer.setInterval(total_remaining)
            self.toggle_action_buttons(False, True)
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
            self.start_btn.clicked.connect(self.on_click_resume)

    def on_click_resume(self):
        """Updates widgets and sends resume command to script
        """

        self.toggle_action_buttons(True, False)
        self.stop_btn.setEnabled(True)
        self.status_timer.start()
        self.total_time_timer.start()
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.gui_controller.resume_clicked()

    def on_click_skip(self):
        """Updates widgets and sends skip command to script
        """
        
       
        if  self.gui_controller.areYouSureMsg('skip to next step'):
            self.gui_controller.skip_clicked()

    def on_click_stop(self):
        """Signals the script that stop was clicked, to home the device"""

        if self.gui_controller.areYouSureMsg('stop'):
            self.current_step_display_btn.setText('STOPPED')
            self.gui_controller.stop_clicked()
            self.finish_protocol()
    
    def finish_protocol(self):
        """Common protocols when stop is pressed and once the purification completes.
        """

        self.close_btn.setEnabled(True)
        self.toggle_action_buttons(False, False)
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
        """Stops the timer on the current step
        """

        self.progressBar.setValue(99)
        self.status_timer.stop()  # Reached the final step

    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display
        """

        try:
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
                time_rem = self.total_time_timer.remainingTime()/(1000*60)
                lbl = 'Estimated Time: {0:.2f} min(s) remaining'.format(time_rem)
                self.estimated_time_remaining_lbl.setText(lbl)
        except IndexError:
            pass


    def get_current_step(self):
        """Used to display the step that is currently running
        """

        return ['Setup and Purging','Equilibrate', 'Load', 
                'Wash', 'Elute', 'Running Clean Up']

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
    
    def total_time_handler(self):
        """If the total timer finishes before the final signal stop the timer
        """

        self.total_time_timer.stop()
        lbl = 'Less than a minute remaining'
        self.estimated_time_remaining_lbl.setText(lbl)
    
    def check_is_sure_timer_handler(self):
        """Runs the start protocol after the 1s timeout
        """

        if self.gui_controller.start_protocol:
            self.gui_controller.start_protocol = None
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.close_btn.setEnabled(False)
            self.toggle_parameter_widgets(False)
            init_params = self.get_run_parameters()
            calib_list = self.get_pump_calibration_factor()
            self.calc_step_times()
            self.total_time_timer.start(sum(self.step_times)*1000)
            self.current_step_display_btn.setEnabled(True)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.gui_controller.run_purification_script(True, init_params, calib_list)
            self.pbar_timer.start(2000)
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.start(self.step_times[self.protocol_step]*1000)