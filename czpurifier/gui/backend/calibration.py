from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.control import GUI_Controller
from czpurifier.gui.frontend import Ui_CalibrationWindow
from signal import signal, SIGUSR1


class BackEnd_CalibrationWindow(Ui_CalibrationWindow):
    def __init__(self, CalibrationWindow, columnsize, caliblist, num_cols):
        """Runs the calibration protocol used to calculate the correction factor"""
        self.CalibrationWindow = CalibrationWindow
        self.columnsize = columnsize
        self.caliblist = caliblist
        self.num_cols = num_cols
        self.gui_controller = GUI_Controller()
        self.setupUi(self.CalibrationWindow)
        self.stop_btn.setStyleSheet("QPushButton#stop_btn {border-radius:42;border-width: 2px;background-color: #ed1c24; color:white; font-size:20px; border: 1px solid #808080}\n"
        "QPushButton:pressed#stop_btn{background-color:#A9A9A9}\n"
        "QPushButton:disabled#stop_btn{background-color:#696969}")    
        self.initEvents()
        signal(SIGUSR1, self.calibrationComplete)

    def initEvents(self):
        """Initialize buttons and text displays"""
        self.stop_btn.setEnabled(False)
        self.column_size_lbl.setText(self.columnsize)
        self.start_btn.clicked.connect(self.onClickStart)
        self.stop_btn.clicked.connect(self.onClickStop)

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
        # Add the 2 for the purging time
        self.time = (10+2) if self.columnsize == '1mL' else (5+2)

        load_vol = 10 if self.columnsize == '1mL' else 25
        self.load_vol.setText('{} mL'.format(load_vol+2))

    def onClickStart(self):
        """Start the calibration protocol"""
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.gui_controller.run_calibration_protocol(self.columnsize, self.caliblist, self.num_cols)
        self.pbar_timer.start(2000)
        self.status_timer.start(self.time*60*1000)
    
    def onClickStop(self):
        """Signals the script that stop was clicked, to home the device"""
        self.gui_controller.areYouSureMsg('stop')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.gui_controller.stop_clicked()
            self.CalibrationWindow.close()

    def onClickDone(self):
        """Close the window when calibration is completed"""
        self.CalibrationWindow.close()

    def calibrationComplete(self, signalNumber, frame):
        """Gets this signal when the calibration protcol is finished. Change the START button to done"""  
        self.start_btn.disconnect()
        self.start_btn.setEnabled(True)
        self.start_btn.setText('DONE')
        self.start_btn.clicked.connect(self.onClickDone)
        self.status_timer.stop()
        self.progressBar.setValue(100)

    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display"""
        percen_comp = self.progressBar.value()
        if percen_comp < 100:
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/(self.time*60)))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
    
    def status_timer_handler(self):
        self.progressBar.setValue(99)
        self.pbar_timer.stop()

