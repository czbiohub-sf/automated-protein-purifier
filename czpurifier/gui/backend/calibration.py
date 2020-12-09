from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.control import GUI_Controller
from czpurifier.gui.frontend import Ui_CalibrationWindow
from constants_calibration import LOAD_VOLUME_1mL, LOAD_VOLUME_5mL
from signal import signal, SIGUSR1
from typing import List


class BackEnd_CalibrationWindow(Ui_CalibrationWindow):
    """Runs the calibration protocol to calculate the per pump flowrate correction

    :param Ui_CalibrationWindow: Frontend display of the calibration window
    :type Ui_CalibrationWindow: QMainWindow Class
    """

    def __init__(self, CalibrationWindow, columnsize: str, 
                caliblist: List[float], num_cols: int):
        """Display the frontend and initialize the backend

        :param CalibrationWindow: The window displaying the Ui
        :type CalibrationWindow: QMainWindow
        :param columnsize: Either '1mL' or '5mL'
        :type columnsize: str
        :param caliblist: The per pump actual flow rate from main window
        :type caliblist: List[float]
        :param num_cols: The number of columns to run the calibration on
        :type num_cols: int
        """

        self.CalibrationWindow = CalibrationWindow
        self.columnsize = columnsize
        self.caliblist = caliblist
        self.num_cols = num_cols
        self.gui_controller = GUI_Controller()
        self.setupUi(self.CalibrationWindow)
        self.stop_btn.setStyleSheet("QPushButton#stop_btn {border-radius:42;border-width: 2px;background-color: #ed1c24; color:white; font-size:20px; border: 1px solid #808080}\n"
        "QPushButton:pressed#stop_btn{background-color:#A9A9A9}\n"
        "QPushButton:disabled#stop_btn{background-color:#696969}")    
        self.init_events()
        signal(SIGUSR1, self.calibration_complete)  # signal recieved when run is complete

    def init_events(self):
        """Initialize the backend
        """

        self.stop_btn.setEnabled(False)
        self.column_size_lbl.setText(self.columnsize)
        self.start_btn.clicked.connect(self.on_click_start)
        self.stop_btn.clicked.connect(self.on_click_stop)

        # All progress bars run the following way
        # There is a progress bar timer that times out every 2s
        # There is a status timer that times out after the step is completed
        # The progress bar timeout handler updates the progress bar while the status timer is running
        # When the status timer times out the progress bar timer is stopped
        self.progressBar.setValue(0)
        self.pbar_timer = QtCore.QTimer()
        self.pbar_timer.timeout.connect(self.progress_bar_handler)

        self.status_timer = QtCore.QTimer()
        self.status_timer.timeout.connect(self.status_timer_handler)
        self.time = (10+2) if self.columnsize == '1mL' else (5+2)  # Add 2 for the purging time

        load_vol = LOAD_VOLUME_1mL+2 if self.columnsize == '1mL' else LOAD_VOLUME_5mL+10
        self.load_vol.setText('{} mL'.format(load_vol))  # Add 2 CV for the purging volume

    def on_click_start(self):
        """Start the calibration protocol
        """
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.gui_controller.run_calibration_protocol(self.columnsize, self.caliblist, self.num_cols)
        self.pbar_timer.start(2000)
        self.status_timer.start(self.time*60*1000)
    
    def on_click_stop(self):
        """Signals the script that stop was clicked, to home the device
        """

        self.gui_controller.areYouSureMsg('stop')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.gui_controller.stop_clicked()
            self.CalibrationWindow.close()

    def on_click_done(self):
        """Close the window when calibration is completed
        """

        self.CalibrationWindow.close()

    def calibration_complete(self, signalNumber, frame):
        """Update start button to done when 'done' signal is received
        """
  
        self.start_btn.disconnect()
        self.start_btn.setEnabled(True)
        self.start_btn.setText('DONE')
        self.start_btn.clicked.connect(self.on_click_done)
        self.status_timer_handler()
        self.stop_btn.setEnabled(False)

    def progress_bar_handler(self):
        """Called every 2s to update the progress bar and estimated time remaining
        """

        percen_comp = self.progressBar.value()
        if percen_comp < 100:
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/(self.time*60)))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
    
    def status_timer_handler(self):
        """Called when the total estimated time is reached
        """

        self.progressBar.setValue(99)
        self.pbar_timer.stop()
        self.status_timer.stop()

