from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import *

class UiClass(QDialog):

    def __init__(self,patientId,doctorId):
        self.patientId = patientId
        self.doctorId = doctorId
        super(UiClass,self).__init__()
        uic.loadUi('../View/AddRecord.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.pushButton_add.clicked.connect(self.addRecord)
        self.setMyStyle()


    def addRecord(self):
        disease = self.lineEdit_disease.text()
        medication = self.plainTextEdit_medication.toPlainText()
        list_of_medicine = self.plainTextEdit_listOfMedicine.toPlainText()
        dd = QDate(self.dateEdit.date())
        date = str(dd.day())+'/'+str(dd.month())+'/'+str(dd.year())
        #patient_id,diseases,doctor_id,medication,list_of_medicine,date
        arr = [self.patientId,disease,self.doctorId,medication,list_of_medicine,date]
        self.addNewData(arr)

    def addNewData(self,arr):
        try:
            from Model.AddDataModel import DataClass
            model = DataClass('../dataset/patient_medical_info.csv')
            print('hi')
            model.addNewData(arr)
            self.clearText()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Add New Record Successfully.")
            msgBox.setWindowTitle("Add Data")
            msgBox.exec_()
        except Exception as e:
            print(str(e))

    def clearText(self):
        self.lineEdit_disease.clear()
        self.plainTextEdit_medication.clear()
        self.plainTextEdit_listOfMedicine.clear()
        self.dateEdit.clear()

    def show(self):
        try:
            self.lineEdit_patientId.setText(str(self.patientId))
        except Exception as e:
            print('show error',str(e))

    def setMyStyle(self):
        self.pushButton_add.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                            "border-width: 2px;border-radius: 10px;}"
                                            "QPushButton:pressed { background-color: #185189226}"
                                            "QPushButton:hover {background-color: #FDEDEC;}")


