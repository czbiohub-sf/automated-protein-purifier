from PyQt5 import QtCore, QtGui, QtWidgets
from fraction_col_gui import Ui_FractionColumn
from buffer_param_gui import Ui_BuffersWindow
from gui_controller import GUI_Controller
from os import chdir, path
from signal import signal, SIGUSR2, SIGUSR1
from time import sleep


class Ui_CustomProtocol(object):
    def __init__(self, CustomProtocol, dev_process):
        self.CustomProtocol = CustomProtocol
        signal(SIGUSR2, self.purificationComplete)
        signal(SIGUSR1, self.startProgressBar)
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.setupUi(self.CustomProtocol)
        self.initEvents()

    ###########################
    # Desinger Generated Code #
    ###########################

    def setupUi(self, CustomProtocol):
        CustomProtocol.setObjectName("CustomProtocol")
        CustomProtocol.setWindowModality(QtCore.Qt.ApplicationModal)
        CustomProtocol.resize(1440, 775)
        self.centralwidget = QtWidgets.QWidget(CustomProtocol)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cust_prot_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cust_prot_lbl.sizePolicy().hasHeightForWidth())
        self.cust_prot_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cust_prot_lbl.setFont(font)
        self.cust_prot_lbl.setObjectName("cust_prot_lbl")
        self.verticalLayout_3.addWidget(self.cust_prot_lbl)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.num_col_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_col_lbl.sizePolicy().hasHeightForWidth())
        self.num_col_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.num_col_lbl.setFont(font)
        self.num_col_lbl.setStyleSheet("")
        self.num_col_lbl.setObjectName("num_col_lbl")
        self.horizontalLayout_13.addWidget(self.num_col_lbl)
        self.num_col_combo_box = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.num_col_combo_box.setFont(font)
        self.num_col_combo_box.setStyleSheet("")
        self.num_col_combo_box.setObjectName("num_col_combo_box")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.horizontalLayout_13.addWidget(self.num_col_combo_box)
        self.col_vol_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.col_vol_lbl.sizePolicy().hasHeightForWidth())
        self.col_vol_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.col_vol_lbl.setFont(font)
        self.col_vol_lbl.setStyleSheet("")
        self.col_vol_lbl.setObjectName("col_vol_lbl")
        self.horizontalLayout_13.addWidget(self.col_vol_lbl)
        self.col_vol_combo_box = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.col_vol_combo_box.setFont(font)
        self.col_vol_combo_box.setObjectName("col_vol_combo_box")
        self.col_vol_combo_box.addItem("")
        self.col_vol_combo_box.addItem("")
        self.horizontalLayout_13.addWidget(self.col_vol_combo_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.rep_num_slider = QtWidgets.QSlider(self.centralwidget)
        self.rep_num_slider.setMinimum(1)
        self.rep_num_slider.setMaximum(100)
        self.rep_num_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rep_num_slider.setObjectName("rep_num_slider")
        self.horizontalLayout_14.addWidget(self.rep_num_slider)
        self.rep_num_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rep_num_lbl.sizePolicy().hasHeightForWidth())
        self.rep_num_lbl.setSizePolicy(sizePolicy)
        self.rep_num_lbl.setMinimumSize(QtCore.QSize(20, 0))
        self.rep_num_lbl.setObjectName("rep_num_lbl")
        self.horizontalLayout_14.addWidget(self.rep_num_lbl)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 890, 346))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.add_step_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_step_btn.sizePolicy().hasHeightForWidth())
        self.add_step_btn.setSizePolicy(sizePolicy)
        self.add_step_btn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.add_step_btn.setFont(font)
        self.add_step_btn.setStyleSheet("QPushButton#add_step_btn {border-radius:25;border-width: 2px;background-color: #32CD32; color:white; border: 1px solid #808080}\n"
"QPushButton:pressed#add_step_btn{background-color:#A9A9A9}\n"
"QPushButton:disabled#add_step_btn{background-color:#696969}")
        self.add_step_btn.setObjectName("add_step_btn")
        self.horizontalLayout_3.addWidget(self.add_step_btn)
        self.remove_step = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_step.sizePolicy().hasHeightForWidth())
        self.remove_step.setSizePolicy(sizePolicy)
        self.remove_step.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.remove_step.setFont(font)
        self.remove_step.setStyleSheet("QPushButton#remove_step {border-radius:25;border-width: 2px;background-color: #FF4500; color:white; border: 1px solid #808080}\n"
"QPushButton:pressed#remove_step{background-color:#A9A9A9}\n"
"QPushButton:disabled#remove_step{background-color:#696969}")
        self.remove_step.setObjectName("remove_step")
        self.horizontalLayout_3.addWidget(self.remove_step)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.current_step_display_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_step_display_btn.sizePolicy().hasHeightForWidth())
        self.current_step_display_btn.setSizePolicy(sizePolicy)
        self.current_step_display_btn.setMinimumSize(QtCore.QSize(300, 25))
        self.current_step_display_btn.setStyleSheet("QPushButton#current_step_display_btn {border-radius:10;border-width: 2px; background-color: #3CB371; font-size:14px;}\n"
"QPushButton:disabled#current_step_display_btn{background-color:#A9A9A9}")
        self.current_step_display_btn.setObjectName("current_step_display_btn")
        self.horizontalLayout_2.addWidget(self.current_step_display_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.status_display_btn = QtWidgets.QPushButton(self.centralwidget)
        self.status_display_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_display_btn.sizePolicy().hasHeightForWidth())
        self.status_display_btn.setSizePolicy(sizePolicy)
        self.status_display_btn.setMinimumSize(QtCore.QSize(300, 25))
        self.status_display_btn.setStyleSheet("QPushButton#status_display_btn {border-radius:10;border-width: 2px; background-color: #3CB371; font-size:14px;}\n"
"QPushButton:disabled#status_display_btn{background-color:#A9A9A9}")
        self.status_display_btn.setObjectName("status_display_btn")
        self.horizontalLayout_16.addWidget(self.status_display_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.log_output_txtbox = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_output_txtbox.sizePolicy().hasHeightForWidth())
        self.log_output_txtbox.setSizePolicy(sizePolicy)
        self.log_output_txtbox.setMinimumSize(QtCore.QSize(500, 0))
        self.log_output_txtbox.setObjectName("log_output_txtbox")
        self.verticalLayout_7.addWidget(self.log_output_txtbox)
        self.estimated_time_remaining_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.estimated_time_remaining_lbl.setFont(font)
        self.estimated_time_remaining_lbl.setObjectName("estimated_time_remaining_lbl")
        self.verticalLayout_7.addWidget(self.estimated_time_remaining_lbl)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.start_btn.setStyleSheet("QPushButton#start_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}QPushButton:pressed#start_btn{background-color:#A9A9A9}")
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.pause_btn.setStyleSheet("QPushButton#pause_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}QPushButton:pressed#pause_btn{background-color:#A9A9A9}")
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout.addWidget(self.pause_btn)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.hold_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hold_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.hold_btn.setStyleSheet("QPushButton#hold_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}\n"
"QPushButton:pressed#hold_btn{background-color:#A9A9A9}")
        self.hold_btn.setObjectName("hold_btn")
        self.horizontalLayout.addWidget(self.hold_btn)
        spacerItem4 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.stop_btn.setStyleSheet("QPushButton#stop_btn {border-radius:35;border-width: 2px;background-color: #ed1c24; color:white; font-size:20px; border: 1px solid #808080}\n"
"QPushButton:pressed#stop_btn{background-color:#A9A9A9}\n"
"QPushButton:disabled#stop_btn{background-color:#696969}")
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_7.addWidget(self.stop_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_7.addWidget(self.close_btn)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        CustomProtocol.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CustomProtocol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        CustomProtocol.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CustomProtocol)
        self.statusbar.setObjectName("statusbar")
        CustomProtocol.setStatusBar(self.statusbar)

        self.retranslateUi(CustomProtocol)
        QtCore.QMetaObject.connectSlotsByName(CustomProtocol)

    def retranslateUi(self, CustomProtocol):
        _translate = QtCore.QCoreApplication.translate
        CustomProtocol.setWindowTitle(_translate("CustomProtocol", "Custom Protocol"))
        self.cust_prot_lbl.setText(_translate("CustomProtocol", "Create Custom Protocol:"))
        self.label_8.setText(_translate("CustomProtocol", "Purging bubbles and clean up will be automatically added before and after the custom purification protocol"))
        self.num_col_lbl.setText(_translate("CustomProtocol", "Number of Columns: "))
        self.num_col_combo_box.setItemText(0, _translate("CustomProtocol", "1"))
        self.num_col_combo_box.setItemText(1, _translate("CustomProtocol", "2"))
        self.num_col_combo_box.setItemText(2, _translate("CustomProtocol", "3"))
        self.num_col_combo_box.setItemText(3, _translate("CustomProtocol", "4"))
        self.col_vol_lbl.setText(_translate("CustomProtocol", "Column Volume: "))
        self.col_vol_combo_box.setItemText(0, _translate("CustomProtocol", "1 mL"))
        self.col_vol_combo_box.setItemText(1, _translate("CustomProtocol", "5 mL"))
        self.label_10.setText(_translate("CustomProtocol", "Repeat: "))
        self.rep_num_lbl.setText(_translate("CustomProtocol", "1"))
        self.add_step_btn.setText(_translate("CustomProtocol", "+"))
        self.remove_step.setText(_translate("CustomProtocol", "-"))
        self.label_9.setText(_translate("CustomProtocol", "Status:"))
        self.status_display_btn.setText(_translate("CustomProtocol", "--"))
        self.label.setText(_translate("CustomProtocol", "Current Step:"))
        self.current_step_display_btn.setText(_translate("CustomProtocol", "--"))
        self.start_btn.setText(_translate("CustomProtocol", "START"))
        self.pause_btn.setText(_translate("CustomProtocol", "PAUSE"))
        self.hold_btn.setText(_translate("CustomProtocol", "HOLD"))
        self.stop_btn.setText(_translate("CustomProtocol", "STOP"))
        self.close_btn.setText(_translate("CustomProtocol", "Close"))
        self.estimated_time_remaining_lbl.setText(_translate("CustomProtocol", "Total Estimated Time: <..> min(s)"))

    ###################
    # Event Handlers #
    ##################

    def initEvents(self):
        """Initializes all on click actions"""
        # counts the current step: Needed for adding and removing steps
        self.step_counter = -1
        # Contains the parent widget for a step
        # len(step_widgets) = number of steps
        self.step_widgets = [] #Qt widget object
        self.step_widget_objs = [] # AddStep class object (used to extract input params)
        self.close_btn.clicked.connect(self.onClickClose)
        self.add_step_btn.clicked.connect(self.onClickAddStep)
        self.remove_step.clicked.connect(self.onClickRemoveStep)
        self.remove_step.setEnabled(False)
        self.rep_num_slider.valueChanged.connect(lambda: self.slider_changed(self.rep_num_slider.value(),
                                                    self.rep_num_lbl))
        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.stop_btn.clicked.connect(self.onClickStop)

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
        self.check_is_sure_timer = QtCore.QTimer()
        self.check_is_sure_timer.timeout.connect(self.check_is_sure_timer_handler)

        #Step display
        self.current_step = 0
        self.rep_num = 1
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)

        self.progressBar.setValue(0)
        self.pbar_timer = QtCore.QTimer()
        self.pbar_timer.timeout.connect(self.progress_bar_handler)

    def purificationComplete(self, signalNumber, frame):
        """Handler for SIGUSR2. Prepares UI for another purification protocol"""
        self._finish_protocol()

    def startProgressBar(self, signalNumber, frame):
        """Start the timer to display the status once purging is completed
        Enable the pause/hold buttons after purging is completed"""
        self.status_timer.start(2000)
        self.pbar_timer.start(2000)    
        self._set_actionbtn_enable(True, False)

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.CustomProtocol.close()

    def onClickAddStep(self):
        """Creates a new widget to add the input parameters"""
        self.start_btn.setEnabled(True)
        self.step_counter += 1
        self.step_widgets.append(QtWidgets.QWidget(self.scrollAreaWidgetContents))
        self.step_widget_objs.append(AddStep(self.step_widgets[self.step_counter], 
                                self.step_counter, self.gui_controller))
        self.verticalLayout_5.addWidget(self.step_widgets[self.step_counter])
        self.gui_controller.flowpathwayClicked(self.step_counter, 1)
        self.remove_step.setEnabled(True)
        self.widgetscroller_timer.start(50)

    def onClickRemoveStep(self):
        """Removes the last step that was added"""
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
        end = self.scrollArea.verticalScrollBar().maximum()
        self.scrollArea.verticalScrollBar().setValue(end)
        self.widgetscroller_timer.stop()

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))
    
    def _generate_run_parameters(self):
        """Generates an array of the run parameters

        Return
        ----------------------------------
        [[4, 1, 10],[None, 200, 0],[2, 100, 1],....]"""
        input_params = []
        self.col_size = 1 if self.col_vol_combo_box.currentIndex() == 0 else 5
        rep = int(self.rep_num_lbl.text())
        input_params.append([self.num_col_combo_box.currentIndex()+1, self.col_size, rep])
        for c in self.step_widget_objs:
            inp = []
            if c.port_combo_box.isEnabled():
                inp.append(c.port_combo_box.currentIndex())
            else:
                inp.append(None)
            inp.append(int(c.volume_val_lbl.text()))
            inp.append(c.flowpath_combo_box.currentIndex())
            input_params.append(inp)
        return input_params

    def get_step_qlines(self):
        """Returns a list of all the qline widgets on display. Used to check that no field is empty"""
        return [c.volume_val_lbl for c in self.step_widget_objs]
    
    def protocol_buffers(self):
        """Create a dic of all the buffers used and the volume of each"""
        total_buffers = {}
        for c in self.step_widget_objs:
            if c.port_combo_box.isEnabled():
                total_buffers.update({str(c.port_combo_box.currentText()): int(c.volume_val_lbl.text())})
        return total_buffers
    
    def pump_times(self):
        """Get all the pump times for each step"""
        pump_times = []
        for c in self.step_widget_objs:
            pump_times.append(int(c.volume_val_lbl.text())*60)
        return pump_times

    ## Action Button Event Handlers ##

    def _set_param_enable(self, is_enabled):
        """Enables/Disables all input parameters"""
        self.col_vol_combo_box.setEnabled(is_enabled)
        self.num_col_combo_box.setEnabled(is_enabled)
        self.rep_num_slider.setEnabled(is_enabled)
        for w in self.step_widgets:
            w.setEnabled(is_enabled)
        self.add_step_btn.setEnabled(is_enabled)
        self.remove_step.setEnabled(is_enabled)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """Either enables or disables the action buttons"""
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    def onClickStart(self):
        """
        1. Pop up to confirm you want to start
        The following actions are performed after 1s by the check_is_sure_timer handler
        2. Enable stop and close (other action btns enabled after purging)
        3. Disable everything that can be edited
        4. Call _generate_run_parameters() to create the array to pass to controller
        5. Start the logging and timers for estimated time
        6. Update the step display
        7. Run the process
        """
        if self.gui_controller.checkEmptyQLines(self.get_step_qlines()):
            self.col_size = 1 if self.col_vol_combo_box.currentIndex() == 0 else 5
            self.gui_controller.columnsize = self.col_size
            self.startbufferWdw()
            self.check_is_sure_timer.start(1000)
    
    def startbufferWdw(self):
        self.bufferwdw = QtWidgets.QMainWindow()
        self.bufferwdw_ui = Ui_BuffersWindow(self.bufferwdw, self.gui_controller, self.protocol_buffers())
        self.bufferwdw.show()

    def onClickPauseHold(self, is_pause):
        """
        Enables Start button to resume
        Calls pause_clicked/hold that sends a pause/hold signal to 
        the process running the purification
        """
        msg = 'pause' if is_pause else 'hold'
        self.gui_controller.areYouSureMsg(msg)
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self._set_actionbtn_enable(False, True)
            self.stop_btn.setEnabled(True)
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.onClickResume)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(
                self.gui_controller.status_display_stylsheet.format(
                self.gui_controller.status_display_color_halt))
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

    def onClickResume(self):
        """
        Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        """
        self._set_actionbtn_enable(True, False)
        self.gui_controller.resume_clicked()
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.status_timer.start()

    def onClickStop(self):
        """Signals the script that stop was clicked, to home the device"""
        self.gui_controller.areYouSureMsg('stop')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.current_step_display_btn.setText('STOPPED')
            self.gui_controller.stop_clicked()
            self._finish_protocol()
    
    def _finish_protocol(self):
        """Common protocols between when stop is pressed and once the purification
        process completes. The window is closed and returned to the main_window"""
        self.close_btn.setEnabled(True)
        self._set_actionbtn_enable(False, False)
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
        TODO: Move the purifer.log reading to controller (all file reads should be in controller)"""
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'r') as f:
            output = f.read()
        if self.log_output is None or self.log_output != output:
            self.log_output_txtbox.setText(output)
            log_end = self.log_output_txtbox.verticalScrollBar().maximum()
            self.log_output_txtbox.verticalScrollBar().setValue(log_end)
        self.log_output = output

    def status_timer_handler(self):
        """Starts the timer on the current step"""
        if self.current_step == len(self.step_widget_objs):
            self.rep_num += 1
            self.current_step = 0

        if self.rep_num > int(self.rep_num_lbl.text()):
            self.rep_num = 1
            self.status_timer.stop()
            output = 'Running Cleanup'
        else:
            pump_vol = self.pump_times()[self.current_step]
            self.status_timer.start(pump_vol*1000)
            output = 'Step# {} Rep# {}'.format(self.current_step, self.rep_num)
            self.current_step +=1
        self.current_step_display_btn.setText(output)

    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display"""
        if self.status_timer.isActive() and self.current_step > 0:
            percen_comp = self.progressBar.value()
            if percen_comp < 100:
                # Calculating time remaining
                time_remaining = (self.status_timer.remainingTime())/1000
                percen_comp = (1-(time_remaining/self.pump_times()[self.current_step - 1]))*100
                self.progressBar.setValue(percen_comp)
                if percen_comp == 100:
                    self.progressBar.setValue(0)

    def check_is_sure_timer_handler(self):
        """Runs the start protocol after the 1s timeout"""
        if self.gui_controller.is_sure:
            init_params = self._generate_run_parameters()
            self.gui_controller.is_sure = None
            self.stop_btn.setEnabled(True)
            self.start_btn.setEnabled(False)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            self.gui_controller.run_purification_script(False, init_params)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.current_step_display_btn.setEnabled(True)
            self.current_step_display_btn.setText('Setup And Purging Bubbles')
            self.estimated_time_remaining_lbl.setText(self.gui_controller.getET(self.pump_times()))

