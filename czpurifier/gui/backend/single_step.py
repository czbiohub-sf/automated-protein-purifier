from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_StepWidget
from czpurifier.gui.control import GUI_Controller


class BackEnd_StepWidget(Ui_StepWidget):
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
        super().setupUi(self.add_step_widget)
        self.step_num.setText("{}".format(step_no))
        self._init_widget_actions()

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
        self.volume_val_lbl.setValidator(QtGui.QDoubleValidator())

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
        """
        Control the enable/disable of widgets based on path selected
        Call the fraction collector methods to display the selected fractions if pathway is 3
        Parameters
        ---------------------------------------
        current_index: The index of the step, used to determine whether to use fraction/flow column
        and which text box to use to get the volume to flow
        """
        flow_path_map = {0: 'PRECOLUMNWASTE', 1: 'POSTCOLUMNWASTE', 2: 'FLOWCOL', 3: 'FRACCOL'}
        # ensure that reclicking the same flowpath twice does not mess the fraction collector pathway
        if self.last_flowpath != current_index:
            self.last_flowpath = current_index
            vol = int(self.volume_val_lbl.text())
            enable_widgets, rejected = self.gui_controller.setFlowPath(self.step_no, flow_path_map[current_index], vol)
            self.fraction_widgets_enabler(enable_widgets)
            if rejected:
                self.flowpath_combo_box.setCurrentIndex(0)
                self.last_flowpath = 0
        
    def fraction_widgets_enabler(self, is_enabled):
        self.volume_val_lbl.setEnabled(is_enabled)
        self.volume_slider.setEnabled(is_enabled)