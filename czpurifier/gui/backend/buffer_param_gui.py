from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_BuffersWindow


class BackEnd_BuffersWindow(Ui_BuffersWindow):
    def __init__(self, BuffersWindow, gui_controller, protocol_buffers):
        """This window pops up when start is clicked to show the volume of 
        buffers needed and to adjust the flow rate calibration
        The default flow rate calibration is loaded from the json file"""
        self.BuffersWindow = BuffersWindow
        self.gui_controller = gui_controller
        super().setupUi(self.BuffersWindow)
        self.initEvents(protocol_buffers)

    def initEvents(self, protocol_buffers):
        """Initializes all on click actions"""
        self.sliders = [self.base_fc_slider, self.load_fc_slider, self.wash_fc_slider, self.elution_fc_slider]
        self.fc_txtbox = [self.base_fc_txtbox, self.load_fc_txtbox, self.wash_fc_txtbox, self.elution_fc_txtbox]
        self.updateDefaultFC()
        self.base_fc_slider.valueChanged.connect(lambda: self.slider_changed(0))
        self.load_fc_slider.valueChanged.connect(lambda: self.slider_changed(1))
        self.wash_fc_slider.valueChanged.connect(lambda: self.slider_changed(2))
        self.elution_fc_slider.valueChanged.connect(lambda: self.slider_changed(3))

        self.start_btn.clicked.connect(lambda: self.onclickStartCancel(True))
        self.cancel_btn.clicked.connect(lambda: self.onclickStartCancel(False))
        self.flow_rate_cor_question.clicked.connect(self.onclickDefineFC)

        self.updateBuffersNeeded(protocol_buffers)

        self.base_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        self.elution_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        self.load_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        self.wash_fc_txtbox.setValidator(QtGui.QDoubleValidator())
        
    def slider_changed(self, indx):
        """Updates text label beside the slider when slider is moved"""
        self.fc_txtbox[indx].setText('{}'.format(self.sliders[indx].value()))

    def onclickStartCancel(self, is_start):
        """Handles when start or cancel is clicked
        They are grouped together as the action is the same. It closes the window
        but if it is start then it puts up the start flag"""
        close = True
        if is_start:
            if self.gui_controller.checkEmptyQLines(self.fc_txtbox):
                self.gui_controller.setFlowCorrection(self.retriveFC())
            else: 
                is_start = False
                close = False
        self.gui_controller.is_sure = is_start
        if close:
            self.BuffersWindow.close()
    
    def retriveFC(self):
        """Get the final values for the percentage correction for each buffer"""
        return {'BASE': int(self.base_fc_txtbox.text()), 'LOAD_BUFFER': int(self.load_fc_txtbox.text()),
                'WASH': int(self.wash_fc_txtbox.text()), 'ELUTION': int(self.elution_fc_txtbox.text())}

    def onclickDefineFC(self):
        """Pops up a message to describe what the flow rate correction value should be"""
        msg = QtWidgets.QMessageBox()
        msg.setText("Flow Rate Correction = (Actual Flow Rate - Expected Flow Rate)*100")
        msg.setInformativeText('To determine the correction factor, ' 
        'run an experiment using the Custom Protol Window that outputs N mLs of buffer'
        ' and weigh the buffer to determine the real volume that was pumped.\n\n'
        'Expected Flow Rate = 1ml/min or 5ml/min for 1ml columns or 5ml columns respectively')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
    
    def updateBuffersNeeded(self, protocol_buffers):
        """Displays the vol of each buffer needed"""
        total_buffers = self.gui_controller.buffer_needed(protocol_buffers)
        self.base_vol.setText('{}'.format(total_buffers['BASE']))
        self.load_vol.setText('{}'.format(total_buffers['LOAD_BUFFER']))
        self.wash_vol.setText('{}'.format(total_buffers['WASH']))
        self.elution_vol.setText('{}'.format(total_buffers['ELUTION']))
        self.load_volume_needed.setText('{} mL'.format(total_buffers['LOAD']))

    def updateDefaultFC(self):
        """Displays the default flow rate correction % on start"""
        i = 0
        for t,s in zip(self.fc_txtbox, self.sliders):
            t.setText('{}'.format(self.gui_controller.default_buffer_fc[i]))
            s.setValue(self.gui_controller.default_buffer_fc[i])
            i += 1