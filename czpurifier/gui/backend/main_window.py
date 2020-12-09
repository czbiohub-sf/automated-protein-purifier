from PyQt5 import QtCore, QtGui, QtWidgets
from purification import BackEnd_Purification
from custom import BackEnd_CustomWindow
from calibration import BackEnd_CalibrationWindow
from czpurifier.gui.control import GUI_Controller
from czpurifier.gui.frontend import Ui_MainWindow
from constants_calibration import LOAD_VOLUME_1mL, LOAD_VOLUME_5mL
import sys
from time import sleep
from multiprocessing import set_start_method
from typing import List


class BackEnd_MainWindow(Ui_MainWindow):
    """Runs the main window

    :param Ui_MainWindow: Frontend display of the main window
    :type Ui_MainWindow: QMainWindow Class
    """

    def __init__(self, MainWindow):
        """Display the frontend and initialize the backend

        :param MainWindow: The window displaying the Ui
        :type MainWindow: QMainWindow
        """
        self.gui_controller = GUI_Controller()
        super().setupUi(MainWindow)
        self.init_events()

    def init_events(self):
        """Initialize the backend
        """

        self.run_calib_prot_btn.clicked.connect(lambda: self.on_click_run_protocol(2))
        self.purification_btn.clicked.connect(lambda: self.on_click_run_protocol(0))
        self.otherscripts_btn.clicked.connect(lambda: self.on_click_run_protocol(1))
        self.close_btn.clicked.connect(self.on_click_close)
        self.run_sim_btn.clicked.connect(self.on_click_simulator)
        self.columnsize_combo.activated.connect(self.on_select_column_size)

        self.display_calibration_volume(self.gui_controller.actualvol1mL, 10)
        self.columnsize = '1mL'
        self.comboBox.setCurrentIndex(3)
        self.p1_actual.setValidator(QtGui.QDoubleValidator())
        self.p2_actual.setValidator(QtGui.QDoubleValidator())
        self.p3_actual.setValidator(QtGui.QDoubleValidator())
        self.p4_actual.setValidator(QtGui.QDoubleValidator())

        # Timer needed between checking for correct input and opening the new window
        self.start_protocol_timer = QtCore.QTimer()
        self.start_protocol_timer.timeout.connect(self.start_protocol)

    def display_calibration_volume(self, actual_val: List[float], expected_val: List[float]):
        """Update the display of the expected and actual load volume

        :param actual_val: The actual volume measured after running the pumps
        :type actual_val: List[float]
        :param expected_val: The expected volume after running the pumps
        :type expected_val: List[float]
        """

        self.p1_actual.setText('{}'.format(actual_val[0]))
        self.p2_actual.setText('{}'.format(actual_val[1]))
        self.p3_actual.setText('{}'.format(actual_val[2]))
        self.p4_actual.setText('{}'.format(actual_val[3]))

        self.p1_expected.setText('{}'.format(expected_val))
        self.p2_expected.setText('{}'.format(expected_val))
        self.p3_expected.setText('{}'.format(expected_val))
        self.p4_expected.setText('{}'.format(expected_val))

    def on_select_column_size(self):
        """Update the calibration volume display based on column size
        """
        if self.columnsize_combo.currentIndex() == 0:
            self.columnsize = '1mL'
            actual_val = self.gui_controller.actualvol1mL
            expected_val = LOAD_VOLUME_1mL
        else:
            self.columnsize = '5mL'
            actual_val = self.gui_controller.actualvol5mL
            expected_val = LOAD_VOLUME_5mL
        
        self.display_calibration_volume(actual_val, expected_val)

    def run_calibration(self):
        """Opens the calibration window
        """

        num_cols = self.comboBox.currentIndex() + 1
        self.calib = QtWidgets.QMainWindow()
        self.calib_ui = BackEnd_CalibrationWindow(self.calib, self.columnsize, self.percolumn, num_cols)
        self.calib.show()
    
    def run_purification(self):
        """Opens the purification window 
        """

        self.purifier = QtWidgets.QMainWindow()
        self.purifier_ui = BackEnd_Purification(self.purifier, self.gui_controller.device_process, 
                                                self.columnsize, self.percolumn)
        self.purifier.show()

    def run_custom(self):
        """Opens the custom window
        """
        
        self.custom_wdw = QtWidgets.QMainWindow()
        self.custom_ui = BackEnd_CustomWindow(self.custom_wdw, self.gui_controller.device_process, 
                                            self.columnsize, self.percolumn)
        self.custom_wdw.show() 

    def on_click_run_protocol(self, protocol_index: int):
        """Open the selected protocol and pass the calibration factors

        A small timer is started after calculating the calibration factors. The 
        protocol window is opened once the timer finishes. Timer needed for error
        pop ups to function properly.

        :param protocol_index: The identifier to know what protocol to run
        :type protocol_index: int. 0 = basic purification, 1 = custom, 2 = calibration
        :raises ZeroDivisionError: Pops error if any actual volume is set to 0
        :raises ValueError: Pops error is any textbox is empty
        """
        
        try:
            expected = LOAD_VOLUME_1mL if self.columnsize == '1mL' else LOAD_VOLUME_5mL
            self.percolumn = []
            self.percolumn.append(expected/float(self.p1_actual.text()))
            self.percolumn.append(expected/float(self.p2_actual.text()))
            self.percolumn.append(expected/float(self.p3_actual.text()))
            self.percolumn.append(expected/float(self.p4_actual.text()))
            self.start_protocol_timer.start(500)
            self.protocol_index = protocol_index
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

    def start_protocol(self):
        """Starts the desired protocol once the timer completes
        """

        if self.protocol_index == 0:
            self.run_purification()
        elif self.protocol_index == 1:
            self.run_custom()
        else:
            self.run_calibration()
        self.start_protocol_timer.stop()

    def on_click_close(self):
        """Closes the GUI
        """
        quit()

    def on_click_simulator(self):
        """Pops ups are you sure message if simulator mode button is clicked
        """

        if self.confirm_simulator():
            self.run_simulator()
            self.run_sim_btn.setEnabled(False)

    def confirm_simulator(self):
        """Confirms whether or not the user meant to click an action button
        """

        msg = QtWidgets.QMessageBox()
        msg.setText('Are you sure you want to run the simulator mode?')
        msg.setInformativeText('If you are connected to the simulator mode and would like to '
        'switch back to the hardware please close the software and rerun it.\n\n'
        'Click Ok to start simulator')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = msg.exec()
        if ret == QtWidgets.QMessageBox.Ok:
            return True
        else:
            return False

    def run_simulator(self):
        """Run the simulator to debug the GUI
        """
        self.gui_controller.connect_to_simulator()
        msg = QtWidgets.QMessageBox()
        msg.setText('Running Simulator')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()

if __name__ == "__main__":
    import sys
    set_start_method('spawn')  # Allow for different forked processes to get signals
    app = QtWidgets.QApplication(sys.argv)
    timer = QtCore.QTimer()  # Timeout the QEvent to allow for signals to be caught
    timer.start(1000)
    timer.timeout.connect(lambda : None)
    MainWindow = QtWidgets.QMainWindow()
    ui = BackEnd_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())