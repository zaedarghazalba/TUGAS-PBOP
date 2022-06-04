#membuat grid layou dalam pyqt
import sys
from PyQt5.QtWidgets import*

class MainForm (QWidget):
        def __init__(self):
                super().__init__()
                self.setupUi()

        def setupUi(self):
                self.resize(250,100)
                self.setWindowTitle('Demo ne boss Grodlayout')
                self.label1=QLabel('Username')
                self.usernameEdit=QLineEdit()
                self.label2=QLabel('Password')
                self.passwordEdit=QLineEdit()
                self.loginButton = QPushButton ('Login')
                self.exitButton = QPushButton('Exit')

                grid=QGridLayout()
                grid.addWidget(self.label1,0,0)
                grid.addWidget(self.usernameEdit,0,1,1,2)
                grid.addWidget(self.label2,1,0)
                grid.addWidget(self.passwordEdit,1,1,1,2)
                grid.addWidget(self.loginButton,2,1)
                grid.addWidget(self.exitButton,2,2)

                self.setLayout(grid)

if __name__ == '__main__':
        a=QApplication(sys.argv)
        form = MainForm()
        form.show()
        a.exec_()