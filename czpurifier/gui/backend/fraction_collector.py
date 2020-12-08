from PyQt5 import QtCore, QtGui, QtWidgets
from czpurifier.gui.frontend import Ui_FractionWindow

class BackEnd_FractionColumn(Ui_FractionWindow):
    def __init__(self, FractionWindow):
        """
        Initialization of the GUI to choose the fractionating column
        This window is opened when 'Fraction Column' is chosen as the flow
        path from the Set Parameter window
        """
        self.flow_col = []
        self.frac_col = []
        self.frac_btn_stylesheet = '{}'.format("QPushButton#frac{0}_btn{{"
                                        "border-radius:17;"
                                        "background-color: {1};"
                                        "}}")
        self.flow_btn_stylesheet = '{}'.format("QPushButton#flowth{0}_btn{{"
                                        "border-radius:30;"
                                        "border-width: 2px;"
                                        "background-color: {1};"
                                        "}}")
        self.FractionWindow = FractionWindow
        super().setupUi(self.FractionWindow)
        self._init_frac_col()

    def _init_frac_col(self):
        """Groups together the flow through and fraction buttons for easy access"""
        self.flow_col = [self.flowth1_btn, self.flowth2_btn, self.flowth3_btn, self.flowth4_btn]
        self.frac_col = [self.frac1_btn, self.frac2_btn, self.frac3_btn, self.frac4_btn, self.frac5_btn,
                        self.frac6_btn, self.frac7_btn, self.frac8_btn, self.frac9_btn, self.frac10_btn]
        for i in range(len(self.flow_col)):
            self.flow_col[i].setStyleSheet(self.flow_btn_stylesheet.format('{}'.format(i+1),'white'))
        for i in range(len(self.frac_col)):
            self.frac_col[i].setStyleSheet(self.frac_btn_stylesheet.format('{}'.format(i+1),'white'))
        self.set_fraction_col_btn.clicked.connect(self.onClickOkay)
    
    def display_selected(self, disp_array):
        """Turn all the non zero columns in disp_array red. Determine the column type from array length"""
        frac_type = len(disp_array)
        btns_to_use = self.flow_col if frac_type == 4 else self.frac_col
        btn_stylesheet = self.flow_btn_stylesheet if frac_type == 4 else self.frac_btn_stylesheet
        i = 1
        for btn in btns_to_use:
            if disp_array[i-1] > 0:
                btn.setStyleSheet(btn_stylesheet.format(i, 'red'))
            i+=1

    def correct_frac_col_design(self):
        """Fix the distance between the buttons in the GUI window"""
        self._cor_design(self.flow_col, self.flow_btn_stylesheet)
        self._cor_design(self.frac_col, self.frac_btn_stylesheet)

    def _cor_design(self, frac, stlsheet):
        """Loop through all the buttons to fix the distance"""
        i = 1 
        for f in frac:
            f.setStyleSheet(stlsheet.format(i, 'white'))
            i += 1

    def onClickOkay(self):
        """Closes fraction column window when clicked Okay"""
        self.FractionWindow.close()