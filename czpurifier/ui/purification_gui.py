from PyQt5 import QtCore, QtGui, QtWidgets
from fraction_col_gui import Ui_FractionColumn
from buffer_param_gui import Ui_BuffersWindow
from os import chdir, path, getpid, kill
from signal import signal, SIGUSR1
from time import sleep
from math import ceil
from gui_controller import GUI_Controller

class Ui_Purification(object):
    def __init__(self, Purification, dev_process, columnsize, percolumncalib):
        """
        Contains the initialization and functionality of the purification tab
        The lists in this class are indexed as such:
        0 - Equilibrate step
        1 - Load step
        3 - Wash step
        4 - Elute step

        Parameters
        ------------------------------------------------
        Purification: The QtWindow that is created to display the purification window
        dev_process: Either a process object, if in simulator mode, or None. Used 
        to ping the simulator process in the controller class
        """
        self.gui_controller = GUI_Controller()
        self.gui_controller.hardware_or_sim(dev_process)
        self.columnsize = columnsize
        self.percolumncalib = percolumncalib
        signal(SIGUSR1, self.startProgressBar)
        self.Purification = Purification
        self.setupUi(self.Purification)
        self.initEvents()

    #################################################################
    # Desinger Generated Code #
    # To update just paste the new generated code below
    # Try to avoid updating the code directly to maintain consistency
    # with the Qt Designer code
    ##################################################################

    def setupUi(self, Purification):
        Purification.setObjectName("Purification")
        Purification.setWindowModality(QtCore.Qt.ApplicationModal)
        Purification.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(Purification)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.current_step_display_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_step_display_btn.sizePolicy().hasHeightForWidth())
        self.current_step_display_btn.setSizePolicy(sizePolicy)
        self.current_step_display_btn.setMinimumSize(QtCore.QSize(300, 45))
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
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
        self.progressBarLayout = QtWidgets.QHBoxLayout()
        self.progressBarLayout.setObjectName("progressBarLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBarLayout.addWidget(self.progressBar)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.progressLabel.setObjectName("progressLabel")
        self.progressBarLayout.addWidget(self.progressLabel)
        self.verticalLayout_7.addLayout(self.progressBarLayout)
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
        spacerItem2 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.start_btn.setStyleSheet("QPushButton#start_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}QPushButton:pressed#start_btn{background-color:#A9A9A9}")
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.pause_btn.setStyleSheet("QPushButton#pause_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}QPushButton:pressed#pause_btn{background-color:#A9A9A9}")
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout.addWidget(self.pause_btn)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.hold_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hold_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.hold_btn.setStyleSheet("QPushButton#hold_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}\n"
"QPushButton:pressed#hold_btn{background-color:#A9A9A9}")
        self.hold_btn.setObjectName("hold_btn")
        self.horizontalLayout.addWidget(self.hold_btn)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.skip_btn = QtWidgets.QPushButton(self.centralwidget)
        self.skip_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.skip_btn.setStyleSheet("QPushButton#skip_btn {border-radius:10;border-width: 2px; background-color: white; font-size:16px; border: 1px solid #808080}\n"
"QPushButton:pressed#skip_btn{background-color:#A9A9A9}")
        self.skip_btn.setObjectName("skip_btn")
        self.horizontalLayout.addWidget(self.skip_btn)
        spacerItem6 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setMinimumSize(QtCore.QSize(85, 85))
        self.stop_btn.setStyleSheet("QPushButton#stop_btn {border-radius:42;border-width: 2px;background-color: #ed1c24; color:white; font-size:20px; border: 1px solid #808080}\n"
"QPushButton:pressed#stop_btn{background-color:#A9A9A9}\n"
"QPushButton:disabled#stop_btn{background-color:#696969}")
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_7.addWidget(self.stop_btn)
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
        self.label_10.setText(_translate("Purification", "<html><head/><body><p>Run basic purification protocols using the following window. </p><p>To change the column size please close the window and update the column size in the main window.</p><p>The per column calibration from the main window will be applied to protocols here, to update the calibration please close the window and update the calibration on the main window.</p><p>On START a prompt will display the buffer and load volumes needed, along with the ability to update buffer dependent flow rates.</p></body></html>"))
        self.num_col_lbl.setText(_translate("Purification", "Number of Columns: "))
        self.num_col_combo_box.setItemText(0, _translate("Purification", "1"))
        self.num_col_combo_box.setItemText(1, _translate("Purification", "2"))
        self.num_col_combo_box.setItemText(2, _translate("Purification", "3"))
        self.num_col_combo_box.setItemText(3, _translate("Purification", "4"))
        self.equilibrate_lbl.setText(_translate("Purification", "Equilibrate"))
        self.equilibrate_vol_lbl.setText(_translate("Purification", "Volume:"))
        self.equilibriate_flowpath_lbl.setText(_translate("Purification", "Flow Path:"))
        self.label.setText(_translate("Purification", "CV"))
        self.equil_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.equil_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_lbl.setText(_translate("Purification", "Load"))
        self.load_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_3.setText(_translate("Purification", "Flow Path:"))
        self.label_2.setText(_translate("Purification", "CV"))
        self.load_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.load_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.load_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.wash_lbl.setText(_translate("Purification", "Wash"))
        self.wash_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_4.setText(_translate("Purification", "Flow Path:"))
        self.label_6.setText(_translate("Purification", "CV"))
        self.wash_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.wash_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.wash_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.elute_lbl.setText(_translate("Purification", "Elute"))
        self.elute_ph_lbl.setText(_translate("Purification", "Volume:"))
        self.label_5.setText(_translate("Purification", "Flow Path:"))
        self.label_7.setText(_translate("Purification", "CV"))
        self.elute_flowpath.setItemText(0, _translate("Purification", "Pre Column Waste"))
        self.elute_flowpath.setItemText(1, _translate("Purification", "Post Column Waste"))
        self.elute_flowpath.setItemText(2, _translate("Purification", "Fraction Collector"))
        self.label_8.setText(_translate("Purification", "Current Step:"))
        self.current_step_display_btn.setText(_translate("Purification", "--"))
        self.label_9.setText(_translate("Purification", "Status:"))
        self.status_display_btn.setText(_translate("Purification", "--"))
        self.estimated_time_remaining_lbl.setText(_translate("Purification", "Estimated Time: <..> min(s)"))
        self.start_btn.setText(_translate("Purification", "START"))
        self.pause_btn.setText(_translate("Purification", "PAUSE"))
        self.hold_btn.setText(_translate("Purification", "HOLD"))
        self.skip_btn.setText(_translate("Purification", "SKIP TO NEXT"))
        self.stop_btn.setText(_translate("Purification", "STOP"))
        self.close_btn.setText(_translate("Purification", "Close"))

    #### End of Qt Designer Code ######

    ###################
    # Event Handlers #
    ##################

    ## Initializing Event Handlers ##

    def initEvents(self):
        """Initializes all on click actions
        Creates additional class attributes"""
        # Parsed when start is clicked to determine the input parameters for run purification
        # Key: Name of the widget, Value: True = textbox widget, False = combobox widget
        self.input_param = {self.num_col_combo_box: False, self.columnsize: None,
                            self.equil_vol_val: True, self.equil_flowpath: False, 
                            self.load_vol_val: True, self.load_flowpath: False,
                            self.wash_vol_val: True, self.wash_flowpath: False,
                            self.elute_vol_val: True, self.elute_flowpath: False}
        # Useful groups of widgets for easier access
        self.vol_vals = [self.equil_vol_val, self.load_vol_val, self.wash_vol_val, self.elute_vol_val]
        self.vol_sliders = [self.equil_vol_slider, self.load_vol_slider, self.wash_vol_slider, self.elute_vol_slider]
        self.flowpath_combo = [self.equil_flowpath, self.load_flowpath, self.wash_flowpath, self.elute_flowpath]

        self.columnsize_int = 1 if self.columnsize == '1mL' else 5
        # Widget setup and activation on start
        self._set_actionbtn_enable(False, True)
        self.setDefaultParam()
        self.equil_flowpath.activated.connect(lambda: self.onClickFlowPath(0))
        self.load_flowpath.activated.connect(lambda: self.onClickFlowPath(1))
        self.wash_flowpath.activated.connect(lambda: self.onClickFlowPath(2))
        self.elute_flowpath.activated.connect(lambda: self.onClickFlowPath(3))
        self.close_btn.clicked.connect(self.onClickClose)
        self.start_btn.clicked.connect(self.onClickStart)
        self.pause_btn.clicked.connect(lambda: self.onClickPauseHold(True))
        self.hold_btn.clicked.connect(lambda: self.onClickPauseHold(False))
        self.skip_btn.clicked.connect(self.onClickSkip)
        self.stop_btn.clicked.connect(self.onClickStop)
        self.equil_vol_slider.valueChanged.connect(lambda: self.slider_changed(0))
        self.load_vol_slider.valueChanged.connect(lambda: self.slider_changed(1))
        self.wash_vol_slider.valueChanged.connect(lambda: self.slider_changed(2))
        self.elute_vol_slider.valueChanged.connect(lambda: self.slider_changed(3))
        self.current_step_display_btn.setEnabled(False)
        self.status_display_btn.setEnabled(False)

        # Set decimal validators for all text box
        self.equil_vol_val.setValidator(QtGui.QDoubleValidator())
        self.load_vol_val.setValidator(QtGui.QDoubleValidator())
        self.wash_vol_val.setValidator(QtGui.QDoubleValidator())
        self.elute_vol_val.setValidator(QtGui.QDoubleValidator())
        
        # Create all the flowpathway objects on init
        for i in range(4):
            self.gui_controller.flowpathwayClicked(i, 1)
        
        # Timers initialized
        # Timer for updating the current status
        self.protocol_step = 0
        self.status_timer = QtCore.QTimer()
        self.status_timer.timeout.connect(self.status_timer_handler)
        self.progressBar.setValue(0)
        self.pbar_timer = QtCore.QTimer()
        self.pbar_timer.timeout.connect(self.progress_bar_handler)

        # Logger initialized to display the steps
        self.log_update_timer = QtCore.QTimer()
        self.log_update_timer.timeout.connect(self.log_timer_handler)
        self.log_update_timer.start(2000)
        self.log_output_txtbox.setReadOnly(True)
        self.log_output = None

        #Timer for a delay between on start window pop up and checking result
        self.check_is_sure_timer = QtCore.QTimer()
        self.check_is_sure_timer.timeout.connect(self.check_is_sure_timer_handler)

        #Timer to track the total time remaining
        self.total_time_timer = QtCore.QTimer()
        self.total_time_timer.timeout.connect(self.total_time_handler)

        self.fraction_collector_window_on = True

    def setDefaultParam(self):
        """Sets the default input parameters that are on the json file"""
        self.num_col_combo_box.setCurrentIndex(self.gui_controller.default_param[0]-1)
        self.elute_vol_slider.setMaximum(10)
        self.equil_vol_val.setText(str(self.gui_controller.default_param[1]))
        self.load_vol_val.setText(str(self.gui_controller.default_param[2]))
        self.wash_vol_val.setText(str(self.gui_controller.default_param[3]))
        self.elute_vol_val.setText(str(self.gui_controller.default_param[4]))
        self.equil_vol_slider.setSliderPosition(self.gui_controller.default_param[1])
        self.load_vol_slider.setSliderPosition(self.gui_controller.default_param[2])
        self.wash_vol_slider.setSliderPosition(self.gui_controller.default_param[3])
        self.elute_vol_slider.setSliderPosition(self.gui_controller.default_param[4])
        self.last_flowpath = [0]*4

        self.fraction_collector_window_on = False
        self.equil_flowpath.setCurrentIndex(1)
        self.load_flowpath.setCurrentIndex(1)
        self.wash_flowpath.setCurrentIndex(1)
        self.elute_flowpath.setCurrentIndex(2)
        # Auto click the combo boxes on start to initialize all the fraction objs
        for i in range(4):
            self.onClickFlowPath(i)
    
    def startProgressBar(self, signalNumber, frame):
        """Start the timer to display the status once purging is completed
        Enable the pause/hold buttons after purging is completed"""  
        try:
            self.protocol_step += 1
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.stop()
            self.status_timer.start(self.step_times[self.protocol_step]*1000)
            self.progressBar.setValue(0)
        except IndexError:
            # Reached the final step
            self._finish_protocol()
        self._set_actionbtn_enable(True, False)

    ## Input Parameter Widget Actions ##

    def onClickFlowPath(self, step_index):
        """
        Control the enable/disable of widgets based on path selected
        Call the fraction collector methods to display the selected fractions if pathway is 3
        Parameters
        ---------------------------------------
        step_index: The index of the step, used to determine whether to use fraction/flow column
        and which text box to use to get the volume to flow
        """
        flow_path_combo = self.flowpath_combo[step_index]
        curIndex = flow_path_combo.currentIndex()
        if self.last_flowpath[step_index] != curIndex:
            self.last_flowpath[step_index] = curIndex
            col_size = 1 if step_index == 3 else 50
            self.gui_controller.flowpathwayClicked(step_index, col_size)
            if curIndex == 2:
                vol = int(self.vol_vals[step_index].text())
                max_vol = self.gui_controller.okay_vol_checker(vol, col_size)
                if max_vol == -1:
                    # volume is okay
                    disp = self.gui_controller.fractionCollectorSel(step_index, vol, col_size)
                    if self.fraction_collector_window_on:
                        self.frac_wdw = QtWidgets.QMainWindow()
                        self.frac_ui = Ui_FractionColumn(self.frac_wdw)
                        self.frac_wdw.show()
                        self.frac_ui.correct_frac_col_design()
                        self.frac_ui.display_selected(disp)
                    self.fraction_widgets_enabler(step_index, False)
                else:
                    # volume not available
                    self.gui_controller.vol_exceeds_msg(max_vol)
                    flow_path_combo.setCurrentIndex(0)
            else:
                self.fraction_widgets_enabler(step_index, True)
                self.gui_controller.fractionCollectorUnsel(step_index)
    
    def fraction_widgets_enabler(self, step_index, is_enabled):
        """Enable/Disable widgets related to the fraction collector pathway"""
        self.vol_vals[step_index].setEnabled(is_enabled)
        self.vol_sliders[step_index].setEnabled(is_enabled)

    def slider_changed(self, step_index):
        """Updates text label beside the slider when slider is moved
        Parameter
        -------------------------------
        step_index: Used to determine the slider and text widget to use
        """
        self.vol_vals[step_index].setText('{}'.format(self.vol_sliders[step_index].value()))

    def _init_run_param(self):
        """Parse through all the input parameters and return
         an array to pass to controller to run purification"""
        run_param = []
        for widget in self.input_param:
            if self.input_param[widget]:
                # Handle text inputs
                run_param.append(int(widget.text()))
            elif self.input_param[widget] is None:
                # handle the columnsize
                run_param.append(widget)
            else:
                # Handle combo box
                run_param.append(widget.currentIndex())
        # +1 needs to be added to the number of pumps
        run_param[0] = run_param[0] + 1

        # Make the per column calibration list
        calib_list = []
        for i in range(run_param[0]):
            calib_list.append(self.percolumncalib[i])

        return run_param, calib_list

    def calc_step_times(self):
        """Calculates an estimate time for each step"""
        step_times = [int(self.equil_vol_val.text()), int(self.load_vol_val.text()),
                    int(self.wash_vol_val.text()), int(self.elute_vol_val.text())]
        step_times = [i*60 for i in step_times]
        self.step_times = self.gui_controller.getPumpTimes(step_times)

    def protocol_buffers(self):
        """Returns the volume of buffers used. The vol is in CV so to convert
        it in mL need to multiply by the column size"""
        return  {'LOAD_BUFFER': int(self.equil_vol_val.text()),
                'WASH': int(self.wash_vol_val.text()),
                'ELUTION': int(self.elute_vol_val.text()), 'LOAD': int(self.load_vol_val.text())}

    ## Enable/Disable Widgets On GUI ##

    def _set_param_enable(self, state):
        """Enables/Disables all the widgets that allow initializing input parameters
        Used to disable inputting parameters when purifier is running"""
        for widget in self.input_param:
            if self.input_param[widget] is not None:
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

    ## Action Buttons Event Handlers ##

    def onClickClose(self):
        """Closes the purification window when close is clicked"""
        self.log_update_timer.stop()
        self.Purification.close()
    
    def onClickStart(self):
        """
        First check and make sure text boxes are not empty
        1. Pop up to confirm you want to start
        The following actions are performed after 1s by the check_is_sure_timer handler
        2. Enable stop and close (other action btns enabled after purging)
        3. Disable everything that can be edited
        4. Call _init_run_param() to create the array to pass to controller
        5. Start the logging and timers for estimated time
        6. Update the step display
        7. Run the process
        """
        if self.gui_controller.checkEmptyQLines(self.vol_vals):
            self.gui_controller.columnsize = self.columnsize_int
            self.startbufferWdw()
            self.check_is_sure_timer.start(1000)
    
    def startbufferWdw(self):
        self.bufferwdw = QtWidgets.QMainWindow()
        self.bufferwdw_ui = Ui_BuffersWindow(self.bufferwdw, self.gui_controller, self.protocol_buffers())
        self.bufferwdw.show()

    def onClickPauseHold(self, is_pause):
        """
        1. Enables Start button to resume
        2. Calls pause_clicked/hold that sends a pause/hold signal to 
        3. the process running the purification
        4. Update the step display from running to pause/hold
        5. Stops the timer and the progress bar updates
        """
        msg = 'pause' if is_pause else 'hold'
        self.gui_controller.areYouSureMsg(msg)
        if self.gui_controller.is_sure:
            self.stop_btn.setEnabled(False)
            self.gui_controller.is_sure = None
            remaining = self.status_timer.remainingTime()
            self.status_timer.stop()
            self.status_timer.setInterval(remaining)

            total_remaining = self.total_time_timer.remainingTime()
            self.total_time_timer.stop()
            self.total_time_timer.setInterval(total_remaining)
            self._set_actionbtn_enable(False, True)
            if is_pause:
                self.gui_controller.pause_clicked()
            else:
                self.gui_controller.hold_clicked()
            self.status_display_btn.setText('on {}'.format(msg))
            self.status_display_btn.setStyleSheet(
                self.gui_controller.status_display_stylsheet.format(
                self.gui_controller.status_display_color_halt))
            self.start_btn.disconnect()
            self.start_btn.setText('RESUME')
            self.start_btn.clicked.connect(self.onClickResume)

    def onClickResume(self):
        """
        1. Handles if resume is clicked after paused
        Sends a signal to the process running purification
        to resume the protocol
        2. Updates the status display back to running
        3. Resumes the timer and the progress bar update
        """
        self._set_actionbtn_enable(True, False)
        self.stop_btn.setEnabled(True)
        self.status_timer.start()
        self.total_time_timer.start()
        self.status_display_btn.setStyleSheet(
            self.gui_controller.status_display_stylsheet.format(
            self.gui_controller.status_display_color_running))
        self.status_display_btn.setText('running')
        self.gui_controller.resume_clicked()

    def onClickSkip(self):
        """
        1. Stops pumping and goes to the next step
        2. Restarts the progress bar timer for skip to the next bar
        """
        self.gui_controller.areYouSureMsg('skip to next step')
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.gui_controller.skip_clicked()

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
    

    ## Timer Related Events ##

    def status_timer_handler(self):
        """Stops the timer on the current step"""
        # Reached the final step
        self.status_timer.stop()

    def progress_bar_handler(self):
        """Update the progress bar and estimated time remaining display"""
        percen_comp = self.progressBar.value()
        if percen_comp < 100 and self.status_timer.isActive():
            # Calculating time remaining
            time_remaining = (self.status_timer.remainingTime())/1000
            percen_comp = (1-(time_remaining/self.step_times[self.protocol_step]))*100
            percen_comp = 0 if percen_comp < 0 else percen_comp
            self.progressBar.setValue(percen_comp)
            self.progressLabel.setText('{:.1f}%'.format(percen_comp))

        # Disable skip to next on clean up
        if self.protocol_step == 5:
            self.skip_btn.setEnabled(False)

        if self.total_time_timer.isActive():
            lbl = 'Estimated Time: {0:.2f} min(s) remaining'.format(self.total_time_timer.remainingTime()/(1000*60))
            self.estimated_time_remaining_lbl.setText(lbl)

    def get_current_step(self):
        """Used to display the step that is currently running"""
        return ['Setup and Purging','Equilibrate', 'Load', 'Wash', 'Elute', 'Running Clean Up']

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
    
    def total_time_handler(self):
        self.total_time_timer.stop()
        lbl = 'Less than a minute remaining'
        self.estimated_time_remaining_lbl.setText(lbl)
    
    def check_is_sure_timer_handler(self):
        """Timer is ran after start button is clicked. There needs to be a short delay
        to allow for the buffer window to display before checking for is_sure = True
        to start the protocol"""
        if self.gui_controller.is_sure:
            self.gui_controller.is_sure = None
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.close_btn.setEnabled(False)
            self._set_param_enable(False)
            init_params, calib_list = self._init_run_param()
            self.calc_step_times()
            self.total_time_timer.start(sum(self.step_times)*1000)
            self.current_step_display_btn.setEnabled(True)
            self.status_display_btn.setEnabled(True)
            self.status_display_btn.setText('running')
            self.gui_controller.run_purification_script(True, init_params, calib_list)
            self.pbar_timer.start(2000)
            self.current_step_display_btn.setText(self.get_current_step()[self.protocol_step])
            self.status_timer.start(self.step_times[self.protocol_step]*1000)