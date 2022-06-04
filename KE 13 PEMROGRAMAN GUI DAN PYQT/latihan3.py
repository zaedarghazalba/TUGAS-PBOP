#membuat slot untuk menanggani sinyal

import sys
from PyQt5.QtWidgets import*


class MainForm (QWidget):
        def __init__(self):
                super().__init__()
                self.setupUi()
        
        def setupUi(self):
                self.resize(250,100)
                self.setWindowTitle('Demo Signal dan Slotnya bossssss')

                self.label=QLabel('Masukkan nama anda')
                self.nameEdit=QLineEdit()
                self.haloButton = QPushButton('Hallo')

                vbox = QVBoxLayout()
                vbox.addWidget(self.label)
                vbox.addWidget(self.nameEdit)
                vbox.addWidget(self.haloButton)

                self.setLayout(vbox)
                self.haloButton.clicked.connect(self.on_haloButton_clicked)

        def on_haloButton_cilicked(self):
                name=self.nameEdit.text()
                QMessageBox.information(self,'HALOO','HAI %s, apa kabar? ' % name)

if __name__ == '__main__':
        a=QApplication(sys.argv)
        form =MainForm()
        form.show()
