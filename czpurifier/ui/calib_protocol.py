from PyQt5 import QtCore, QtGui, QtWidgets
from gui_controller import GUI_Controller
from signal import signal, SIGUSR1


class Ui_CalibrationProtocol(object):
    def __init__(self, CalibrationProtocol, columnsize, caliblist):
        """Runs the calibration protocol used to calculate the correction factor"""
        self.CalibrationProtocol = CalibrationProtocol
        self.columnsize = columnsize
        self.caliblist = caliblist
        self.gui_controller = GUI_Controller()
        self.setupUi(self.CalibrationProtocol)
        self.initEvents()
        signal(SIGUSR1, self.calibrationComplete)

    ## Designer Generated Code ##
    def setupUi(self, CalibrationProtocol):
        CalibrationProtocol.setObjectName("CalibrationProtocol")
        CalibrationProtocol.setWindowModality(QtCore.Qt.ApplicationModal)
        CalibrationProtocol.resize(673, 399)
        self.centralwidget = QtWidgets.QWidget(CalibrationProtocol)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.column_size_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.column_size_lbl.setFont(font)
        self.column_size_lbl.setObjectName("column_size_lbl")
        self.gridLayout.addWidget(self.column_size_lbl, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.load_vol = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.load_vol.setFont(font)
        self.load_vol.setText("")
        self.load_vol.setObjectName("load_vol")
        self.gridLayout.addWidget(self.load_vol, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        CalibrationProtocol.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalibrationProtocol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 22))
        self.menubar.setObjectName("menubar")
        CalibrationProtocol.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalibrationProtocol)
        self.statusbar.setObjectName("statusbar")
        CalibrationProtocol.setStatusBar(self.statusbar)

        self.retranslateUi(CalibrationProtocol)
        QtCore.QMetaObject.connectSlotsByName(CalibrationProtocol)

    def retranslateUi(self, CalibrationProtocol):
        _translate = QtCore.QCoreApplication.translate
        CalibrationProtocol.setWindowTitle(_translate("CalibrationProtocol", "Run Calibration Protocol"))
        self.column_size_lbl.setText(_translate("CalibrationProtocol", "1 mL"))
        self.label_3.setText(_translate("CalibrationProtocol", "Column Size:"))
        self.label_2.setText(_translate("CalibrationProtocol", "<html><head/><body><p>The calibration protocol will begin when start is clicked. </p><p>To change the column size close this window and change the column size in the main window<br/><br/><span style=\" font-weight:600;\">Protocol Description:</span></p><p>1 mL: The load is pumped for <span style=\" font-weight:600;\">10 minutes</span> into the first flow through column. The expected volume is <span style=\" font-weight:600;\">10mL</span>.</p><p>5mL: The load is pumped for <span style=\" font-weight:600;\">5 minutes</span> into the first flow through column. The expected volume is <span style=\" font-weight:600;\">25mL</span>.</p><p><span style=\" font-weight:600;\">Calibration Factor:</span></p><p>The calibration factor for each pump is the <span style=\" font-weight:600;\">Expected Volume/Actual Volume</span></p></body></html>"))
        self.label.setText(_translate("CalibrationProtocol", "Run Calibration Protocol"))
        self.label_4.setText(_translate("CalibrationProtocol", "Load Volume Needed: "))
        self.start_btn.setText(_translate("CalibrationProtocol", "START"))

    ## End of designer generated code ##
    def initEvents(self):
        """Initialize buttons and text displays"""
        self.column_size_lbl.setText(self.columnsize)
        self.start_btn.clicked.connect(self.onClickStart)

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
        """Start the calibration protocol
        TODO: start the progress bar"""
        self.start_btn.setEnabled(False)
        self.gui_controller.run_calibration_protocol(self.columnsize, self.calib_list)
        self.pbar_timer.start(2000)
        self.status_timer.start(self.time*60*1000)
    
    def onClickDone(self):
        """Close the window when calibration is completed"""
        self.CalibrationProtocol.close()

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalibrationProtocol = QtWidgets.QMainWindow()
    ui = Ui_CalibrationProtocol()
    ui.setupUi(CalibrationProtocol)
    CalibrationProtocol.show()
    sys.exit(app.exec_())
