from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import QtGui
import pandas as pd
import sys


class UiClass(QDialog):
    global patient_id
    patient_id = 0
    global medical_id
    medical_id = 0
    def __init__(self,id):
        self.id = id
        super(UiClass,self).__init__()
        uic.loadUi('../View/DoctorForm.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.setMyStyle()
        self.showPatientName()
        self.comboBox_patientName.currentIndexChanged.connect(self.showPatientInfoTable)
        self.tableView_patient_list.doubleClicked.connect(self.doubleClicked_table)
        self.add_new_record.clicked.connect(self.addNewRecord)
        self.medical_record.clicked.connect(self.checkMedicalRecord)

    def checkMedicalRecord(self):
        try:
            global medical_id
            print(medical_id)
            if(medical_id==0):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("You should select at least one record to add")
                msgBox.setWindowTitle("No Data")
                msgBox.exec_()
            else:
                from Controller.MedicalRecord_Form import UiClass
                window = UiClass(medical_id)
                window.show()
                window.exec_()
        except Exception as e:
            print("checkMedicalRecord Error:",str(e))

    def addNewRecord(self):
        global patient_id
        if patient_id == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("You should select at least one record to add")
            msgBox.setWindowTitle("No Data")
            msgBox.exec_()
        else:
            from Controller.AddRecord_Form import UiClass
            window = UiClass(patient_id,self.id)
            window.show()
            window.exec_()


    def doubleClicked_table(self):
        index = self.tableView_patient_list.selectedIndexes()[0]
        id_us = self.tableView_patient_list.model().data(index)
        global medical_id
        medical_id=id_us
        print(medical_id)

    def showPatientInfoTable(self):
        try:
            patientName = self.comboBox_patientName.currentText()
            if patientName != "Choose Patient":
                df = pd.read_csv('../dataset/patient_info_table.csv')
                patientId = df[df['name']==patientName].patient_id.iloc[0]
                global patient_id
                patient_id = patientId
                medical_df = pd.read_csv('../dataset/patient_medical_info.csv')
                medical_data = medical_df[(medical_df['patient_id']==patientId)&(medical_df['doctor_id']==self.id)][['id','patient_id','diseases','medication','list_of_medicine','date']]
                from Model.TableModel import pandasModel
                model = pandasModel(medical_data)
                self.tableView_patient_list.setModel(model)
        except Exception as e:
            print('showPatientInfoTabel Error:',str(e))

    def showPatientName(self):
        df = pd.read_csv('../dataset/patient_info_table.csv')
        patientName = df[df['doctor_id']==self.id].name
        for i in patientName:
            self.comboBox_patientName.addItem(i)

    def setMyStyle(self):
        self.add_new_record.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                            "border-width: 2px;border-radius: 10px;}"
                                            "QPushButton:pressed { background-color: #185189226}"
                                            "QPushButton:hover {background-color: #FDEDEC;}")
        self.medical_record.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                                  "border-width: 2px;border-radius: 10px;}"
                                                  "QPushButton:pressed { background-color: #185189226}"
                                                  "QPushButton:hover {background-color: #FDEDEC;}")

'''app = QApplication(sys.argv)
window = UiClass(1)
window.show()
app.exec_()'''