from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QDialog
import sys
from PyQt5 import QtGui
class mainForm(QDialog):

    def __init__(self):
        super(mainForm,self).__init__()
        uic.loadUi('../View/main.ui',self)
        self.setMyStyle()
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.pushButton_login.clicked.connect(self.startProgram)

    def startProgram(self):
        try:
            from Controller.Login_Form import UiClass
            ui = UiClass()
            ui.show()
            ui.exec_()
        except Exception as e:
            print(str(e))

    def closeEvent(self, event):
        print('in close')

    def setMyStyle(self):
        self.label_picture.setStyleSheet("background-image:url(../img/hospital.jpg);\n"
                                   "width:100%;\n"
                                   "height:100%;")

        self.pushButton_login.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                           "border-width: 2px;border-radius: 10px;}"
                                           "QPushButton:pressed { background-color: #185189226}"
                                           "QPushButton:hover {background-color: #FDEDEC;}")

app=QApplication(sys.argv)
window=mainForm()
window.show()
app.exec_()