from PyQt5 import QtCore, QtGui, QtWidgets
from fraction_col_gui import Ui_FractionColumn
from os import chdir, path, getpid, kill
from signal import signal, SIGUSR2, SIGUSR1
from time import sleep

class Ui_Purification(object):
    def __init__(self, Purification, gui_controller):
        """
        Contains the initialization and functionality of the purification tab
        """
        signal(SIGUSR2, self.purificationComplete)
        signal(SIGUSR1, self.startProgressBar)
        self.gui_controller = gui_controller
        self.is_sure = None
        self.frac_size = None
        self.Purification = Purification
        self.setupUi(self.Purification)
        self.initEvents()

    ###########################
    # Desinger Generated Code #
    ###########################

    def setupUi(self, Purification):
        Purification.setObjectName("Purification")
        Purification.setWindowModality(QtCore.Qt.ApplicationModal)
        Purification.resize(1440, 775)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.equilibrate_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equilibrate_lbl.sizePolicy().hasHeightForWidth())
        self.equilibrate_lbl.setSizePolicy(sizePolicy)
        self.equilibrate_lbl.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.equilibrate_lbl.setFont(font)
        self.equilibrate_lbl.setObjectName("equilibrate_lbl")
        self.horizontalLayout_2.addWidget(self.equilibrate_lbl)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.equilibrate_vol_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equilibrate_vol_lbl.sizePolicy().hasHeightForWidth())
        self.equilibrate_vol_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equilibrate_vol_lbl.setFont(font)
        self.equilibrate_vol_lbl.setObjectName("equilibrate_vol_lbl")
        self.verticalLayout_10.addWidget(self.equilibrate_vol_lbl)
        self.equilibriate_flowpath_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equilibriate_flowpath_lbl.sizePolicy().hasHeightForWidth())
        self.equilibriate_flowpath_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equilibriate_flowpath_lbl.setFont(font)
        self.equilibriate_flowpath_lbl.setObjectName("equilibriate_flowpath_lbl")
        self.verticalLayout_10.addWidget(self.equilibriate_flowpath_lbl)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.equil_vol_slider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equil_vol_slider.sizePolicy().hasHeightForWidth())
        self.equil_vol_slider.setSizePolicy(sizePolicy)
        self.equil_vol_slider.setMinimumSize(QtCore.QSize(0, 0))
        self.equil_vol_slider.setMinimum(0)
        self.equil_vol_slider.setMaximum(200)
        self.equil_vol_slider.setOrientation(QtCore.Qt.Horizontal)
        self.equil_vol_slider.setObjectName("equil_vol_slider")
        self.horizontalLayout_8.addWidget(self.equil_vol_slider)
        self.equil_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equil_vol_val.sizePolicy().hasHeightForWidth())
        self.equil_vol_val.setSizePolicy(sizePolicy)
        self.equil_vol_val.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equil_vol_val.setFont(font)
        self.equil_vol_val.setText("")
        self.equil_vol_val.setMaxLength(5)
        self.equil_vol_val.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.equil_vol_val.setObjectName("equil_vol_val")
        self.horizontalLayout_8.addWidget(self.equil_vol_val)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.verticalLayout_14.addLayout(self.horizontalLayout_8)
        self.equil_flowpath = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equil_flowpath.setFont(font)
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
        self.equilibriate_pbar.setMinimumSize(QtCore.QSize(200, 0))
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
        self.load_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_lbl.sizePolicy().hasHeightForWidth())
        self.load_lbl.setSizePolicy(sizePolicy)
        self.load_lbl.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_lbl.setFont(font)
        self.load_lbl.setObjectName("load_lbl")
        self.horizontalLayout_4.addWidget(self.load_lbl)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.load_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.load_ph_lbl.setFont(font)
        self.load_ph_lbl.setObjectName("load_ph_lbl")
        self.verticalLayout_11.addWidget(self.load_ph_lbl)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.load_vol_slider = QtWidgets.QSlider(self.centralwidget)
        self.load_vol_slider.setMaximum(200)
        self.load_vol_slider.setOrientation(QtCore.Qt.Horizontal)
        self.load_vol_slider.setObjectName("load_vol_slider")
        self.horizontalLayout_9.addWidget(self.load_vol_slider)
        self.load_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_vol_val.sizePolicy().hasHeightForWidth())
        self.load_vol_val.setSizePolicy(sizePolicy)
        self.load_vol_val.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.load_vol_val.setFont(font)
        self.load_vol_val.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.load_vol_val.setObjectName("load_vol_val")
        self.horizontalLayout_9.addWidget(self.load_vol_val)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.load_flowpath = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.load_flowpath.setFont(font)
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
        self.load_pbar.setMinimumSize(QtCore.QSize(200, 0))
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
        self.wash_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wash_lbl.sizePolicy().hasHeightForWidth())
        self.wash_lbl.setSizePolicy(sizePolicy)
        self.wash_lbl.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wash_lbl.setFont(font)
        self.wash_lbl.setObjectName("wash_lbl")
        self.horizontalLayout_5.addWidget(self.wash_lbl)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.wash_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wash_ph_lbl.setFont(font)
        self.wash_ph_lbl.setObjectName("wash_ph_lbl")
        self.verticalLayout_12.addWidget(self.wash_ph_lbl)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(104, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wash_vol_slider = QtWidgets.QSlider(self.centralwidget)
        self.wash_vol_slider.setMaximum(200)
        self.wash_vol_slider.setOrientation(QtCore.Qt.Horizontal)
        self.wash_vol_slider.setObjectName("wash_vol_slider")
        self.horizontalLayout_10.addWidget(self.wash_vol_slider)
        self.wash_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wash_vol_val.sizePolicy().hasHeightForWidth())
        self.wash_vol_val.setSizePolicy(sizePolicy)
        self.wash_vol_val.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wash_vol_val.setFont(font)
        self.wash_vol_val.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wash_vol_val.setObjectName("wash_vol_val")
        self.horizontalLayout_10.addWidget(self.wash_vol_val)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.wash_flowpath = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wash_flowpath.setFont(font)
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
        self.wash_pbar.setMinimumSize(QtCore.QSize(200, 0))
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
        self.elute_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elute_lbl.sizePolicy().hasHeightForWidth())
        self.elute_lbl.setSizePolicy(sizePolicy)
        self.elute_lbl.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.elute_lbl.setFont(font)
        self.elute_lbl.setObjectName("elute_lbl")
        self.horizontalLayout_3.addWidget(self.elute_lbl)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.elute_ph_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.elute_ph_lbl.setFont(font)
        self.elute_ph_lbl.setObjectName("elute_ph_lbl")
        self.verticalLayout_13.addWidget(self.elute_ph_lbl)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.elute_vol_slider = QtWidgets.QSlider(self.centralwidget)
        self.elute_vol_slider.setOrientation(QtCore.Qt.Horizontal)
        self.elute_vol_slider.setObjectName("elute_vol_slider")
        self.horizontalLayout_11.addWidget(self.elute_vol_slider)
        self.elute_vol_val = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elute_vol_val.sizePolicy().hasHeightForWidth())
        self.elute_vol_val.setSizePolicy(sizePolicy)
        self.elute_vol_val.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.elute_vol_val.setFont(font)
        self.elute_vol_val.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.elute_vol_val.setObjectName("elute_vol_val")
        self.horizontalLayout_11.addWidget(self.elute_vol_val)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.verticalLayout_17.addLayout(self.horizontalLayout_11)
        self.elute_flowpath = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.elute_flowpath.setFont(font)
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
        self.elute_pbar.setMinimumSize(QtCore.QSize(200, 0))
        self.elute_pbar.setProperty("value", 24)
        self.elute_pbar.setObjectName("elute_pbar")
        self.horizontalLayout_3.addWidget(self.elute_pbar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.current_step_display_btn = QtWidgets.QPushButton(self.centralwidget)
        self.current_step_display_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.current_step_display_btn.setStyleSheet("QPushButton#current_step_display_btn {border-radius:10;border-width: 2px; background-color: #3CB371; font-size:18px;}\n"
"QPushButton:disabled#current_step_display_btn{background-color:#A9A9A9}")
        self.current_step_display_btn.setObjectName("current_step_display_btn")
        self.horizontalLayout_15.addWidget(self.current_step_display_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.status_display_btn = QtWidgets.QPushButton(self.centralwidget)
        self.status_display_btn.setEnabled(True)
        self.status_display_btn.setMinimumSize(QtCore.QSize(392, 25))
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
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.skip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.skip_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.skip_btn.setStyleSheet("QPushButton#skip_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}\n"
"QPushButton:pressed#skip_btn{background-color:#A9A9A9}")
        self.skip_btn.setObjectName("skip_btn")
        self.horizontalLayout.addWidget(self.skip_btn)
        spacerItem5 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
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
        self.horizontalLayout_12.addWidget(self.stop_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_7.addWidget(self.close_btn)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        Purification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Purification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        Purification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Purification)
        self.statusbar.setObjectName("statusbar")
        Purification.setStatusBar(self.statusbar)

        self.retranslateUi(Purification)
        QtCore.QMetaObject.connectSlotsByName(Purification)

    def retranslateUi(self, Purification):
        _translate = QtCore.QCoreApplication.translate
        Purification.setWindowTitle(_translate("Purification", "Purification"))
        self.num_col_lbl.setText(_translate("Purification", "Number of Columns: "))
        self.num_col_combo_box.setItemText(0, _translate("Purification", "1"))
        self.num_col_combo_box.setItemText(1, _translate("Purification", "2"))
        self.num_col_combo_box.setItemText(2, _translate("Purification", "3"))
        self.num_col_combo_box.setItemText(3, _translate("Purification", "4"))
        self.col_vol_lbl.setText(_translate("Purification", "Column Volume: "))
        self.col_vol_combo_box.setItemText(0, _translate("Purification", "1 ml"))
        self.col_vol_combo_box.setItemText(1, _translate("Purification", "5 ml"))
        self.equilibrate_lbl.setText(_translate("Purification", "Equilibrate"))
        self.equilibrate_vol_lbl.setText(_translate("Purification", "Volume:"))
        self.equilibriate_flowpath_lbl.setText(_translate("Purification", "Flow Path:"))
        self.equil_vol_val.setInputMask(_translate("Purification", "99999"))
        self.label.setText(_translate("Purification", "ml"))
        self.equil_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.equil_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_lbl.setText(_translate("Purification", "Load"))
        self.load_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_3.setText(_translate("Purification", "Flow Path:"))
        self.load_vol_val.setInputMask(_translate("Purification", "99999"))
        self.label_2.setText(_translate("Purification", "ml"))
        self.load_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.load_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.wash_lbl.setText(_translate("Purification", "Wash"))
        self.wash_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_4.setText(_translate("Purification", "Flow Path:"))
        self.wash_vol_val.setInputMask(_translate("Purification", "99999"))
        self.label_6.setText(_translate("Purification", "ml"))
        self.wash_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.wash_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.wash_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.elute_lbl.setText(_translate("Purification", "Elute"))
        self.elute_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_5.setText(_translate("Purification", "Flow Path:"))
        self.elute_vol_val.setInputMask(_translate("Purification", "99999"))
        self.label_7.setText(_translate("Purification", "ml"))
        self.elute_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.elute_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.elute_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.label_8.setText(_translate("Purification", "Current Step:"))
        self.current_step_display_btn.setText(_translate("Purification", "--"))
        self.label_9.setText(_translate("Purification", "Status:"))
        self.status_display_btn.setText(_translate("Purification", "--"))
        self.estimated_time_remaining_lbl.setText(_translate("Purification", "Total Estimated Time: <..> min(s)"))
        self.start_btn.setText(_translate("Purification", "START"))
        self.pause_btn.setText(_translate("Purification", "PAUSE"))
        self.hold_btn.setText(_translate("Purification", "HOLD"))
        self.skip_btn.setText(_translate("Purification", "SKIP TO NEXT"))
        self.stop_btn.setText(_translate("Purification", "STOP"))
        self.close_btn.setText(_translate("Purification", "Close"))

    ###################
    # Event Handlers #
    ##################

    ## Initializing Event Handlers ##

    def initEvents(self):
        """Initializes all on click actions"""
        self.input_param = {self.num_col_combo_box: False, self.col_vol_combo_box: False,
                            self.equil_vol_val: True, self.equil_flowpath: False, 
                            self.load_vol_val: True, self.load_flowpath: False,
                            self.wash_vol_val: True, self.wash_flowpath: False,
                            self.elute_vol_val: True, self.elute_flowpath: False}
        self.fractions_selected = [None]*4
        self._set_actionbtn_enable(False, True)
        self.col_vol_combo_box.activated.connect(self.onClickFractionSize)
        self.setDefaultParam()
        self.pbars = [self.equilibriate_pbar, self.load_pbar, self.wash_pbar, self.elute_pbar]
        self._reset_pbar()

        self.vol_vals = [self.equil_vol_val, self.load_vol_val, self.wash_vol_val, self.elute_vol_val]
        self.vol_sliders = [self.equil_vol_slider, self.load_vol_slider, self.wash_vol_slider, self.elute_vol_slider]
        self.equil_flowpath.activated.connect(lambda: self.onClickFlowPath(self.equil_flowpath, 0))
        self.load_flowpath.activated.connect(lambda: self.onClickFlowPath(self.load_flowpath, 1))
        self.wash_flowpath.activated.connect(lambda: self.onClickFlowPath(self.wash_flowpath, 2))
        self.elute_flowpath.activated.connect(lambda: self.onClickFlowPath(self.elute_flowpath, 3))
        
        self.close_btn.clicked.connect(self.onClickClose)
        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.skip_btn.clicked.connect(self.onClickSkip)
        self.stop_btn.clicked.connect(self.onClickStop)

        self.equil_vol_slider.valueChanged.connect(lambda: self.slider_changed(self.equil_vol_slider.value(),
                                                    self.equil_vol_val))
        self.load_vol_slider.valueChanged.connect(lambda: self.slider_changed(self.load_vol_slider.value(),
                                                    self.load_vol_val))
        self.wash_vol_slider.valueChanged.connect(lambda: self.slider_changed(self.wash_vol_slider.value(),
                                                    self.wash_vol_val))
        self.elute_vol_slider.valueChanged.connect(lambda: self.slider_changed(self.elute_vol_slider.value(),
                                                    self.elute_vol_val))
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)

        self.status_display_color_running = '#3CB371'
        self.status_display_color_halt = '#FFFF66'
        self.status_display_stylsheet = '{}'.format("QPushButton#status_display_btn{{"
                                        "border-radius:10;"
                                        "border-width: 2px;"
                                        "background-color: {0};"
                                        "font-size:14px;}}\n"
                                        "QPushButton:disabled#status_display_btn{{"
                                        "background-color:#A9A9A9}}")
        self.estimated_time = None
        self.timer_index = None
        # timer event handler called every 1s
        self._time_per_update = 1000
        self._timer_on_flag = False
        self.timer_counter = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress_bar_handler)

        self.log_update_timer = QtCore.QTimer()
        self.log_update_timer.timeout.connect(self.log_timer_handler)
        self.log_update_timer.start(self._time_per_update)
        self.log_output_txtbox.setReadOnly(True)
        self.log_output = None

    def setDefaultParam(self):
        """Sets the default input parameters that are on the json file"""
        self.num_col_combo_box.setCurrentIndex(self.gui_controller.default_param[0]-1)
        if self.gui_controller.default_param[1] == 1:
            self.col_vol_combo_box.setCurrentIndex(0)
            self.elute_vol_slider.setMaximum(10)
            self.frac_size = 1
        else:
            self.col_vol_combo_box.setCurrentIndex(1)
            self.elute_vol_slider.setMaximum(50)
            self.frac_size = 5
        self.equil_vol_val.setText(str(self.gui_controller.default_param[2]))
        self.load_vol_val.setText(str(self.gui_controller.default_param[3]))
        self.wash_vol_val.setText(str(self.gui_controller.default_param[4]))
        self.elute_vol_val.setText(str(self.gui_controller.default_param[5]))
        self.equil_vol_slider.setSliderPosition(self.gui_controller.default_param[2])
        self.load_vol_slider.setSliderPosition(self.gui_controller.default_param[3])
        self.wash_vol_slider.setSliderPosition(self.gui_controller.default_param[4])
        self.elute_vol_slider.setSliderPosition(self.gui_controller.default_param[5])
    
    def purificationComplete(self, signalNumber, frame):
        """Handler for SIGUSR2. Prepares UI for another purification protocol"""
        self._finish_protocol()
    
    def startProgressBar(self, signalNumber, frame):
        """Handler for SIGUSR1. Starts the progress bar sequence"""
        self.timer_index = 0
        self._set_actionbtn_enable(True, False)
        self.current_step_display_btn.setText('Equilibrate')
        self._timer_on_flag = True
        self.timer.start(self._time_per_update)

    ## Input Parameter Widget Actions ##

    def onClickFractionSize(self):
        """Update the max vol allowed on elute slider based on fraction size"""
        curIndex = self.col_vol_combo_box.currentIndex()
        if curIndex == 0:
            self.elute_vol_slider.setMaximum(10)
            self.frac_size = 1
        else:
            self.elute_vol_slider.setMaximum(50)
            self.frac_size = 5

    def onClickFlowPath(self, flow_path_combo, step_index):
        """If the selected flow path is fraction column:
            1. Confirm that fraction column should be selected for the following total vol
            2. Display the fraction column window with the fractions selected
        Parameters
        ---------------------------------------
        flow_path_combo: The combobox object of the current flow path selected
        step_index: The index of the step, used to determine whether to use fraction/flow column
        and which text box to use to get the volume to flow
        """
        curIndex = flow_path_combo.currentIndex()
        col_size = self.frac_size if step_index == 3 else None
        if curIndex == 2 and self._okayFracVol(self.vol_vals[step_index].text(), col_size):
            self.vol_vals[step_index].setEnabled(False)
            self.vol_sliders[step_index].setEnabled(False)
            self.load_vol_slider.setEnabled(False)
            self.frac_wdw = QtWidgets.QMainWindow()
            self.frac_ui = Ui_FractionColumn(self.frac_wdw, int(self.vol_vals[step_index].text()), col_size)
            self.frac_wdw.show()
            self.frac_ui.correct_frac_col_design()
            self.fractions_selected[step_index] = self.frac_ui.select_frac_columns()
            if step_index == 3:
                self.col_vol_combo_box.setEnabled(False)
        else:
            self.vol_vals[step_index].setEnabled(True)
            self.vol_sliders[step_index].setEnabled(True)
            self.col_vol_combo_box.setEnabled(True)

    def _okayFracVol(self, vol, col_size = None):
        """
        Checks that the frac volume input does not exceed the total capacity

        Parameters
        ------------------------------------
        vol: The volume going into the fraction/flow through column
        col_size: None = Volume flowing through flow through column (fixed max = 200ml)
        Else 1 or 5 to indicate the size of the fraction columns
        """
        max_vol = 200 if col_size is None else col_size*10
        if int(vol) > max_vol:
            msg = QtWidgets.QMessageBox()
            msg.setText('Total volume cannot exceed {} ml for fraction collector pathway'.format(max_vol))
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec()
            return False
        return True

    def slider_changed(self, value, lbl):
        """Updates text label beside the slider when slider is moved"""
        lbl.setText('{}'.format(value))

    def _init_run_param(self):
        """Parse through all the input parameters and store
        in an array to pass to controller to run purification"""
        run_param = []
        for widget in self.input_param:
            if self.input_param[widget]:
                # Handle text inputs
                run_param.append(int(widget.text()))
            else:
                # Handle combo box
                run_param.append(widget.currentIndex())
        run_param[0] = run_param[0] + 1
        run_param[1] = 5 if run_param[1] == 1 else 1
        return run_param

    ## Enable/Disable Widgets On GUI ##

    def _set_param_enable(self, state):
        """Enables/Disables all the widgets that allow initializing input parameters"""
        for widget in self.input_param:
            widget.setEnabled(state)
        self.equil_vol_slider.setEnabled(state)
        self.load_vol_slider.setEnabled(state)
        self.wash_vol_slider.setEnabled(state)
        self.elute_vol_slider.setEnabled(state)
        self.label.setEnabled(state)
        self.label_2.setEnabled(state)
        self.label_6.setEnabled(state)
        self.label_7.setEnabled(state)
    
    def _set_actionbtn_enable(self, halt_state, start_state):
        """Either enables or disables the action buttons"""
        self.pause_btn.setEnabled(halt_state)
        self.hold_btn.setEnabled(halt_state)
        self.skip_btn.setEnabled(halt_state)
        self.stop_btn.setEnabled(halt_state)
        self.start_btn.setEnabled(start_state)

    def _reset_pbar(self):
        """Reset all the progress bars"""
        for pbar in self.pbars:
            pbar.setValue(0)

    ## Action Buttons Event Handlers ##

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.log_update_timer.stop()
        self.Purification.close()
    
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
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            init_params = self._init_run_param()
            self.estimated_time = self.gui_controller.calc_step_times(init_params, self.fractions_selected)
            self.estimated_time_remaining_lbl.setText('Estimated Time: {} min(s)'.format(sum(self.estimated_time)/60))
            self.current_step_display_btn.setEnabled(True)
            self.current_step_display_btn.setText('Setup And Purging Bubbles')
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.gui_controller.run_purification_script(init_params, self.fractions_selected)

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
            self._timer_on_flag = False
            self.timer.stop()
            self._set_actionbtn_enable(False, True)
            self.stop_btn.setEnabled(True)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(self.status_display_stylsheet.format(self.status_display_color_halt))
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.onClickResume)

    def onClickResume(self):
        """
        Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        """
        self._set_actionbtn_enable(True, False)
        self._timer_on_flag = True
        self.timer.start(self._time_per_update)
        self.status_display_btn.setStyleSheet(self.status_display_stylsheet.format(self.status_display_color_running))
        self.status_display_btn.setText('running')
        self.gui_controller.resume_clicked()

    def onClickSkip(self):
        """Stops pumping and goes to the next step"""
        self.areYouSureMsg('skip to next step')
        if self.is_sure:
            self.is_sure = None
            self.timer_index +=1
            self.timer_counter = 0
            self._update_current_step()
            self.gui_controller.skip_clicked()

    def onClickStop(self):
        """Signals the script that stop was clicked, to home the device"""
        self.areYouSureMsg('stop')
        if self.is_sure:
            self.is_sure = None
            self._finish_protocol()
            self.current_step_display_btn.setText('STOPPED')
            self.gui_controller.stop_clicked()
    
    def _finish_protocol(self):
        self._set_actionbtn_enable(False, True)
        self._timer_on_flag = False
        self.timer.stop()
        self.close_btn.setEnabled(True)
        self._set_param_enable(True)
        self.timer_index = 0
        self.timer_counter = 0
        self._reset_pbar()
        self.start_btn.disconnect()
        self.start_btn.setText('START')
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)
        self.status_display_btn.setText('--')
        self.estimated_time_remaining_lbl.setText( "Estimated Time: <..> min(s)") 
        self.start_btn.clicked.connect(self.onClickStart)
    
    def areYouSureMsg(self, action):
        """Confirms whether or not the user meant to click an action button"""
        msg = QtWidgets.QMessageBox()
        msg.setText('Are you sure you want to {}'.format(action))
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)
        msg.exec()
    
    def msgbtn(self, i):
        """Returns the result from the are you sure pop up"""
        self.is_sure = True if 'ok' in i.text().lower() else False

    ## Timer Related Events ##

    def progress_bar_handler(self):
        """
        Update the progress bar and estimated time remaining display
        """
        if self._timer_on_flag:
            if self.timer_index < 4:
                # Update progress bar as needed
                percen_comp = self.pbars[self.timer_index].value()
                if percen_comp < 100:
                    # Calculating time remaining
                    time_rem = self.estimated_time[self.timer_index] - (self.timer_counter*self._time_per_update/1000)
                    percen_comp = (1-(time_rem/self.estimated_time[self.timer_index]))*100
                    self.timer_counter += 1
                    self.pbars[self.timer_index].setValue(percen_comp)
                    if percen_comp == 100:
                        self.timer_index += 1
                        self._update_current_step()
                        # reset the counter when completed
                        self.timer_counter = 0

    def _update_current_step(self):
        step = ['Equilibrate', 'Load', 'Wash', 'Elute', 'Purification Complete']
        self.current_step_display_btn.setText(step[self.timer_index])

    def log_timer_handler(self):
        """Update the logger"""
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'r') as f:
            output = f.read()
        if self.log_output is None or self.log_output != output:
            self.log_output_txtbox.setText(output)
            log_end = self.log_output_txtbox.verticalScrollBar().maximum()
            self.log_output_txtbox.verticalScrollBar().setValue(log_end)
        self.log_output = output