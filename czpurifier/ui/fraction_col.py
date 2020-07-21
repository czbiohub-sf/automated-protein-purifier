from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FractionColumn(object):
    def __init__(self, MainWindow):
        """
        Initialization of the GUI to choose the fractionating column
        This window is opened when 'Fraction Column' is chosen as the flow path from the Set Parameter window
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QPushButton#flowth1_btn {\n"
"    border-radius:50\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frac1_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac1_btn.sizePolicy().hasHeightForWidth())
        self.frac1_btn.setSizePolicy(sizePolicy)
        self.frac1_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac1_btn.setStyleSheet("QPushButton#frac1_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac1_btn.setText("")
        self.frac1_btn.setObjectName("frac1_btn")
        self.horizontalLayout_2.addWidget(self.frac1_btn)
        self.frac2_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac2_btn.sizePolicy().hasHeightForWidth())
        self.frac2_btn.setSizePolicy(sizePolicy)
        self.frac2_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac2_btn.setStyleSheet("QPushButton#frac2_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac2_btn.setText("")
        self.frac2_btn.setObjectName("frac2_btn")
        self.horizontalLayout_2.addWidget(self.frac2_btn)
        self.frac3_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac3_btn.sizePolicy().hasHeightForWidth())
        self.frac3_btn.setSizePolicy(sizePolicy)
        self.frac3_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac3_btn.setStyleSheet("QPushButton#frac3_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac3_btn.setText("")
        self.frac3_btn.setObjectName("frac3_btn")
        self.horizontalLayout_2.addWidget(self.frac3_btn)
        self.frac4_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac4_btn.sizePolicy().hasHeightForWidth())
        self.frac4_btn.setSizePolicy(sizePolicy)
        self.frac4_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac4_btn.setStyleSheet("QPushButton#frac4_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac4_btn.setText("")
        self.frac4_btn.setObjectName("frac4_btn")
        self.horizontalLayout_2.addWidget(self.frac4_btn)
        self.frac5_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac5_btn.sizePolicy().hasHeightForWidth())
        self.frac5_btn.setSizePolicy(sizePolicy)
        self.frac5_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac5_btn.setStyleSheet("QPushButton#frac5_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac5_btn.setText("")
        self.frac5_btn.setObjectName("frac5_btn")
        self.horizontalLayout_2.addWidget(self.frac5_btn)
        self.frac6_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac6_btn.sizePolicy().hasHeightForWidth())
        self.frac6_btn.setSizePolicy(sizePolicy)
        self.frac6_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac6_btn.setStyleSheet("QPushButton#frac6_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac6_btn.setText("")
        self.frac6_btn.setObjectName("frac6_btn")
        self.horizontalLayout_2.addWidget(self.frac6_btn)
        self.frac7_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac7_btn.sizePolicy().hasHeightForWidth())
        self.frac7_btn.setSizePolicy(sizePolicy)
        self.frac7_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac7_btn.setStyleSheet("QPushButton#frac7_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac7_btn.setText("")
        self.frac7_btn.setObjectName("frac7_btn")
        self.horizontalLayout_2.addWidget(self.frac7_btn)
        self.frac8_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac8_btn.sizePolicy().hasHeightForWidth())
        self.frac8_btn.setSizePolicy(sizePolicy)
        self.frac8_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac8_btn.setStyleSheet("QPushButton#frac8_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac8_btn.setText("")
        self.frac8_btn.setObjectName("frac8_btn")
        self.horizontalLayout_2.addWidget(self.frac8_btn)
        self.frac9_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac9_btn.sizePolicy().hasHeightForWidth())
        self.frac9_btn.setSizePolicy(sizePolicy)
        self.frac9_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac9_btn.setStyleSheet("QPushButton#frac9_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac9_btn.setText("")
        self.frac9_btn.setObjectName("frac9_btn")
        self.horizontalLayout_2.addWidget(self.frac9_btn)
        self.frac10_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frac10_btn.sizePolicy().hasHeightForWidth())
        self.frac10_btn.setSizePolicy(sizePolicy)
        self.frac10_btn.setMinimumSize(QtCore.QSize(34, 34))
        self.frac10_btn.setStyleSheet("QPushButton#frac10_btn{\n"
"    border-radius:17;\n"
"    background-color: white;\n"
"\n"
"}")
        self.frac10_btn.setText("")
        self.frac10_btn.setObjectName("frac10_btn")
        self.horizontalLayout_2.addWidget(self.frac10_btn)
        self.flowth1_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowth1_btn.sizePolicy().hasHeightForWidth())
        self.flowth1_btn.setSizePolicy(sizePolicy)
        self.flowth1_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.flowth1_btn.setStyleSheet("QPushButton#flowth1_btn {\n"
"    border-radius:30;\n"
"    border-width: 2px;\n"
"    background-color: white;\n"
"\n"
"}")
        self.flowth1_btn.setText("")
        self.flowth1_btn.setObjectName("flowth1_btn")
        self.horizontalLayout_2.addWidget(self.flowth1_btn)
        self.flowth2_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowth2_btn.sizePolicy().hasHeightForWidth())
        self.flowth2_btn.setSizePolicy(sizePolicy)
        self.flowth2_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.flowth2_btn.setStyleSheet("QPushButton#flowth2_btn {\n"
"    border-radius:30;\n"
"    border-width: 2px;\n"
"    background-color: white;\n"
"\n"
"}")
        self.flowth2_btn.setText("")
        self.flowth2_btn.setObjectName("flowth2_btn")
        self.horizontalLayout_2.addWidget(self.flowth2_btn)
        self.flowth3_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowth3_btn.sizePolicy().hasHeightForWidth())
        self.flowth3_btn.setSizePolicy(sizePolicy)
        self.flowth3_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.flowth3_btn.setStyleSheet("QPushButton#flowth3_btn{\n"
"    border-radius:30;\n"
"    border-width: 2px;\n"
"    background-color: white;\n"
"\n"
"}")
        self.flowth3_btn.setText("")
        self.flowth3_btn.setObjectName("flowth3_btn")
        self.horizontalLayout_2.addWidget(self.flowth3_btn)
        self.flowth4_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowth4_btn.sizePolicy().hasHeightForWidth())
        self.flowth4_btn.setSizePolicy(sizePolicy)
        self.flowth4_btn.setMinimumSize(QtCore.QSize(60, 60))
        self.flowth4_btn.setStyleSheet("QPushButton#flowth4_btn{\n"
"    border-radius:30;\n"
"    border-width: 2px;\n"
"    background-color: white;\n"
"\n"
"}")
        self.flowth4_btn.setText("")
        self.flowth4_btn.setObjectName("flowth4_btn")
        self.horizontalLayout_2.addWidget(self.flowth4_btn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.set_fraction_col_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_fraction_col_btn.setObjectName("set_fraction_col_btn")
        self.horizontalLayout_5.addWidget(self.set_fraction_col_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Fraction Position:"))
        self.radioButton_2.setText(_translate("MainWindow", "Select All Fraction Columns"))
        self.radioButton.setText(_translate("MainWindow", "Select All Flow Throw Columns"))
        self.label_2.setText(_translate("MainWindow", "Fraction Volume:"))
        self.label_3.setText(_translate("MainWindow", "Total Volume /"))
        self.set_fraction_col_btn.setText(_translate("MainWindow", "Set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
