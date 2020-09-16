from PyQt5 import QtCore, QtGui, QtWidgets
from fraction_col_gui import Ui_FractionColumn
from gui_controller import GUI_Controller
from os import chdir, path


class Ui_CustomProtocol(object):
    def __init__(self, CustomProtocol, simulator_process):
        self.CustomProtocol = CustomProtocol
        self.gui_controller = GUI_Controller()
        self.gui_controller.device_process = simulator_process
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
        self.add_step_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_step_btn.setFont(font)
        self.add_step_btn.setObjectName("add_step_btn")
        self.horizontalLayout_3.addWidget(self.add_step_btn)
        self.remove_step = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remove_step.setFont(font)
        self.remove_step.setObjectName("remove_step")
        self.horizontalLayout_3.addWidget(self.remove_step)
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
        self.cur_step_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cur_step_btn.sizePolicy().hasHeightForWidth())
        self.cur_step_btn.setSizePolicy(sizePolicy)
        self.cur_step_btn.setMinimumSize(QtCore.QSize(300, 25))
        self.cur_step_btn.setStyleSheet("QPushButton#cur_step_btn {border-radius:10;border-width: 2px; background-color: #3CB371; font-size:14px;}\n"
"QPushButton:disabled#cur_step_btn{background-color:#A9A9A9}")
        self.cur_step_btn.setObjectName("cur_step_btn")
        self.horizontalLayout_2.addWidget(self.cur_step_btn)
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
        self.log_output_txtbox = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_output_txtbox.sizePolicy().hasHeightForWidth())
        self.log_output_txtbox.setSizePolicy(sizePolicy)
        self.log_output_txtbox.setMinimumSize(QtCore.QSize(500, 0))
        self.log_output_txtbox.setObjectName("log_output_txtbox")
        self.verticalLayout_7.addWidget(self.log_output_txtbox)
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
        self.col_vol_combo_box.setItemText(0, _translate("CustomProtocol", "1 ml"))
        self.col_vol_combo_box.setItemText(1, _translate("CustomProtocol", "5 ml"))
        self.label_10.setText(_translate("CustomProtocol", "Repeat: "))
        self.rep_num_lbl.setText(_translate("CustomProtocol", "1"))
        self.add_step_btn.setText(_translate("CustomProtocol", "ADD"))
        self.remove_step.setText(_translate("CustomProtocol", "REMOVE"))
        self.label_9.setText(_translate("CustomProtocol", "Status:"))
        self.status_display_btn.setText(_translate("CustomProtocol", "Running"))
        self.label.setText(_translate("CustomProtocol", "Current Step:"))
        self.cur_step_btn.setText(_translate("CustomProtocol", "1"))
        self.start_btn.setText(_translate("CustomProtocol", "START"))
        self.pause_btn.setText(_translate("CustomProtocol", "PAUSE"))
        self.hold_btn.setText(_translate("CustomProtocol", "HOLD"))
        self.stop_btn.setText(_translate("CustomProtocol", "STOP"))
        self.close_btn.setText(_translate("CustomProtocol", "Close"))

    ###################
    # Event Handlers #
    ##################

    def initEvents(self):
        """Initializes all on click actions"""
        # counts the current step: Needed for adding and removing steps
        self.step_counter = -1
        # Contains the parent widget for a step
        # len(step_widgets) = number of steps
        self.step_widgets = []
        self.step_widget_objs = []
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

        # Logger initialized to display the steps
        self.log_update_timer = QtCore.QTimer()
        self.log_update_timer.timeout.connect(self.log_timer_handler)
        self.log_update_timer.start(1000)
        self.log_output_txtbox.setReadOnly(True)
        self.log_output = None

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.CustomProtocol.close()

    def onClickAddStep(self):
        """Creates a new widget to add the input parameters"""
        self.step_counter += 1
        self.step_widgets.append(QtWidgets.QWidget(self.scrollAreaWidgetContents))
        self.step_widget_objs.append(AddStep(self.step_widgets[self.step_counter], self.step_counter+1))
        self.verticalLayout_5.addWidget(self.step_widgets[self.step_counter])
        self.remove_step.setEnabled(True)

    def onClickRemoveStep(self):
        """Removes the last step that was added"""
        self.step_widgets[self.step_counter].setParent(None)
        self.step_widgets.pop()
        self.step_widget_objs.pop()
        self.step_counter -= 1
        if self.step_counter < 0:
                self.remove_step.setEnabled(False)

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))
    
    def _generate_run_parameters(self):
        """Generates an array of the run parameters

        Return
        ----------------------------------
        [[4, 1, 10],[None, 200, 0],[2, 100, 1],....]"""
        input_params = []
        col_size = 1 if self.col_vol_combo_box.currentIndex() == 0 else 5
        rep = int(self.rep_num_lbl.text())
        input_params.append([self.num_col_combo_box.currentIndex()+1, col_size, rep])
        for c in self.step_widget_objs:
            inp = []
            if c.port_combo_box.isEnabled():
                inp.append(c.port_combo_box.currentIndex())
            else:
                inp.append(None)
            inp.append(int(c.volume_val_lbl.text()))
            inp.append(c.flowpath_combo_box.currentIndex())
            input_params.append(inp)
        print(input_params)
        return input_params


    ## Action Button Event Handlers ##

    def _set_param_enable(self, is_enabled):
        """Enables/Disables all input parameters"""
        self.col_vol_combo_box.setEnabled(is_enabled)
        self.num_col_combo_box.setEnabled(is_enabled)
        self.rep_num_slider.setEnabled(is_enabled)
        for w in self.step_widgets:
            w.setEnabled(is_enabled)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """Either enables or disables the action buttons"""
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    def onClickStart(self):
        """"""
        self.gui_controller.areYouSureMsg('start')
        if self.gui_controller.is_sure:
            init_params = self._generate_run_parameters()
            self.gui_controller.is_sure = None
            self._set_actionbtn_enable(True, False)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            self.gui_controller.run_purification_script(False, init_params, 'self.fractions_selected')

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

    def onClickResume(self):
        """
        Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        """
        self._set_actionbtn_enable(True, False)
        self.gui_controller.resume_clicked()

    def onClickStop(self):
        """Signals the script that stop was clicked, to home the device"""
        self.gui_controller.areYouSureMsg('stop')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self._finish_protocol()
            self.gui_controller.stop_clicked()

    def _finish_protocol(self):
        self._set_actionbtn_enable(False, True)
        self.close_btn.setEnabled(True)
        self._set_param_enable(True)
        self.start_btn.disconnect()
        self.start_btn.setText('START')
        self.start_btn.clicked.connect(self.onClickStart)
        for w in self.step_widgets:
            w.setParent(None)
        self.step_widgets = []
        self.step_widget_objs = []
        self.step_counter = -1

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


