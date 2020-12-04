from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5 import QtGui
import pandas as pd


class UiClass(QDialog):

    def __init__(self,id):
        self.id = id
        super(UiClass,self).__init__()
        uic.loadUi('../View/AdminForm.ui',self)
        self.setWindowIcon(QtGui.QIcon('../img/red_cross.png'))
        self.pushButton_add_patient.clicked.connect(self.addPatientInfo)
        self.pushButton_add_doctor.clicked.connect(self.addDoctorInfo)
        self.pushButton_show.clicked.connect(self.showDoctorList)
        self.showDoctor()
        self.setPatientId()
        self.setDoctorId()
        self.setMyStyle()

#---------- Patient Info Form -----------#

    def setPatientId(self):
        df = pd.read_csv('../dataset/patient_info_table.csv')
        total_row = len(df) + 1
        print(total_row)
        self.lineEdit_patientId.setText(str(total_row))

    def showDoctor(self):
        df = pd.read_csv('../dataset/doctor_info_table.csv')
        names = df.name
        for i in names:
            self.comboBox_doctor.addItem(i)

    def addPatientInfo(self):
        pateint_id = self.lineEdit_patientId.text()
        name = self.lineEdit_patientName.text()
        gender = self.comboBox_gender.currentText()
        age = self.lineEdit_age.text()
        city = self.lineEdit_city.text()
        fathername = self.lineEdit_fathername.text()
        phone = self.lineEdit_phone.text()
        email = self.lineEdit_email.text()
        doctor = self.comboBox_doctor.currentText()
        doctor_id = self.getDoctorId(doctor)
        #id,patient_id,name,gender,age,city,doctor_id,fathername,phone,email
        arr = [pateint_id,name,gender,age,city,doctor_id,fathername,phone,email]
        self.addNewPatient(arr)

    def addNewPatient(self,arr):
        try:
            from Model.AddDataModel import DataClass
            model = DataClass('../dataset/patient_info_table.csv')
            model.addNewData(arr)
            self.clearPatientText()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Add New Patient Successfully.")
            msgBox.setWindowTitle("Add Data")
            msgBox.exec_()
        except Exception as e:
            print(str(e))

    def clearPatientText(self):
        self.setPatientId()
        self.lineEdit_patientName.clear()
        self.lineEdit_age.clear()
        self.lineEdit_city.clear()
        self.lineEdit_fathername.clear()
        self.lineEdit_phone.clear()
        self.lineEdit_email.clear()
        self.comboBox_gender.setCurrentIndex(0)
        self.comboBox_doctor.setCurrentIndex(0)

    def getDoctorId(self,doctorname):
        df = pd.read_csv('../dataset/doctor_info_table.csv')
        doctorId = df[df['name']==doctorname].doctor_id.iloc[0]
        return doctorId

#---------- Doctor Info Form ----------#

    def setDoctorId(self):
        df = pd.read_csv('../dataset/doctor_info_table.csv')
        total_row = len(df) + 1
        print(total_row)
        self.lineEdit_doctorId.setText(str(total_row))

    def addDoctorInfo(self):
        doctor_id = self.lineEdit_doctorId.text()
        name = self.lineEdit_doctorName.text()
        specialization = self.comboBox_specialization.currentText()
        department = self.comboBox_department.currentText()
        degree = self.comboBox_degree.currentText()
        phone = self.lineEdit_doctorPhone.text()
        email = self.lineEdit_doctorEmail.text()
        duty_time = self.lineEdit_dutyTime.text()
        #id,doctor_id,name,degree,specialization,department,phone,email,duty_time
        arr = [doctor_id,name,degree,specialization,department,phone,email,duty_time]
        self.addNewDoctor(arr)

    def addNewDoctor(self,arr):
        try:
            from Model.AddDataModel import DataClass
            model = DataClass('../dataset/doctor_info_table.csv')
            model.addNewData(arr)
            self.clearDoctorText()
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Add New Doctor Successfully.")
            msgBox.setWindowTitle("Add Data")
            msgBox.exec_()
        except Exception as e:
            print(str(e))

    def clearDoctorText(self):
        self.setDoctorId()
        self.lineEdit_doctorName.clear()
        self.lineEdit_doctorPhone.clear()
        self.lineEdit_doctorEmail.clear()
        self.lineEdit_dutyTime.clear()
        self.comboBox_specialization.setCurrentIndex(0)
        self.comboBox_department.setCurrentIndex(0)
        self.comboBox_degree.setCurrentIndex(0)


#---------- Doctor List Form ----------#

    def showDoctorList(self):
        try:
            department = self.comboBox_department_2.currentText()
            specialization = self.comboBox_specialization_2.currentText()
            df = pd.read_csv('../dataset/doctor_info_table.csv')
            data = df[(df['department']==department)&(df['specialization']==specialization)]
            from Model.TableModel import pandasModel
            model = pandasModel(data)
            self.tableView_doctor_list.setModel(model)
        except Exception as e:
            print('showDoctorList Error:',str(e))


    def setMyStyle(self):
        self.pushButton_add_patient.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                            "border-width: 2px;border-radius: 10px;}"
                                            "QPushButton:pressed { background-color: #185189226}"
                                            "QPushButton:hover {background-color: #FDEDEC;}")
        self.pushButton_add_doctor.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                                  "border-width: 2px;border-radius: 10px;}"
                                                  "QPushButton:pressed { background-color: #185189226}"
                                                  "QPushButton:hover {background-color: #FDEDEC;}")
        self.pushButton_show.setStyleSheet("QPushButton { background-color:#ffdf46;"
                                                  "border-width: 2px;border-radius: 10px;}"
                                                  "QPushButton:pressed { background-color: #185189226}"
                                                  "QPushButton:hover {background-color: #FDEDEC;}")

'''app = QApplication(sys.argv)
window = UiClass(1)
window.show()
app.exec_()'''