from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import QtGui
import pandas as pd

class UiClass(QDialog):

    def __init__(self,id):
        self.id = id
        super(UiClass,self).__init__()
        uic.loadUi('../View/MedicalRecord.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.showData()

    def showData(self):
        try:
            df = pd.read_csv("../dataset/patient_medical_info.csv")
            data = df[df['id']==int(self.id)]
            self.label_patientId.setText(str(data.patient_id.iloc[0]))
            self.label_disease.setText(data.diseases.iloc[0])
            self.plainTextEdit_medication.setPlainText(str(data.medication.iloc[0]))
            self.plainTextEdit_listOfMedicine.setPlainText(data.list_of_medicine.iloc[0])
            self.label_date.setText(data.date.iloc[0])
        except Exception as e:
            print('showData Error:',str(e))