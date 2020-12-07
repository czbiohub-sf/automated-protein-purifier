from PyQt5 import QtCore, QtGui, QtWidgets
from purification_gui import Ui_Purification
from custom_protocol import Ui_CustomProtocol
from calib_protocol import Ui_CalibrationProtocol
from czpurifier.gui.control import GUI_Controller
from czpurifier.gui.frontend import Ui_MainWindow
import sys
from time import sleep
from multiprocessing import set_start_method


class BackEnd_MainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.gui_controller = GUI_Controller()
        super().setupUi(MainWindow)
        self.initEvents()

    def initEvents(self):
        """Initialize all buttons"""
        self.run_calib_prot_btn.clicked.connect(lambda: self.percolumncalib(2))
        self.purification_btn.clicked.connect(lambda: self.percolumncalib(0))
        self.otherscripts_btn.clicked.connect(lambda: self.percolumncalib(1))
        self.close_btn.clicked.connect(self.onClick_close_btn)
        self.run_sim_btn.clicked.connect(self.onClick_sim_btn)
        self.columnsize_combo.activated.connect(self.onSelect_columnSize)

        self.update_calib_disp(self.gui_controller.actualvol1mL, 10)
        self.columnsize = '1mL'
        self.comboBox.setCurrentIndex(3)
        self.p1_actual.setValidator(QtGui.QDoubleValidator())
        self.p2_actual.setValidator(QtGui.QDoubleValidator())
        self.p3_actual.setValidator(QtGui.QDoubleValidator())
        self.p4_actual.setValidator(QtGui.QDoubleValidator())

        # Timer needed between checking for correct input and opening the new window
        self.start_protocol_timer = QtCore.QTimer()
        self.start_protocol_timer.timeout.connect(self.startProtocol)

    def update_calib_disp(self, actual_val, expected_val):
        """Update the expected and actual values for the flow volume"""
        self.p1_actual.setText('{}'.format(actual_val[0]))
        self.p2_actual.setText('{}'.format(actual_val[1]))
        self.p3_actual.setText('{}'.format(actual_val[2]))
        self.p4_actual.setText('{}'.format(actual_val[3]))

        self.p1_expected.setText('{}'.format(expected_val))
        self.p2_expected.setText('{}'.format(expected_val))
        self.p3_expected.setText('{}'.format(expected_val))
        self.p4_expected.setText('{}'.format(expected_val))

    def onSelect_columnSize(self):
        """Update the default parameter display based on the column size selected"""
        if self.columnsize_combo.currentIndex() == 0:
            self.columnsize = '1mL'
            actual_val = self.gui_controller.actualvol1mL
            expected_val = 10
        else:
            self.columnsize = '5mL'
            actual_val = self.gui_controller.actualvol5mL
            expected_val = 25
        
        self.update_calib_disp(actual_val, expected_val)

    def onClick_calib_protocol(self):
        num_cols = self.comboBox.currentIndex() + 1
        self.calib = QtWidgets.QMainWindow()
        self.calib_ui = Ui_CalibrationProtocol(self.calib, self.columnsize, self.percolumn, num_cols)
        self.calib.show()

    def onClick_sim_btn(self):
        self.confirm_connectSim()
        if self.is_sure:
            self.is_sure = None
            self.run_sim()
            self.run_sim_btn.setEnabled(False)
    
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

    def run_sim(self):
        """
        Call the method to run the simulator if 'run simulator' is clicked
        on the connect to device pop up
        """
        self.gui_controller.connect_to_simulator()
        msg = QtWidgets.QMessageBox()
        msg.setText('Running Simulator')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
    
    def onClick_purification_btn(self):
        """
        Opens the purification window 
        """
        self.purifier = QtWidgets.QMainWindow()
        self.purifier_ui = Ui_Purification(self.purifier, self.gui_controller.device_process, self.columnsize, self.percolumn)
        self.purifier.show()

    def onClick_otherscripts_btn(self):
        """
        Opens the other scripts window
        """
        self.oth_sc_window = QtWidgets.QMainWindow()
        self.oth_sc_ui = Ui_CustomProtocol(self.oth_sc_window, self.gui_controller.device_process, self.columnsize, self.percolumn)
        self.oth_sc_window.show() 
    
    def onClick_close_btn(self):
        """
        Closes the GUI
        """
        quit()

    def percolumncalib(self, is_basic_purification):
        """Create the list of per column calibration factor based on the input values in the GUI
        Initiated when either basic purification, column calibration or other script button is clicked"""
        try:
            expected = 10 if self.columnsize == '1mL' else 25
            self.percolumn = []
            self.percolumn.append(expected/float(self.p1_actual.text()))
            self.percolumn.append(expected/float(self.p2_actual.text()))
            self.percolumn.append(expected/float(self.p3_actual.text()))
            self.percolumn.append(expected/float(self.p4_actual.text()))
            self.start_protocol_timer.start(500)
            self.is_basic_purification = is_basic_purification
        except ZeroDivisionError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Error! Require non-zero actual volume for pumps!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setText('Error! Actual Volume can\'t be empty!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()

    def startProtocol(self):
        """Starts the protocol window after the wait time passes
        Wait time required for pyqt widgets"""
        if self.is_basic_purification == 0:
            self.onClick_purification_btn()
        elif self.is_basic_purification == 1:
            self.onClick_otherscripts_btn()
        else:
            self.onClick_calib_protocol()
        self.start_protocol_timer.stop()

if __name__ == "__main__":
    import sys
    set_start_method('spawn')
    app = QtWidgets.QApplication(sys.argv)
    # Timeout the QEvent to allow for signals to be caught
    timer = QtCore.QTimer()
    timer.start(1000)
    timer.timeout.connect(lambda : None)
    MainWindow = QtWidgets.QMainWindow()
    ui = BackEnd_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())