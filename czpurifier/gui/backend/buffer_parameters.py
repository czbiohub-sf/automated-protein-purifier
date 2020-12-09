from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_BuffersWindow
from czpurifier.gui.control import GUI_Controller
from typing import Type, Dict


class BackEnd_BuffersWindow(Ui_BuffersWindow):
    """Display the volume of buffer/load needed and allow flow rate calibration

    :param Ui_BuffersWindow: Frontend display of the buffer window
    :type Ui_BuffersWindow: QMainWindow Class
    """

    def __init__(self, BuffersWindow, gui_controller: Type[GUI_Controller], 
                reagent_volume: Dict[str, float]):
        """Display the frontend and initialize the backend

        :param BuffersWindow: The window displaying the Ui
        :type BuffersWindow: QMainWindow
        :param gui_controller: Used to get the reagent volume needed
        :type gui_controller: Type[GUI_Controller]
        :param reagent_volume: Dict{k:v} k = Reagent name, v = volume needed
        :type reagent_volume: Dict[str, float]
        """
        
        self.BuffersWindow = BuffersWindow
        self.gui_controller = gui_controller
        super().setupUi(self.BuffersWindow)
        self.init_events(reagent_volume)

    def init_events(self, reagent_volume: Dict[str, float]):
        """Initialize the backend

        :param reagent_volume: Dict{k:v} k = Reagent name, v = volume needed
        :type reagent_volume: Dict[str, float]
        """

        self.sliders = [self.base_fc_slider, self.load_fc_slider, self.wash_fc_slider, self.elution_fc_slider]
        self.fc_txtbox = [self.base_fc_txtbox, self.load_fc_txtbox, self.wash_fc_txtbox, self.elution_fc_txtbox]
        self.display_default_flowrate_correction()
        self.base_fc_slider.valueChanged.connect(lambda: self.slider_changed(0))
        self.load_fc_slider.valueChanged.connect(lambda: self.slider_changed(1))
        self.wash_fc_slider.valueChanged.connect(lambda: self.slider_changed(2))
        self.elution_fc_slider.valueChanged.connect(lambda: self.slider_changed(3))

        self.start_btn.clicked.connect(lambda: self.onClick_start_or_cancel(True))
        self.cancel_btn.clicked.connect(lambda: self.onClick_start_or_cancel(False))
        self.flow_rate_cor_question.clicked.connect(self.onClick_define_flowrate_correction)

        self.display_reagents_volume(reagent_volume)

        self.base_fc_txtbox.setValidator(QtGui.QDoubleValidator())  # Only allow double inputs
        self.elution_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        self.load_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        self.wash_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        
    def slider_changed(self, indx: int):
        """Updates text label beside the slider when slider is moved

        :param indx: The index identifier for the slider and textbox
        :type indx: int
        """

        self.fc_txtbox[indx].setText('{}'.format(self.sliders[indx].value()))

    def onClick_start_or_cancel(self, is_start: bool):
        """Closes the window when start or cancel is clicked

        :param is_start: True: Raises the start flag
        :type is_start: bool
        """

        close = True
        if is_start:
            if self.gui_controller.checkEmptyQLines(self.fc_txtbox):  # Make sure no textbox is empty
                self.gui_controller.setFlowCorrection(self.get_flowrate_correction())
            else: 
                is_start = False
                close = False
        self.gui_controller.is_sure = is_start
        if close:
            self.BuffersWindow.close()
    
    def get_flowrate_correction(self) -> Dict[str, float]:
        """Get the percentage correction for each buffer from the textbox""

        :return: Dict{k:v} k = Reagent name, v = correction factor
        :rtype: Dict[str, float]
        """

        return {'BASE': float(self.base_fc_txtbox.text()), 'LOAD_BUFFER': float(self.load_fc_txtbox.text()),
                'WASH': float(self.wash_fc_txtbox.text()), 'ELUTION': float(self.elution_fc_txtbox.text())}

    def onClick_define_flowrate_correction(self):
        """A pop up to describe what the flowrate correction factor is
        """

        msg = QtWidgets.QMessageBox()
        msg.setText("Flow Rate Correction = (Actual Flow Rate - Expected Flow Rate)*100")
        msg.setInformativeText('To determine the correction factor, ' 
        'run an experiment using the Custom Protol Window that outputs N mLs of buffer'
        ' and weigh the buffer to determine the real volume that was pumped.\n\n'
        'Expected Flow Rate = 1ml/min or 5ml/min for 1ml columns or 5ml columns respectively')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
    
    def display_reagents_volume(self, reagent_volume: Dict[str, float]):
        """Display the volume of reagents needed

        :param reagent_volume: Dict{k:v} k = Reagent name, v = volume needed
        :type reagent_volume: Dict[str, float]
        """

        total_buffers = self.gui_controller.buffer_needed(reagent_volume)
        self.base_vol.setText('{}'.format(total_buffers['BASE']))
        self.load_vol.setText('{}'.format(total_buffers['LOAD_BUFFER']))
        self.wash_vol.setText('{}'.format(total_buffers['WASH']))
        self.elution_vol.setText('{}'.format(total_buffers['ELUTION']))
        self.load_volume_needed.setText('{} mL'.format(total_buffers['LOAD']))

    def display_default_flowrate_correction(self):
        """Displays the default flow rate correction % on start
        """
        
        i = 0
        for t,s in zip(self.fc_txtbox, self.sliders):
            t.setText('{}'.format(self.gui_controller.default_buffer_fc[i]))
            s.setValue(self.gui_controller.default_buffer_fc[i])
            i += 1