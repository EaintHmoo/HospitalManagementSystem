from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import QtGui
import pandas as pd
from PyQt5.QtCore import *

class UiClass(QDialog):
    def __init__(self,id):
        self.id = id
        super(UiClass,self).__init__()
        uic.loadUi('../View/PatientForm.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.showPersonalInfo()
        self.showMedicalInfo()

    def showPersonalInfo(self):
        try:
            df,doctor = self.getData('../dataset/patient_info_table.csv')
            self.label_patientId.setText(str(df.iloc[0].patient_id))
            self.label_name.setText(str(df.iloc[0].name))
            self.label_gender.setText(df.iloc[0].gender)
            self.label_age.setText(str(df.iloc[0].age))
            self.label_city.setText(df.iloc[0].city)
            self.label_doctor.setText(doctor.iloc[0])
            self.label_fathername.setText(df.iloc[0].fathername)
            self.label_phone.setText(str(int(df.iloc[0].phone)))
            self.label_email.setText(df.iloc[0].email)
        except Exception as e:
            print('showPersonalInfo Error',str(e))

    def showMedicalInfo(self):
        try:
            df,doctor = self.getData('../dataset/patient_medical_info.csv')
            self.label_diseases.setText(str(df.iloc[0].diseases))
            self.label_doctor_2.setText(str(doctor.iloc[0]))
            self.plainTextEdit_medication.setPlainText(str(df.iloc[0].medication))
            self.plainTextEdit_listOfMedicine.setPlainText(str(df.iloc[0].list_of_medicine))
            dob = df.iloc[0].date
            dates = dob.split('/')
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2])
            dd = QDate(year, month, day)
            self.dateEdit.setDate(dd)
        except Exception as e:
            print('showMedicalInfo Error',str(e))

    def getData(self,filepath):
        try:
            df = pd.read_csv(filepath)
            doctor_df = pd.read_csv('../dataset/doctor_info_table.csv')
            data = df[df['patient_id']==self.id]
            doctor_name = doctor_df[doctor_df['doctor_id'] == data.doctor_id.iloc[0]].name
            return data,doctor_name
        except Exception as e:
            print('getData Error',str(e))


'''app = QApplication(sys.argv)
window = UiClass(1)
window.show()
app.exec_()'''