class AddStep():
    def __init__(self, step_widget, step_no, gui_controller):
        """Implements the initialization and control of a single step widget
        A step widget is defined as the parent widget containing all the input 
        parameters needed to define a single step
        Parameters
        ---------------------------
        step_widget: Parent QtWidget object for the step
        step_no: The step that we are currently on
        gui_controller: GUI_Controller obj for flowpath selection
        """
        self.add_step_widget = step_widget
        self.gui_controller = gui_controller
        self.step_no = step_no
        self._create_widget(step_no)
        self._init_widget_actions()
    
    def _create_widget(self, step_no):
        """Contains implementation for the widgets for each step"""

        ####################################################################################
        # Designer Generated Code 
        # To update find the first line below in the new code and paste till indicated below
        ####################################################################################
        self.gridLayout_4 = QtWidgets.QGridLayout(self.add_step_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.valve_inp_lbl = QtWidgets.QLabel(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valve_inp_lbl.setFont(font)
        self.valve_inp_lbl.setObjectName("valve_inp_lbl")
        self.gridLayout_3.addWidget(self.valve_inp_lbl, 1, 0, 1, 1)
        self.port_lbl = QtWidgets.QLabel(self.add_step_widget)
        self.port_lbl.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_lbl.setFont(font)
        self.port_lbl.setObjectName("port_lbl")
        self.gridLayout_3.addWidget(self.port_lbl, 2, 0, 1, 1)
        self.vol_lbl = QtWidgets.QLabel(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vol_lbl.setFont(font)
        self.vol_lbl.setObjectName("vol_lbl")
        self.gridLayout_3.addWidget(self.vol_lbl, 3, 0, 1, 1)
        self.flowpath_lbl = QtWidgets.QLabel(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.flowpath_lbl.setFont(font)
        self.flowpath_lbl.setObjectName("flowpath_lbl")
        self.gridLayout_3.addWidget(self.flowpath_lbl, 4, 0, 1, 1)
        self.flowpath_combo_box = QtWidgets.QComboBox(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.flowpath_combo_box.setFont(font)
        self.flowpath_combo_box.setObjectName("flowpath_combo_box")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.flowpath_combo_box, 4, 1, 1, 1)
        self.volume_slider = QtWidgets.QSlider(self.add_step_widget)
        self.volume_slider.setMaximum(200)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.gridLayout_3.addWidget(self.volume_slider, 3, 1, 1, 1)
        self.valve_inp_combo_box = QtWidgets.QComboBox(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valve_inp_combo_box.setFont(font)
        self.valve_inp_combo_box.setObjectName("valve_inp_combo_box")
        self.valve_inp_combo_box.addItem("")
        self.valve_inp_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.valve_inp_combo_box, 1, 1, 1, 1)
        self.port_combo_box = QtWidgets.QComboBox(self.add_step_widget)
        self.port_combo_box.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_combo_box.setFont(font)
        self.port_combo_box.setObjectName("port_combo_box")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.port_combo_box, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.add_step_widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 3)
        self.volume_val_lbl = QtWidgets.QLineEdit(self.add_step_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_val_lbl.sizePolicy().hasHeightForWidth())
        self.volume_val_lbl.setSizePolicy(sizePolicy)
        self.volume_val_lbl.setMaximumSize(QtCore.QSize(60, 16777215))
        self.volume_val_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.volume_val_lbl.setObjectName("volume_val_lbl")
        self.gridLayout_3.addWidget(self.volume_val_lbl, 3, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.add_step_widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 5, 1, 1, 3)
        self.step_num = QtWidgets.QLabel(self.add_step_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.step_num.setFont(font)
        self.step_num.setAlignment(QtCore.Qt.AlignCenter)
        self.step_num.setObjectName("step_num")
        self.gridLayout_3.addWidget(self.step_num, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        ###### Fine the above line and paste until that#######
        
        _translate = QtCore.QCoreApplication.translate
        self.valve_inp_lbl.setText(_translate("CustomProtocol", "Valve Input:"))
        self.port_lbl.setText(_translate("CustomProtocol", "Port:"))
        self.vol_lbl.setText(_translate("CustomProtocol", "Total Volume:"))
        self.flowpath_lbl.setText(_translate("CustomProtocol", "Flow Path:"))
        self.flowpath_combo_box.setItemText(0, _translate("CustomProtocol", "Pre Column Waste"))
        self.flowpath_combo_box.setItemText(1, _translate("CustomProtocol", "Post Column Waste"))
        self.flowpath_combo_box.setItemText(2, _translate("CustomProtocol", "Fraction Column"))
        self.flowpath_combo_box.setItemText(3, _translate("CustomProtocol", "Flow Through Column"))
        self.valve_inp_combo_box.setItemText(0, _translate("CustomProtocol", "Load"))
        self.valve_inp_combo_box.setItemText(1, _translate("CustomProtocol", "Buffer"))
        self.port_combo_box.setItemText(0, _translate("CustomProtocol", "WASH"))
        self.port_combo_box.setItemText(1, _translate("CustomProtocol", "LOAD_BUFFER"))
        self.port_combo_box.setItemText(2, _translate("CustomProtocol", "ELUTION"))
        self.port_combo_box.setItemText(3, _translate("CustomProtocol", "BASE"))
        self.label_2.setText(_translate("CustomProtocol", "CV"))
        self.volume_val_lbl.setInputMask(_translate("CustomProtocol", "9999"))
        self.step_num.setText(_translate("CustomProtocol", "{}".format(step_no)))
        ## Add title for any new widgets above this line

    def _init_widget_actions(self):
        """Initialize on click actions for the combo box and slider present in the widget"""
        self.last_flowpath = 0
        self.volume_val_lbl.setText('{}'.format(1))
        self.volume_slider.valueChanged.connect(lambda: self.slider_changed(self.volume_slider.value(),
                                                    self.volume_val_lbl))
        self.valve_inp_combo_box.activated.connect(lambda: self.onSelectInput(self.valve_inp_combo_box.currentIndex(),
                                                self.port_combo_box))
        self.flowpath_combo_box.activated.connect(self.onSelectFlowPath)
        self.onSelectFlowPath(0)

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))

    def onSelectInput(self, cur_index, port):
        """Enable port selection if buffer is selected"""
        if cur_index == 1:
            port.setEnabled(True)
        else:
            port.setEnabled(False)

    def onSelectFlowPath(self, current_index):
        if self.last_flowpath != current_index:
            self.last_flowpath = current_index
            c_size = 50 if current_index == 3 else 1
            self.gui_controller.flowpathwayClicked(self.step_no, c_size)
            self.gui_controller.fractionCollectorUnsel(self.step_no)
            if current_index > 1:
                vol = int(self.volume_val_lbl.text())
                max_vol = self.gui_controller.okay_vol_checker(vol, c_size)
                if max_vol == -1:
                    # volume is okay
                    disp = self.gui_controller.fractionCollectorSel(self.step_no, vol, c_size)
                    self.frac_wdw = QtWidgets.QMainWindow()
                    self.frac_ui = Ui_FractionColumn(self.frac_wdw)
                    self.frac_wdw.show()
                    self.frac_ui.correct_frac_col_design()
                    self.frac_ui.display_selected(disp)
                    self.fraction_widgets_enabler(False)
                else:
                    # volume not available
                    self.gui_controller.vol_exceeds_msg(max_vol)
                    self.flowpath_combo_box.setCurrentIndex(0)
            else:
                self.fraction_widgets_enabler(True)
        
    def fraction_widgets_enabler(self, is_enabled):
        self.volume_val_lbl.setEnabled(is_enabled)
        self.volume_slider.setEnabled(is_enabled)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomProtocol = QtWidgets.QMainWindow()
    ui = Ui_CustomProtocol()
    ui.setupUi(CustomProtocol)
    CustomProtocol.show()
    sys.exit(app.exec_())
