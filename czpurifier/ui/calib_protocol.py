from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalibrationProtocol(object):
    def __init__(self, CalibrationProtocol, columnsize):
        """Runs the calibration protocol used to calculate the correction factor"""
        self.CalibrationProtocol = CalibrationProtocol
        self.columnsize = columnsize
        self.setupUi(self.CalibrationProtocol)
        self.initEvents()

    ## Designer Generated Code ##
    def setupUi(self, CalibrationProtocol):
        CalibrationProtocol.setObjectName("CalibrationProtocol")
        CalibrationProtocol.resize(673, 375)
        self.centralwidget = QtWidgets.QWidget(CalibrationProtocol)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.column_size_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.column_size_lbl.setFont(font)
        self.column_size_lbl.setObjectName("column_size_lbl")
        self.gridLayout.addWidget(self.column_size_lbl, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 2)
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
        self.label_3.setText(_translate("CalibrationProtocol", "Column Size:"))
        self.column_size_lbl.setText(_translate("CalibrationProtocol", "1 mL"))
        self.label.setText(_translate("CalibrationProtocol", "Run Calibration Protocol"))
        self.label_2.setText(_translate("CalibrationProtocol", "<html><head/><body><p>The calibration protocol will begin when start is clicked. </p><p>To change the column size close this window and change the column size in the main window<br/><br/><span style=\" font-weight:600;\">Protocol Description:</span></p><p>1 mL: The load is pumped for <span style=\" font-weight:600;\">10 minutes</span> into the first flow column. The expected volume is <span style=\" font-weight:600;\">10mL</span>.</p><p>5mL: The load is pumped for <span style=\" font-weight:600;\">5 minutes</span> into the first flow column. The expected volume is <span style=\" font-weight:600;\">25mL</span>.</p><p><span style=\" font-weight:600;\">Calibration Factor:</span></p><p>The calibration factor for each pump is the <span style=\" font-weight:600;\">Expected Volume/Actual Volume</span></p></body></html>"))
        self.start_btn.setText(_translate("CalibrationProtocol", "START"))

    ## End of designer generated code ##
    def initEvents(self):
        self.column_size_lbl.setText(self.columnsize)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalibrationProtocol = QtWidgets.QMainWindow()
    ui = Ui_CalibrationProtocol()
    ui.setupUi(CalibrationProtocol)
    CalibrationProtocol.show()
    sys.exit(app.exec_())
