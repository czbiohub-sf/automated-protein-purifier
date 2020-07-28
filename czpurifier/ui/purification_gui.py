from PyQt5 import QtCore, QtGui, QtWidgets
from fraction_col_gui import Ui_FractionColumn
from os import chdir, path

class Ui_Purification(object):
    def __init__(self, Purification, gui_controller):
        """
        Contains the initialization of the purification tab
        """
        self.flowPathComboBox = []
        self.gui_controller = gui_controller
        self.is_sure = None
        self.initUI(Purification)

    def initUI(self, Purification):
        self.Purification = Purification
        self.Purification.setObjectName("Purification")
        self.Purification.setWindowModality(QtCore.Qt.ApplicationModal)
        self.Purification.resize(1128, 663)
        self.centralwidget = QtWidgets.QWidget(Purification)
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
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.num_col_lbl = QtWidgets.QLabel(self.centralwidget)
        self.num_col_lbl.setObjectName("num_col_lbl")
        self.horizontalLayout_13.addWidget(self.num_col_lbl)
        self.num_col_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.num_col_combo_box.setObjectName("num_col_combo_box")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.num_col_combo_box.addItem("")
        self.horizontalLayout_13.addWidget(self.num_col_combo_box)
        self.col_vol_lbl = QtWidgets.QLabel(self.centralwidget)
        self.col_vol_lbl.setObjectName("col_vol_lbl")
        self.horizontalLayout_13.addWidget(self.col_vol_lbl)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        """
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.colVol1_rdiobtn = QtWidgets.QRadioButton(self.centralwidget)
        self.colVol1_rdiobtn.setObjectName("colVol1_rdiobtn")
        self.verticalLayout_8.addWidget(self.colVol1_rdiobtn)
        self.colVol5_rdiobtn = QtWidgets.QRadioButton(self.centralwidget)
        self.colVol5_rdiobtn.setObjectName("colVol5_rdiobtn")
        self.verticalLayout_8.addWidget(self.colVol5_rdiobtn)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        """
        self.col_vol_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.col_vol_combo_box.setObjectName("num_col_combo_box")
        self.col_vol_combo_box.addItem("")
        self.col_vol_combo_box.addItem("")
        self.horizontalLayout_13.addWidget(self.col_vol_combo_box)

        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.equilibrate_btn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equilibrate_btn.sizePolicy().hasHeightForWidth())
        self.equilibrate_btn.setSizePolicy(sizePolicy)
        self.equilibrate_btn.setObjectName("equilibrate_btn")
        self.horizontalLayout_2.addWidget(self.equilibrate_btn)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.equilibrate_vol_lbl = QtWidgets.QLabel(self.centralwidget)
        self.equilibrate_vol_lbl.setObjectName("equilibrate_vol_lbl")
        self.verticalLayout_10.addWidget(self.equilibrate_vol_lbl)
        self.equilibriate_flowpath_lbl = QtWidgets.QLabel(self.centralwidget)
        self.equilibriate_flowpath_lbl.setObjectName("equilibriate_flowpath_lbl")
        self.verticalLayout_10.addWidget(self.equilibriate_flowpath_lbl)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.equil_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        self.equil_vol_val.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equil_vol_val.sizePolicy().hasHeightForWidth())
        self.equil_vol_val.setSizePolicy(sizePolicy)
        self.equil_vol_val.setMinimumSize(QtCore.QSize(50, 0))
        self.equil_vol_val.setMaximumSize(QtCore.QSize(60, 16777215))
        self.equil_vol_val.setObjectName("equil_vol_val")
        self.horizontalLayout_8.addWidget(self.equil_vol_val)
        self.equil_vol_unit = QtWidgets.QLabel(self.centralwidget)
        self.equil_vol_unit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.equil_vol_unit.setObjectName("equil_vol_unit")
        #self.equil_vol_unit.addItem("")
        #self.equil_vol_unit.addItem("")
        self.equil_vol_unit.setText("ml")
        self.horizontalLayout_8.addWidget(self.equil_vol_unit)
        self.verticalLayout_14.addLayout(self.horizontalLayout_8)
        self.equil_flowpath = QtWidgets.QComboBox(self.centralwidget)
        self.equil_flowpath.setMaximumSize(QtCore.QSize(200, 16777215))
        self.equil_flowpath.setObjectName("equil_flowpath")
        self.equil_flowpath.addItem("")
        self.equil_flowpath.addItem("")
        self.verticalLayout_14.addWidget(self.equil_flowpath)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.equilibriate_pbar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equilibriate_pbar.sizePolicy().hasHeightForWidth())
        self.equilibriate_pbar.setSizePolicy(sizePolicy)
        self.equilibriate_pbar.setMinimumSize(QtCore.QSize(150, 0))
        self.equilibriate_pbar.setProperty("value", 24)
        self.equilibriate_pbar.setObjectName("equilibriate_pbar")
        self.horizontalLayout_2.addWidget(self.equilibriate_pbar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.load_btn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy)
        self.load_btn.setMinimumSize(QtCore.QSize(107, 0))
        self.load_btn.setObjectName("load_btn")
        self.horizontalLayout_4.addWidget(self.load_btn)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.load_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        self.load_ph_lbl.setObjectName("load_ph_lbl")
        self.verticalLayout_11.addWidget(self.load_ph_lbl)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.load_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        self.load_vol_val.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_vol_val.sizePolicy().hasHeightForWidth())
        self.load_vol_val.setSizePolicy(sizePolicy)
        self.load_vol_val.setMaximumSize(QtCore.QSize(60, 16777215))
        self.load_vol_val.setObjectName("load_vol_val")
        self.horizontalLayout_9.addWidget(self.load_vol_val)
        self.load_vol_unit = QtWidgets.QLabel(self.centralwidget)
        self.load_vol_unit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.load_vol_unit.setObjectName("load_vol_unit")
        #self.load_vol_unit.addItem("")
        #self.load_vol_unit.addItem("")
        self.load_vol_unit.setText("ml")
        self.horizontalLayout_9.addWidget(self.load_vol_unit)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.load_flowpath = QtWidgets.QComboBox(self.centralwidget)
        self.load_flowpath.setObjectName("load_flowpath")
        self.load_flowpath.addItem("")
        self.load_flowpath.addItem("")
        self.load_flowpath.addItem("")
        self.verticalLayout_15.addWidget(self.load_flowpath)
        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.load_pbar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_pbar.sizePolicy().hasHeightForWidth())
        self.load_pbar.setSizePolicy(sizePolicy)
        self.load_pbar.setMinimumSize(QtCore.QSize(150, 0))
        self.load_pbar.setProperty("value", 24)
        self.load_pbar.setObjectName("load_pbar")
        self.horizontalLayout_4.addWidget(self.load_pbar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.wash_btn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wash_btn.sizePolicy().hasHeightForWidth())
        self.wash_btn.setSizePolicy(sizePolicy)
        self.wash_btn.setMinimumSize(QtCore.QSize(107, 0))
        self.wash_btn.setObjectName("wash_btn")
        self.horizontalLayout_5.addWidget(self.wash_btn)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 40, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.wash_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        self.wash_ph_lbl.setObjectName("wash_ph_lbl")
        self.verticalLayout_12.addWidget(self.wash_ph_lbl)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(104, 16777215))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wash_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        self.wash_vol_val.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.wash_vol_val.setMaximumSize(QtCore.QSize(60, 16777215))
        self.wash_vol_val.setObjectName("wash_vol_val")
        self.horizontalLayout_10.addWidget(self.wash_vol_val)
        self.wash_vol_unit = QtWidgets.QLabel(self.centralwidget)
        self.wash_vol_unit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.wash_vol_unit.setObjectName("wash_vol_unit")
        #self.wash_vol_unit.addItem("")
        #self.wash_vol_unit.addItem("")
        self.wash_vol_unit.setText("ml")
        self.horizontalLayout_10.addWidget(self.wash_vol_unit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.wash_flowpath = QtWidgets.QComboBox(self.centralwidget)
        self.wash_flowpath.setMaximumSize(QtCore.QSize(154, 16777215))
        self.wash_flowpath.setObjectName("wash_flowpath")
        self.wash_flowpath.addItem("")
        self.wash_flowpath.addItem("")
        self.wash_flowpath.addItem("")
        self.verticalLayout.addWidget(self.wash_flowpath)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.wash_pbar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wash_pbar.sizePolicy().hasHeightForWidth())
        self.wash_pbar.setSizePolicy(sizePolicy)
        self.wash_pbar.setMinimumSize(QtCore.QSize(150, 0))
        self.wash_pbar.setProperty("value", 24)
        self.wash_pbar.setObjectName("wash_pbar")
        self.horizontalLayout_5.addWidget(self.wash_pbar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.elute_btn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elute_btn.sizePolicy().hasHeightForWidth())
        self.elute_btn.setSizePolicy(sizePolicy)
        self.elute_btn.setMinimumSize(QtCore.QSize(107, 0))
        self.elute_btn.setObjectName("elute_btn")
        self.horizontalLayout_3.addWidget(self.elute_btn)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 40, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.elute_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        self.elute_ph_lbl.setObjectName("elute_ph_lbl")
        self.verticalLayout_13.addWidget(self.elute_ph_lbl)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.elute_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        self.elute_vol_val.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.elute_vol_val.setMaximumSize(QtCore.QSize(60, 16777215))
        self.elute_vol_val.setObjectName("elute_vol_val")
        self.horizontalLayout_11.addWidget(self.elute_vol_val)
        self.elute_vol_unit = QtWidgets.QLabel(self.centralwidget)
        self.elute_vol_unit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.elute_vol_unit.setObjectName("elute_vol_unit")
        self.elute_vol_unit.setText("ml")
        #self.elute_vol_unit.addItem("")
        #self.elute_vol_unit.addItem("")
        self.horizontalLayout_11.addWidget(self.elute_vol_unit)
        self.verticalLayout_17.addLayout(self.horizontalLayout_11)
        self.elute_flowpath = QtWidgets.QComboBox(self.centralwidget)
        self.elute_flowpath.setMaximumSize(QtCore.QSize(154, 16777215))
        self.elute_flowpath.setObjectName("elute_flowpath")
        self.elute_flowpath.addItem("")
        self.elute_flowpath.addItem("")
        self.elute_flowpath.addItem("")
        self.verticalLayout_17.addWidget(self.elute_flowpath)
        self.horizontalLayout_3.addLayout(self.verticalLayout_17)
        self.elute_pbar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elute_pbar.sizePolicy().hasHeightForWidth())
        self.elute_pbar.setSizePolicy(sizePolicy)
        self.elute_pbar.setMinimumSize(QtCore.QSize(150, 0))
        self.elute_pbar.setProperty("value", 24)
        self.elute_pbar.setObjectName("elute_pbar")
        self.horizontalLayout_3.addWidget(self.elute_pbar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progress_model_placeholder = QtWidgets.QTextBrowser(self.centralwidget)
        self.progress_model_placeholder.setObjectName("progress_model_placeholder")
        self.verticalLayout_7.addWidget(self.progress_model_placeholder)
        self.current_step_log_lbl = QtWidgets.QTextEdit(self.centralwidget)
        self.current_step_log_lbl.setObjectName("current_step_log_lbl")
        self.verticalLayout_7.addWidget(self.current_step_log_lbl)
        self.estimated_time_remaining_lbl = QtWidgets.QLabel(self.centralwidget)
        self.estimated_time_remaining_lbl.setObjectName("estimated_time_remaining_lbl")
        self.verticalLayout_7.addWidget(self.estimated_time_remaining_lbl)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout.addWidget(self.pause_btn)
        self.hold_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hold_btn.setObjectName("hold_btn")
        self.horizontalLayout.addWidget(self.hold_btn)
        self.skip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.skip_btn.setObjectName("skip_btn")
        self.horizontalLayout.addWidget(self.skip_btn)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_7.addWidget(self.close_btn)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.Purification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.Purification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 22))
        self.menubar.setObjectName("menubar")
        self.Purification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.Purification)
        self.statusbar.setObjectName("statusbar")
        self.Purification.setStatusBar(self.statusbar)
        
        self.initEvents()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Purification)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Purification.setWindowTitle(_translate("Purification", "Purification"))
        self.num_col_lbl.setText(_translate("Purification", "Number of Columns: "))
        self.num_col_combo_box.setItemText(0, _translate("Purification", "1"))
        self.num_col_combo_box.setItemText(1, _translate("Purification", "2"))
        self.num_col_combo_box.setItemText(2, _translate("Purification", "3"))
        self.num_col_combo_box.setItemText(3, _translate("Purification", "4"))
        self.col_vol_lbl.setText(_translate("Purification", "Column Volume: "))
        self.col_vol_combo_box.setItemText(0, _translate("Purification", "1 ml"))
        self.col_vol_combo_box.setItemText(1, _translate("Purification", "5 ml"))
        self.equilibrate_btn.setText(_translate("Purification", "  Equilibrate          "))
        self.equilibrate_vol_lbl.setText(_translate("Purification", "Volume:"))
        self.equilibriate_flowpath_lbl.setText(_translate("Purification", "Flow Path:"))
        #self.equil_vol_unit.setItemText(0, _translate("Purification", "ml"))
        #self.equil_vol_unit.setItemText(1, _translate("Purification", "CV"))
        self.equil_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.equil_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_btn.setText(_translate("Purification", "  Load    "))
        self.load_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_3.setText(_translate("Purification", "Flow Path:"))
        #self.load_vol_unit.setItemText(0, _translate("Purification", "ml"))
        #self.load_vol_unit.setItemText(1, _translate("Purification", "CV"))
        self.load_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.load_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.wash_btn.setText(_translate("Purification", "  Wash"))
        self.wash_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_4.setText(_translate("Purification", "Flow Path:"))
        #self.wash_vol_unit.setItemText(0, _translate("Purification", "ml"))
        #self.wash_vol_unit.setItemText(1, _translate("Purification", "CV"))
        self.wash_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.wash_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.wash_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.elute_btn.setText(_translate("Purification", "  Elute"))
        self.elute_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_5.setText(_translate("Purification", "Flow Path:"))
        #self.elute_vol_unit.setItemText(0, _translate("Purification", "ml"))
        #self.elute_vol_unit.setItemText(1, _translate("Purification", "CV"))
        self.elute_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.elute_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.elute_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.progress_model_placeholder.setHtml(_translate("Purification", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;Progress Model&gt;</p></body></html>"))
        #self.current_step_log_lbl.setText(_translate("Purification", "Current Step: <this is the current step>"))
        self.estimated_time_remaining_lbl.setText(_translate("Purification", "Estimated Time Remaining: <..> min(s)"))
        self.start_btn.setText(_translate("Purification", "Start"))
        self.pause_btn.setText(_translate("Purification", "Pause"))
        self.hold_btn.setText(_translate("Purification", "Hold"))
        self.skip_btn.setText(_translate("Purification", "Skip To Next"))
        self.stop_btn.setText(_translate("Purification", "Stop"))
        self.close_btn.setText(_translate("Purification", "Close"))

    def initEvents(self):
        """
        Initializes all on click actions
        """
        # widget: is_text
        self.input_param = {self.num_col_combo_box: False, self.col_vol_combo_box: False,
                            self.equil_vol_val: True, self.equil_flowpath: False, 
                            self.load_vol_val: True, self.load_flowpath: False,
                            self.wash_vol_val: True, self.wash_flowpath: False,
                            self.elute_vol_val: True, self.elute_flowpath: False}
        self._set_actionbtn_enable(False, True)
        self.setDefaultParam()
        self._reset_pbar()

        self.equil_flowpath.activated.connect(lambda: self.onClickFlowPath(0))
        self.load_flowpath.activated.connect(lambda: self.onClickFlowPath(1))
        self.wash_flowpath.activated.connect(lambda: self.onClickFlowPath(2))
        self.elute_flowpath.activated.connect(lambda: self.onClickFlowPath(3))
        self.flowPathComboBox = [self.equil_flowpath, self.load_flowpath, self.wash_flowpath, self.elute_flowpath]
        self.close_btn.clicked.connect(self.onClickClose)

        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.skip_btn.clicked.connect(self.onClickSkip)
        self.stop_btn.clicked.connect(self.onClickStop)

        self.display_log()

    def onClickFlowPath(self, step_index):
        curIndex = self.flowPathComboBox[step_index].currentIndex()
        if curIndex == 2:
            self.frac_wdw = QtWidgets.QMainWindow()
            self.frac_ui = Ui_FractionColumn(self.frac_wdw)
            self.frac_wdw.show()

    def onClickClose(self):
        self.Purification.close()
    
    def setDefaultParam(self):
        self.num_col_combo_box.setCurrentIndex(self.gui_controller.default_param[0]-1)
        if self.gui_controller.default_param[1] == 1:
            self.col_vol_combo_box.setCurrentIndex(0)
        else:
            self.col_vol_combo_box.setCurrentIndex(1)
        self.equil_vol_val.setText(str(self.gui_controller.default_param[2]))
        self.load_vol_val.setText(str(self.gui_controller.default_param[3]))
        self.wash_vol_val.setText(str(self.gui_controller.default_param[4]))
        self.elute_vol_val.setText(str(self.gui_controller.default_param[5]))
    
    def onClickStart(self):
        """
        1. Pop up to confirm you want to start
        2. Enable all other action buttons
        3. Disable everything that can be edited
        4. Update the json file with all the run cmds
        5. Run the process
        """
        self.areYouSureMsg('start')
        if self.is_sure:
            self.is_sure = None
            self._set_actionbtn_enable(True, False)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            self.gui_controller.run_purification_script(self._init_run_param())
        else:
            self.current_step_log_lbl.verticalScrollBar().setValue(self.current_step_log_lbl.verticalScrollBar().maximum())
    
    def _init_run_param(self):
        """
        Parse through all the input parameters and store
        in an array to pass to controller to update json file
        """
        run_param = []
        for widget in self.input_param:
            if self.input_param[widget]:
                # Handle text inputs
                run_param.append(int(widget.text()))
            else:
                # Handle combo box
                run_param.append(widget.currentIndex()+1)
        run_param[1] = 5 if run_param[1] == 2 else run_param[1]
        return run_param
    
    def _set_param_enable(self, state):
        """
        Enables/Disables all the widgets that allow initializing input parameters
        """
        for widget in self.input_param:
            widget.setEnabled(state)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """
        Either enables or disables the action buttons
        """
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.skip_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
       
        self.start_btn.setEnabled(start_state)
    
    def _reset_pbar(self):
        """
        Enable/Disable all the progress bars
        """
        self.equilibriate_pbar.setValue(0)
        self.load_pbar.setValue(0)
        self.wash_pbar.setValue(0)
        self.elute_pbar.setValue(0)

    def onClickPauseHold(self, is_pause):
        """
        Enables Start button to resume
        Calls pause_clicked/hold that sends a pause/hold signal to 
        the process running the purification
        """
        msg = 'pause' if is_pause else 'hold'
        self.areYouSureMsg(msg)
        if self.is_sure:
            self.is_sure = None
            self._set_actionbtn_enable(False, True)
            self.stop_btn.setEnabled(True)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.start_btn.disconnect()
            self.start_btn.setText('Resume')
            self.start_btn.clicked.connect(self.onClickResume)

    def onClickSkip(self):
        self.areYouSureMsg('skip to next step')
        if self.is_sure:
            self.is_sure = None
            self._set_actionbtn_enable(False, True)
            self.stop_btn.setEnabled(True)

    def onClickStop(self):
        self.areYouSureMsg('stop')
        if self.is_sure:
            self.is_sure = None
            self._set_actionbtn_enable(False, True)
            self.close_btn.setEnabled(True)
            self._set_param_enable(True)
    
    def onClickResume(self):
        """
        Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        """
        self._set_actionbtn_enable(True, False)
        self.gui_controller.resume_pause_clicked()
        
    
    def areYouSureMsg(self, action):
        """
        Confirms whether or not the user meant to click an action button
        """
        msg = QtWidgets.QMessageBox()
        msg.setText('Are you sure you want to {}'.format(action))
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec()
    
    def msgbtn(self, i):
        """ Returns the result from the are you sure pop up"""
        self.is_sure = True if i.text() == 'OK' else False

    def display_log(self):
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'r') as f:
            self.current_step_log_lbl.setText(f.read())
