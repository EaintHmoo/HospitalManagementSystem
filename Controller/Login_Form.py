from PyQt5 import uic,QtGui,QtWidgets
from PyQt5.QtWidgets import QDialog,QMessageBox


class UiClass(QDialog):
    def __init__(self):
        super(UiClass,self).__init__()
        uic.loadUi('../View/login.ui',self)
        self.setMyStyle()
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.pushButton_login.clicked.connect(self.login_attemp)
        self.pushButton_signup.clicked.connect(self.singup)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def login_attemp(self):
        usr = self.lineEdit_username.text().strip()
        pwd = self.lineEdit_password.text().strip()
        from Controller.LoginCheck import LoginFromFile
        lg = LoginFromFile('../dataset/login_table.csv', usr, pwd)
        login_list = lg.getDataFromFileCSV()
        result, link_id, role = lg.checkLogin(login_list)
        if result == True:
            if role == "patient":
                import sys
                # self.window1.setVisible(False)
                print('patient')
                from Controller.Patient_Form import UiClass
                ui = UiClass(link_id)
                ui.show()
                ui.exec_()
            elif role == "admin":
                from Controller.Admin_Form import UiClass
                ui = UiClass(link_id)
                ui.show()
                ui.exec_()
            else:
                from Controller.Doctor_Form import UiClass
                teacher = UiClass(link_id)
                teacher.show()
                teacher.exec_()
        else:
            self.unsuccessMessage()

    def unsuccessMessage(self):
        try:
            from PyQt5.QtWidgets import QMessageBox
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Login Unsucessful")
            msgBox.setWindowTitle("Login Error")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec_()
            if returnValue == QMessageBox.Ok:
                self.lineEdit_username.clear()
                self.lineEdit_password.clear()
        except Exception as e:
            print("unsuccessMessage Error",str(e))



    def singup(self):
        from Controller.Signup_Form import UiClass
        ui = UiClass()
        ui.show()
        ui.exec_()


    def setMyStyle(self):
        self.label.setStyleSheet("background-image:url(../img/login.png);\n")

        self.pushButton_login.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                           "border-width: 2px;border-radius: 10px;}"
                                           "QPushButton:pressed { background-color: #185189226}"
                                           "QPushButton:hover {background-color: #FDEDEC;}")

        self.pushButton_signup.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                            "border-width: 2px;border-radius: 10px;}"
                                            "QPushButton:pressed { background-color: #185189226}"
                                            "QPushButton:hover {background-color: #FDEDEC;}")