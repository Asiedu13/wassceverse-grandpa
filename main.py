import re
from tkinter import dialog
from PIL import Image
from autocrop import Cropper
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *
from PySide2.QtWidgets import *

import email
import sqlite3
import sys
import pathlib
import platform
import time
import cv2
import numpy as np
import os


# GUI FILES
from ui_classes.ui_main import Ui_MainWindow
from ui_classes.signInFailedOneDialog import Ui_signInFailedOneDialog
from ui_classes.ui_incorrectDialog import Ui_incorrectDialog
import ui_classes.edit as edit
from ui_classes.edit import Ui_Dialog


# IMPORT FUNCTIONS
from ui_functions import *

BASE_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
FOLDER_NAME = '.TEMP'

SAVE_PATH = BASE_DIR / FOLDER_NAME
SAVE_PATH.mkdir(exist_ok=True, parents=True)


class EditStudentInformation(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.school = window.school_name
        self.index = window.currentStudentId
        connection = sqlite3.connect("server2.db")
        cursor = connection.cursor()
        sql = f"SELECT * FROM student_details WHERE school = '{self.school}'"
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.close()
        index = self.index
        data = data[index]

        self.checkboxes = [
            self.ui.checkBox,
            self.ui.checkBox_2,
            self.ui.checkBox_3,
            self.ui.checkBox_4,
            self.ui.checkBox_5,
            self.ui.checkBox_6,
            self.ui.checkBox_7,
            self.ui.checkBox_8,
            self.ui.checkBox_9,
            self.ui.checkBox_10,
            self.ui.checkBox_11,
            self.ui.checkBox_12,
            self.ui.checkBox_13,
            self.ui.checkBox_14,
            self.ui.checkBox_15,
            self.ui.checkBox_16,
            self.ui.checkBox_17,
            self.ui.checkBox_18,
            self.ui.checkBox_19,
            self.ui.checkBox_20,
            self.ui.checkBox_21,
            self.ui.checkBox_22,
            self.ui.checkBox_23,
            self.ui.checkBox_24
        ]

        self.electives = data[7].split(",")
        for checkbox in self.checkboxes:
            for elective in self.electives:
                if checkbox.text() == elective:
                    checkbox.setChecked(True)

        self.radios = [self.ui.radioButton, self.ui.radioButton_2]
        for radio in self.radios:
            if radio.text() == data[9]:
                radio.setChecked(True)

        def update():
            surname = self.ui.plainTextEdit.toPlainText().replace("'", "''")
            first_name = self.ui.plainTextEdit_2.toPlainText().replace("'", "''")
            other_names = self.ui.plainTextEdit_3.toPlainText().replace("'", "''")
            course = self.ui.comboBox.currentText().replace("'", "''")
            class_ = self.ui.textEdit.toPlainText().replace("'", "''")
            index_number = self.ui.plainTextEdit_4.toPlainText().replace("'", "''")
            # year_completed = str(self.ui.dateEdit_2.date().year())
            elective = []
            for checkbox in self.checkboxes:
                if checkbox.isChecked():
                    elective.append(checkbox.text())

            gender = ""
            for radio in self.radios:
                if radio.isChecked:
                    gender = radio.text()

            parent_contact = self.ui.plainTextEdit_5.toPlainText().replace("'", "''")
            # dob = str(self.ui.dateEdit_2.date())

            connection = sqlite3.connect("server2.db")

            sql = f"UPDATE student_details SET surname = '{surname}', first_name = '{first_name}', other_names = '{other_names}', course = '{course}', class = '{class_}', index_number = '{index_number}', electives = '{elective[0]},{elective[1]},{elective[2]},{elective[3]}', gender = '{gender}', parent_contact = '{parent_contact}' WHERE _rowid_ = {self.index}"
            connection.execute(sql)
            print(sql)
            connection.commit()
            connection.close()

        self.ui.plainTextEdit.setPlainText(data[0])
        self.ui.plainTextEdit_2.setPlainText(data[1])
        self.ui.plainTextEdit_3.setPlainText(data[2])
        date = data[11].split("/")
        self.ui.dateEdit.setDate(
            QDate(int(date[2]), int(date[1]), int(date[0])))
        self.ui.comboBox.setCurrentText(data[3])
        self.ui.textEdit.setText(data[4])
        self.ui.plainTextEdit_4.setPlainText(data[5])
        self.ui.dateEdit_2.setDate(QDate(int(data[6]), 1, 1))
        self.ui.plainTextEdit_5.setPlainText(data[10])
        self.ui.save.clicked.connect(lambda: update())


class AddStudentInformation(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        def insert():
            surname = self.ui.plainTextEdit.toPlainText().replace("'", "''")
            first_name = self.ui.plainTextEdit_2.toPlainText().replace("'", "''")
            other_names = self.ui.plainTextEdit_3.toPlainText().replace("'", "''")
            course = self.ui.comboBox.currentText().replace("'", "''")
            class_ = self.ui.textEdit.toPlainText().replace("'", "''")
            index_number = self.ui.plainTextEdit_4.toPlainText().replace("'", "''")
            # year_completed = str(self.ui.dateEdit_2.date().year())

            self.checkboxes = [
            self.ui.checkBox,
            self.ui.checkBox_2,
            self.ui.checkBox_3,
            self.ui.checkBox_4,
            self.ui.checkBox_5,
            self.ui.checkBox_6,
            self.ui.checkBox_7,
            self.ui.checkBox_8,
            self.ui.checkBox_9,
            self.ui.checkBox_10,
            self.ui.checkBox_11,
            self.ui.checkBox_12,
            self.ui.checkBox_13,
            self.ui.checkBox_14,
            self.ui.checkBox_15,
            self.ui.checkBox_16,
            self.ui.checkBox_17,
            self.ui.checkBox_18,
            self.ui.checkBox_19,
            self.ui.checkBox_20,
            self.ui.checkBox_21,
            self.ui.checkBox_22,
            self.ui.checkBox_23,
            self.ui.checkBox_24
        ]

            self.radios = [self.ui.radioButton, self.ui.radioButton_2]


            elective = []
            for checkbox in self.checkboxes:
                if checkbox.isChecked():
                    elective.append(checkbox.text())

            gender = ""
            for radio in self.radios:
                if radio.isChecked:
                    gender = radio.text()

            parent_contact = self.ui.plainTextEdit_5.toPlainText().replace("'", "''")
            # dob = str(self.ui.dateEdit_2.date())

            connection = sqlite3.connect("server2.db")

            sql = f"INSERT INTO student_details (surname, first_name, other_names, course, class, index_number, electives, gender, parent_contact) VALUES ('{surname}', '{first_name}', '{other_names}', '{course}', '{class_}', '{index_number}', '{elective[0]},{elective[1]},{elective[2]},{elective[3]}', '{gender}', '{parent_contact}')"
            connection.execute(sql)
            print(sql)
            connection.commit()
            connection.close()

        self.ui.save.clicked.connect(lambda: insert())


class PasswordIncorrectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_incorrectDialog()
        self.ui.setupUi(self)


class FailDialogOne(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_signInFailedOneDialog()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.availableCameras = QCameraInfo.availableCameras()
        self.viewFinder = self.ui.camera_input
        self.savePath = None
        self.school_name = ""
        self.students = []
        self.currentStudentId = 0
        self.studentsNo = 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.comboBox.addItems([camera.description()
                                  for camera in self.availableCameras])

        statement = "SELECT school_name from registered_schools"
        connection = sqlite3.connect("server2.db")
        cursor = connection.cursor()
        cursor.execute(statement)
        data = cursor.fetchall()
        self.schools = [d[0]
                        for d in data]
        print(self.schools)

        statement = "SELECT school_code from registered_schools"
        cursor.execute(statement)
        data = cursor.fetchall()
        self.codes = [d[0]
                      for d in data]
        print(self.codes)

        statement = "SELECT school_email from registered_schools"
        cursor.execute(statement)
        data = cursor.fetchall()
        self.emails = [d[0]
                       for d in data]
        print(self.emails)
        connection.close()

        completer = QCompleter(self.schools)
        self.ui.schoolNameSignIn.setCompleter(completer)

        def camera_screen():
            self.selectCamera(0)
            self.ui.stackedWidget.setCurrentIndex(2)

        # CHECK INFO
        def signIn(db: str):
            schoolName = self.ui.schoolNameSignIn.text()
            if "'" in schoolName:
                schoolName = schoolName.replace("'", "''")
            email = self.ui.emailSignIn.text()
            password = self.ui.passwordSignIn.text()

            connection = sqlite3.connect("server2.db")
            cursor = connection.cursor()

            sql = f"SELECT * FROM registered_schools WHERE school_name = '{schoolName}' AND school_email = '{email}'"
            cursor.execute(sql)
            data = cursor.fetchall()
            connection.close()

            if len(data) != 0:
                if password != data[0][6]:
                    dialog = PasswordIncorrectDialog(self)
                    dialog.exec()
                else:
                    self.school_name = schoolName
                    getStudent(0)
                    switch_screen(3)
            else:
                dialog = FailDialogOne(self)
                dialog.exec()

        def signUp(db: str):
            school_name = self.ui.schoolNameSignUp.text().replace("'", "''")
            email = self.ui.emailSignUp.text()
            school_code = self.ui.schoolCodeSignUp.text()
            password = self.ui.passwordSignUp.text().replace("'", "''")
            if len(password) <= 6:
                self.ui.password_error.setHidden(False)
                self.ui.school_name_error.setHidden(True)
                self.ui.school_code_error.setHidden(True)
            elif len(email) > 0 and len(school_name) > 0 and len(school_code) > 0:
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if (not re.search(regex, email)):
                    "TODO"
                elif email in self.emails:
                    self.ui.email_error.setHidden(False)
                    self.ui.school_name_error.setHidden(True)
                    self.ui.school_code_error.setHidden(True)
                    self.ui.password_error.setHidden(True)
                elif school_name in self.schools:
                    self.ui.school_name_error.setHidden(False)
                    self.ui.email_error.setHidden(True)
                    self.ui.school_code_error.setHidden(True)
                    self.ui.password_error.setHidden(True)
                elif (not school_code.isnumeric()):
                    "TODO"
                elif school_code in self.codes:
                    self.ui.email_error.setHidden(True)
                    self.ui.school_name_error.setHidden(True)
                    self.ui.school_code_error.setHidden(False)
                    self.ui.password_error.setHidden(True)

                else:
                    connection = sqlite3.connect("server2.db")
                    # cursor = connection.cursor()
                    sql = f"INSERT INTO registered_schools (school_name, school_code, school_email, password, verified, country, location) VALUES ('{school_name}', {school_code}, '{email}', '{password}', 1, 'Ghana', 'nowhere')"
                    print(sql)
                    connection.execute(sql)
                    connection.commit()
                    connection.close()
                    switch_screen(0)

        def getStudent(id=self.currentStudentId):
            connection = sqlite3.connect("server2.db")
            cursor = connection.cursor()
            sql = f"SELECT * FROM student_details WHERE school = '{self.school_name}'"
            cursor.execute(sql)
            data = cursor.fetchall()
            connection.close()
            self.studentsNo = len(data)
            self.currentStudentId = id
            print("Number of students: ", self.studentsNo)
            print("Current student S/N: ", self.currentStudentId)

            def previous_block():
                if self.currentStudentId == 0:
                    self.ui.previous_data_button.setStyleSheet(
                        "background-color: rgb(200, 200, 200);")
                    self.ui.previous_data_button.setDisabled(True)
                else:
                    self.ui.previous_data_button.setStyleSheet("""QWidget {
                            background-color: rgb(112, 112, 112);
                            padding: 0px;
                            }

                            QWidget:hover {
                                background-color: rgb(168, 168, 168);
                            }
                        """
                                                               )
                    self.ui.previous_data_button.setDisabled(False)

            def next_block():
                if self.currentStudentId < self.studentsNo - 1:
                    self.ui.next_data_button.setStyleSheet("""QWidget {
                            background-color: rgb(112, 112, 112);
                            padding: 0px;
                            }

                            QWidget:hover {
                                background-color: rgb(168, 168, 168);
                            }
                        """
                                                           )
                    self.ui.next_data_button.setDisabled(False)
                elif self.currentStudentId == self.studentsNo - 1:
                    self.ui.next_data_button.setStyleSheet(
                        "background-color: rgb(70, 70, 70);")
                    self.ui.next_data_button.setDisabled(True)

            next_block()
            previous_block()

            if len(data) != 0:
                name = f"{data[id][0]} {data[id][1]} {data[id][2]}"
                self.ui.student_name.setText(name.strip())
                self.ui.student_school.setText(data[id][8])
                self.ui.student_class.setText(data[id][4])
                self.ui.student_course.setText(data[id][3])
                self.ui.student_gender.setText(data[id][9].title())
                date = data[id][11]
                date = date.split("/")
                day = int(date[0])
                suffix = ""
                if 11 <= (day % 100) <= 13:
                    suffix = 'th'
                else:
                    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(day % 10, 4)]
                day = f"{str(day)}{suffix}"

                months = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]
                month = months[int(date[1])-1]
                self.currentStudentId = id

                date = f"{day} {month} {date[2]}"
                self.ui.date_of_birth_label.setText(date)
                self.ui.parent_contact.setText(data[0][10])
                self.ui.index_number_bece.setText(data[0][5])
                electives_array = data[0][7].split(",")
                self.ui.elective_1.setText(electives_array[0])
                self.ui.elective_2.setText(electives_array[1])
                self.ui.elective_3.setText(electives_array[2])
                self.ui.elective_4.setText(electives_array[3])

        def nextStudent():
            id = self.currentStudentId
            if self.currentStudentId < self.studentsNo:
                id = self.currentStudentId + 1
            getStudent(id)

        def previousStudent():
            id = 0
            if self.currentStudentId > 1:
                id = self.currentStudentId - 1
            getStudent(id)

        def delete_student():
            connection = sqlite3.connect("server2.db")
            cursor = connection.cursor()
            sql = f"DELETE FROM student_details WHERE _rowid_ = {self.currentStudentId}"
            cursor.execute(sql)
            connection.commit()
            connection.close()
            getStudent(self.currentStudentId)

        def add_student_dialog():
            dialog = AddStudentInformation(self)
            dialog.exec()

        def edit_student_dialog():
            dialog = EditStudentInformation(self)
            dialog.exec()

        self.ui.SignInSubmit_2.clicked.connect(lambda: signUp("server2.db"))
        self.ui.next_data_button.clicked.connect(lambda: nextStudent())
        self.ui.previous_data_button.clicked.connect(lambda: previousStudent())
        self.ui.search_student_button.clicked.connect(lambda: switch_screen(4))
        self.ui.close_search.clicked.connect(lambda: switch_screen(3))
        self.ui.take_photo.clicked.connect(lambda: camera_screen())
        self.ui.capture.clicked.connect(lambda: self.clickPhoto())
        self.ui.SignUpButton.clicked.connect(lambda: switch_screen(1))
        self.ui.SignUpButton_2.clicked.connect(lambda: switch_screen(0))
        self.ui.close_camera.clicked.connect(lambda: self.closeCamera())
        self.ui.SignInSubmit.clicked.connect(lambda: signIn("server2.db"))
        self.ui.edit_student_button.clicked.connect(
            lambda: edit_student_dialog())
        self.ui.add_student_button.clicked.connect(
            lambda: add_student_dialog())
        self.ui.delete_student_button.clicked.connect(lambda: delete_student())

        def switch_screen(screen: int):
            self.ui.stackedWidget.setCurrentIndex(screen)

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    # APP EVENTS
    ########################################################################

    def selectCamera(self, i):
        self.camera = QCamera(self.availableCameras[i])
        self.camera.setViewfinder(self.viewFinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda:
                                  self.alert(self.camera.errorString()))
        self.camera.start()
        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda d, i:
                                   print(
                                       f'Image Captured {str(self.saveSeq)}'))
        self.currentCameraName = self.availableCameras[i].description()
        self.saveSeq = 0

    def clickPhoto(self):
        timeStamp = time.strftime('Date %d %b %Y Time %H %M %S')
        fileName = f'Webcam {self.currentCameraName} {timeStamp} .jpg'
        savePath = SAVE_PATH / fileName
        self.savePath = savePath
        self.saveImage(str(savePath))
        print('Image saved on ', str(savePath))
        self.saveSeq += 1

    def closeCamera(self):
        if self.savePath == None:
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            cropper = Cropper(
                width=150,
                height=200,
                face_percent=40
            )

            # Get a Numpy array of the cropped image
            img_url = str(self.savePath)
            cropped_array = cropper.crop(img_url)

            # Save the cropped image with PIL if a face was detected:
            try:
                if len(cropped_array) != 0:
                    cropped_image = Image.fromarray(cropped_array)
                    cropped_image.save(self.savePath)
                with open(self.savePath, 'rb') as input_file:
                    ablob = input_file.read()
                    base = os.path.basename(self.savePath)
                    afile, ext = os.path.splitext(base)
                    sql = """UPDATE student_details
                    SET image = ?
                    WHERE _rowid_ = {self.currentStudentId}"""
                    connection = sqlite3.connect("server2.db")
                    # cursor = connection.cursor()
                    connection.execute(sql)
                    connection.commit()
                    connection.close()
                self.savePath = None
            except TypeError:
                self.savePath = None
                self.ui.stackedWidget.setCurrentIndex(3)

    def saveImage(self, savePath: str):
        self.capture.capture(savePath)

    def alert(self, msg):
        error = QErrorMessage(self)
        error.showMessage(msg)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
