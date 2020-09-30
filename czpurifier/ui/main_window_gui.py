from PyQt5 import QtCore, QtGui, QtWidgets
from purification_gui import Ui_Purification
from custom_protocol import Ui_CustomProtocol
from gui_controller import GUI_Controller
import sys
from time import sleep


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        """
        The initialization for the Main Window that is run 
        upon opening the GUI
        """
        self.gui_controller = GUI_Controller()
        self.setupUi(MainWindow)
        self.initEvents()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.purification_btn = QtWidgets.QPushButton(self.centralwidget)
        self.purification_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.purification_btn.setFont(font)
        self.purification_btn.setObjectName("purification_btn")
        self.verticalLayout.addWidget(self.purification_btn)
        self.otherscripts_btn = QtWidgets.QPushButton(self.centralwidget)
        self.otherscripts_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.otherscripts_btn.setFont(font)
        self.otherscripts_btn.setObjectName("otherscripts_btn")
        self.verticalLayout.addWidget(self.otherscripts_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_sim_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.run_sim_btn.setFont(font)
        self.run_sim_btn.setObjectName("run_sim_btn")
        self.horizontalLayout_3.addWidget(self.run_sim_btn)
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setMinimumSize(QtCore.QSize(10, 0))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Protein Purifier"))
        self.label_2.setText(_translate("MainWindow", "Choose Procedure"))
        self.purification_btn.setText(_translate("MainWindow", "Basic Purification"))
        self.otherscripts_btn.setText(_translate("MainWindow", "Custom Protocol"))
        self.run_sim_btn.setText(_translate("MainWindow", "Run Simulation Mode"))
        self.close_btn.setText(_translate("MainWindow", "Close"))

    def initEvents(self):
        """Initialize all buttons"""
        self.purification_btn.clicked.connect(self.onClick_purification_btn)
        self.otherscripts_btn.clicked.connect(self.onClick_otherscripts_btn)
        self.close_btn.clicked.connect(self.onClick_close_btn)
        self.run_sim_btn.clicked.connect(self.onClick_sim_btn)
        self.connect_device()

    def onClick_sim_btn(self):
        self.confirm_connectSim()
        if self.is_sure:
            self.is_sure = None
            print('Connect')

    def confirm_connectSim(self):
        """Confirms whether or not the user meant to click an action button"""
        msg = QtWidgets.QMessageBox()
        msg.setText('Are you sure you want to run the simulator mode?')
        msg.setInformativeText('If you are connected to the simulator mode and would like to '
        'switch back to the hardware please close the software and rerun it.\n\n'
        'Click Ok to start simulator')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self._msgbtn)
        msg.exec()
    
    def _msgbtn(self, i):
        """Returns the result from the are you sure pop up"""
        self.is_sure = True if 'ok' in i.text().lower() else False

    def connect_device(self):
        """
        Try to connect to device and if failed pop up a message to either
        retry device connection or connect to the simulator
        """
        if not self.gui_controller.connect_to_device():
            self.connect_hardware = QtWidgets.QPushButton('Retry Device Connection')
            self.run_simulator = QtWidgets.QPushButton('Run Simulation Mode')
            self.connect_hardware.clicked.connect(self.onClickConnect_hardware)
            self.run_simulator.clicked.connect(self.onClickRunSim)
            msg = QtWidgets.QMessageBox()
            msg.setText('Failed To Connect')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.addButton(self.connect_hardware, QtWidgets.QMessageBox.NoRole)
            msg.addButton(self.run_simulator, QtWidgets.QMessageBox.NoRole)
            msg.exec()

    def onClickConnect_hardware(self):
        """
        If retry connection is clicked in the connect to device pop up
        The connect device button is automatically clicked to call its on event action
        """
        self.connect_device()

    def onClickRunSim(self):
        """
        Call the method to run the simulator if 'run simulator' is clicked
        on the connect to device pop up
        """
        self.gui_controller.connect_to_simulator()
        msg = QtWidgets.QMessageBox()
        msg.setText('Running Simulator')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
        self.purification_btn.setEnabled(True)
        self.otherscripts_btn.setEnabled(True)
    
    def onClick_purification_btn(self):
        """
        Opens the purification window 
        """
        self.purifier = QtWidgets.QMainWindow()
        self.purifier_ui = Ui_Purification(self.purifier, self.gui_controller.device_process)
        self.purifier.show()

    def onClick_otherscripts_btn(self):
        """
        Opens the other scripts window
        """
        self.oth_sc_window = QtWidgets.QMainWindow()
        self.oth_sc_ui = Ui_CustomProtocol(self.oth_sc_window, self.gui_controller.device_process)
        self.oth_sc_window.show() 
    
    def onClick_close_btn(self):
        """
        Closes the GUI
        """
        quit()        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Timeout the QEvent to allow for signals to be caught
    timer = QtCore.QTimer()
    timer.start(1000)
    timer.timeout.connect(lambda : None)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())