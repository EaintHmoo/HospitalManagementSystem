from PyQt5 import uic,QtGui,QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import *
import pandas as pd
from PyQt5.QtWidgets import QMessageBox

class UiClass(QDialog):
    def __init__(self):
        super(UiClass,self).__init__()
        uic.loadUi('../View/signup.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.setMyStyle()
        self.pushButton_singUp.clicked.connect(self.signUp)


    def setMyStyle(self):
        self.pushButton_singUp.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                            "border-width: 2px;border-radius: 10px;}"
                                            "QPushButton:pressed { background-color: #185189226}"
                                            "QPushButton:hover {background-color: #FDEDEC;}")

    def signUp(self):
        try:
            usr = self.lineEdit_usr.text().strip()
            psw = self.lineEdit_psw.text()
            role = self.comboBox_role.currentText().lower()
            link_id = self.lineEdit_linkId.text()
            #id, username, password, link_id, role
            arr = [usr,psw,link_id,role]
            print(arr)
            flag = self.addLoginData(arr)
            print(arr)
            if flag:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Sign In sucessfully")
                msgBox.setWindowTitle("SignIn")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec_()
                if returnValue == QMessageBox.Ok:
                    self.lineEdit_usr.clear()
                    self.lineEdit_psw.clear()
                    self.comboBox_role.setCurrentIndex(0)
                    self.lineEdit_linkId.clear()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("This username is already exist.\nPlease use another username.")
                msgBox.setWindowTitle("SignIn Error")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec_()
                if returnValue == QMessageBox.Ok:
                    self.lineEdit_usr.clear()
                    self.lineEdit_psw.clear()
                    self.comboBox_role.setCurrentIndex(0)
                    self.lineEdit_linkId.clear()
        except Exception as e:
            print('signUp Error',str(e))

    def addLoginData(self,arr):
        try:
            df = pd.read_csv('../dataset/login_table.csv').username
            username = arr[0]
            print(df)
            for x in df:
                if username == x:
                    return False
            # write to file
            from Model.AddDataModel import DataClass
            model = DataClass('../dataset/login_table.csv')
            model.addNewData(arr)
            return True
        except Exception as e:
            print('addLoginData Error',str(e))