class AddStep():
    def __init__(self, step_widget, step_no):
        """Implements the initialization and control of a single step widget
        A step widget is defined as the parent widget containing all the input 
        parameters needed to define a single step
        Parameters
        ---------------------------
        step_widget: Parent QtWidget object for the step
        step_no: The step that we are currently on
        """
        self.add_step_widget = step_widget
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
        self.port_combo_box.setItemText(0, _translate("CustomProtocol", "Wash"))
        self.port_combo_box.setItemText(1, _translate("CustomProtocol", "Load Buffer"))
        self.port_combo_box.setItemText(2, _translate("CustomProtocol", "Elution"))
        self.port_combo_box.setItemText(3, _translate("CustomProtocol", "Base"))
        self.label_2.setText(_translate("CustomProtocol", "ml"))
        self.volume_val_lbl.setInputMask(_translate("CustomProtocol", "9999"))
        self.step_num.setText(_translate("CustomProtocol", "{}".format(step_no)))
        ## Add title for any new widgets above this line

    def _init_widget_actions(self):
        """Initialize on click actions for the combo box and slider present in the widget"""
        self.volume_val_lbl.setText('{}'.format(self.volume_slider.value()))
        self.volume_slider.valueChanged.connect(lambda: self.slider_changed(self.volume_slider.value(),
                                                    self.volume_val_lbl))
        self.valve_inp_combo_box.activated.connect(lambda: self.onSelectInput(self.valve_inp_combo_box.currentIndex(),
                                                self.port_combo_box))
        self.flowpath_combo_box.activated.connect(lambda: self.onSelectFlowPath(self.flowpath_combo_box,
                                                        self.volume_slider, self.volume_val_lbl.text()))

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))

    def onSelectInput(self, cur_index, port):
        """Enable port selection if buffer is selected"""
        if cur_index == 1:
            port.setEnabled(True)
        else:
            port.setEnabled(False)

    def onSelectFlowPath(self, combobox, slider, vol):
        """Display fraction collector window with selected fractions depending on
        the flow path selected"""
        cur_index = combobox.currentIndex()
        #self.col_vol_combo_box.setEnabled(True)
        run = False
        if cur_index == 2:
                col_size = 1
                #col_size = 1 if self.col_vol_combo_box.currentIndex() == 0 else 5
                run = self._okayFracVol(vol, col_size)
                """
                if run:
                    self.col_vol_combo_box.setEnabled(False)
                else:
                    combobox.setCurrentIndex(0)
                """
        if cur_index == 3:
                col_size = None
                run = True
        if run:
            slider.setEnabled(False)
            self.frac_wdw = QtWidgets.QMainWindow()
            self.frac_ui = Ui_FractionColumn(self.frac_wdw, int(vol), col_size)
            self.frac_wdw.show()
            self.frac_ui.correct_frac_col_design()
            #self.fractions_selected[step_index] = 
            #self.frac_ui.select_frac_columns()
        else:
            slider.setEnabled(True)

    def _okayFracVol(self, vol, col_size):
        """Checks that the frac volume input does not exceed the total capacity"""
        max_vol = col_size*10
        if int(vol) > max_vol:
            msg = QtWidgets.QMessageBox()
            msg.setText('Total volume cannot exceed {} ml for fraction collector pathway'.format(max_vol))
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return False
        return True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CustomProtocol = QtWidgets.QMainWindow()
    ui = Ui_CustomProtocol()
    ui.setupUi(CustomProtocol)
    CustomProtocol.show()
    sys.exit(app.exec_())
