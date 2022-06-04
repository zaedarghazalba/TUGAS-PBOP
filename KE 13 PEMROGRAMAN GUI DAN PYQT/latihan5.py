# membuat kalkulatordengan program GUI dan pyqt5


import sys
from PyQt5.QtWidgets import *


class mainForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 200) 
        self.setWindowTitle('Demo Kalkulator') 
        self.label1=QLabel('Bilangan ke-1') 
        self.num1Edit = QLineEdit() 
        self.label2 = QLabel('Bilangan ke-2') 
        self. num2Edit = QLineEdit() 
        self.label3 = QLabel('Hasil Perhitungan') 
        self.resultEdit=QLineEdit() 
        self.addButton=QPushButton('Tambah') 
        self.subtractButton=QPushButton('Kurang') 
        self.mulButton=QPushButton('Kali ') 
        self.divButton=QPushButton('Bagi') 
        vbox=QVBoxLayout() 
        vbox.addWidget(self.label1) 
        vbox.addWidget(self.num1Edit) 
        vbox.addWidget(self.label2) 
        vbox.addWidget(self.num2Edit) 
        vbox.addWidget(self.label3) 
        vbox.addWidget(self.resultEdit) 
        vbox.addStretch()

        hbox=QHBoxLayout() 
        hbox.addWidget(self.addButton) 
        hbox.addWidget(self.subtractButton)
        hbox.addWidget(self.mulButton)
        hbox.addWidget(self.divButton)

        mainLayout = QVBoxLayout() 
        mainLayout.addLayout(vbox) 
        mainLayout.addLayout(hbox) 
        self.setLayout(mainLayout) 
        self.addButton.clicked.connect(lambda: self.calculate('+')) 
        self.subtractButton.clicked.connect(lambda: self.calculate('-')) 
        self.mulButton.clicked.connect(lambda: self.calculate('*'))
        self.divButton.clicked.connect(lambda: self.calculate('/')) 
        
    def calculate(self, operator): 
        num1 =  float ( self.num1Edit.text ( ) ) 
        num2 = float ( self.num2Edit.text ( ) ) 
        if operator == '+':
             result = num1 + num2 
             operation = ' penjumlahan'
        elif operator == '-':
            result = num1 - num2 
            operation = 'pengurangan'
        elif operator == '*':
            result = num1 * num2 
            operation = 'perkalian'
        else :
            result = num1 / num2 
            operation = 'pembagian'

        self.label3.setText("Hasil : %s" % operation)
        self.resultEdit.setText(str(result))

if __name__ == '__main__' :
    a = QApplication(sys.argv)
    form = mainForm()
    form.show()
    a.exec_()