import re
from tkinter import dialog
from PIL import Image
from autocrop import Cropper
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage)
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
import mariadb
import shutil


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

CONNECTION = mariadb.connect(
    host="localhost",
    user="root",
    passwd="",
    database="wassceverse",
    port=3306
)

CURSOR = CONNECTION.cursor()

class EditStudentInformation(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.school = window.school_name
        self.index = window.studentData[0]
        self.listIndex = window.currentStudentId
        sql = "SELECT * FROM student_details WHERE school = ?"
        CURSOR.execute(sql, (self.school,))

        result = []
        for data in CURSOR:
            result.append(data)

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

        self.electives = data[8].split(",")
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

            electives = f'{elective[0]},{elective[1]},{elective[2]},{elective[3]}'
            sql = "UPDATE student_details SET surname = ?, first_name = ?, other_names = ?, course = ?, class = ?, index_number = ?, electives = ?, gender = ?, school = ?, parent_contact = ?"
            CURSOR.execute(sql, (surname, first_name, other_names, course, class_,
                           index_number, electives, gender, self.school, parent_contact))
            CONNECTION.commit()

        self.ui.plainTextEdit.setPlainText(data[1])
        self.ui.plainTextEdit_2.setPlainText(data[2])
        self.ui.plainTextEdit_3.setPlainText(data[3])
        date = data[12].split("/")
        self.ui.dateEdit.setDate(
            QDate(int(date[2]), int(date[1]), int(date[0])))
        self.ui.comboBox.setCurrentText(data[4])
        self.ui.textEdit.setText(data[5])
        self.ui.plainTextEdit_4.setPlainText(data[6])
        self.ui.dateEdit_2.setDate(QDate(int(data[7]), 1, 1))
        self.ui.plainTextEdit_5.setPlainText(data[11])
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
                if radio.isChecked():
                    gender = radio.text()

            parent_contact = self.ui.plainTextEdit_5.toPlainText().replace("'", "''")
            # dob = str(self.ui.dateEdit_2.date())

            connection = sqlite3.connect("server2.db")

            sql = f"INSERT INTO student_details (surname, first_name, other_names, course, class, index_number, electives, school, gender, parent_contact) VALUES ('{surname}', '{first_name}', '{other_names}', '{course}', '{class_}', '{index_number}', '{elective[0]},{elective[1]},{elective[2]},{elective[3]}', '{window.school_name}',  '{gender}', '{parent_contact}')"
            connection.execute(sql)
            connection.commit()
            connection.close()
            window.getStudent()

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
        self.studentData = []
        self.currentStudentId = 0
        self.studentsNo = 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.comboBox.addItems([camera.description()
                                  for camera in self.availableCameras])

        sql = "SELECT * FROM registered_schools"
        CURSOR.execute(sql)
        self.schools = []
        self.codes = []
        self.emails = []
        for data in CURSOR:
            self.schools.append(data[1])
            self.codes.append(data[4])
            self.emails.append(data[6])

        completer = QCompleter(self.schools)
        self.ui.schoolNameSignIn.setCompleter(completer)

        def camera_screen():
            self.selectCamera(0)
            self.ui.stackedWidget.setCurrentIndex(2)

        # CHECK INFO
        def signIn():
            schoolName = self.ui.schoolNameSignIn.text()
            email = self.ui.emailSignIn.text()
            password = self.ui.passwordSignIn.text()

            sql = "SELECT * FROM registered_schools WHERE school_name = ? AND school_email = ?"
            CURSOR.execute(sql, (schoolName, email))
            data = []
            for d in CURSOR:
                data.append(d)

            if len(data) != 0:
                if password != data[0][7]:
                    dialog = PasswordIncorrectDialog(self)
                    dialog.exec()
                else:
                    self.school_name = schoolName
                    sql = "SELECT * FROM student_details WHERE school = ?"
                    CURSOR.execute(sql, (self.school_name,))
                    data = []
                    for d in CURSOR:
                        data.append(d)
                    self.studentsNo = len(data)
                    if self.studentsNo > 0:
                        self.getStudent(0)
                        switch_screen(3)
                    else:
                        switch_screen(5)
            else:
                dialog = FailDialogOne(self)
                dialog.exec()

        def signUp(db: str):
            school_name = self.ui.schoolNameSignUp.text()
            email = self.ui.emailSignUp.text()
            school_code = self.ui.schoolCodeSignUp.text()
            password = self.ui.passwordSignUp.text()
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
                    sql = "INSERT INTO registered_schools (school_name, school_code, school_email, password, verified, country, location) VALUES (?, ?, ?, ?, 1, 'Ghana', 'nowhere')"
                    CURSOR.execute(
                        sql, (school_name, school_code, email, password))
                    CONNECTION.commit()
                    switch_screen(0)

        def nextStudent():
            id = self.currentStudentId
            if self.currentStudentId < self.studentsNo:
                id = self.currentStudentId + 1
            self.getStudent(id)

        def previousStudent():
            id = 0
            if self.currentStudentId > 1:
                id = self.currentStudentId - 1
            self.getStudent(id)

        def delete_student():
            sql = "DELETE FROM student_details WHERE id = ?"
            CURSOR.execute(sql, (self.studentData[0],))
            CONNECTION.commit()
            if self.currentStudentId + 1 == self.studentsNo:
                self.getStudent(self.currentStudentId-1)
            else:
                self.getStudent(self.currentStudentId)

        def add_student_dialog():
            dialog = AddStudentInformation(self)
            dialog.exec()

        def edit_student_dialog():
            dialog = EditStudentInformation(self)
            dialog.exec()

        def getImageFromFile():
            src = self.get_image_file()
            saveDir = SAVE_PATH / self.studentData[9]
            saveDir.mkdir(exist_ok=True, parents=True)
            saveFolder = saveDir / self.studentData[5]
            saveFolder.mkdir(exist_ok=True, parents=True)
            fileName = f'{self.studentData[1]} {self.studentData[2]} {self.studentData[3]}'.strip(
            ) + '.jpg'
            savePath = saveFolder / fileName
            pathlib.Path(src).rename(str(savePath))
            # Get a Numpy array of the cropped image
            img_url = str(savePath)

            cropper = Cropper(
                width=150,
                height=200,
                face_percent=40
            )
            cropped_array = cropper.crop(img_url)

            # Save the cropped image with PIL if a face was detected:
            try:
                if len(cropped_array) != 0:
                    cropped_image = Image.fromarray(cropped_array)
                    cropped_image.save(savePath)

            except TypeError:
                self.savePath = None

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
        self.ui.SignInSubmit.clicked.connect(lambda: signIn())
        self.ui.edit_student_button.clicked.connect(
            lambda: edit_student_dialog())
        self.ui.add_student_button.clicked.connect(
            lambda: add_student_dialog())
        self.ui.pushButton.clicked.connect(lambda: add_student_dialog())
        self.ui.delete_student_button.clicked.connect(lambda: delete_student())
        self.ui.import_file.clicked.connect(lambda: getImageFromFile())
        self.ui.searchbar_main.textChanged.connect(lambda: getStudentList())

        def getStudentList():
            sql = "SELECT * FROM student_details WHERE school = ?"
            CURSOR.execute(sql, (self.school_name,))
            data = []
            for d in CURSOR:
                data.append(d)
            search = self.ui.searchbar_main.text()
            names = []
            for d in data:
                name = f"{d[1]} {d[2]} {d[3]}".strip()
                names.append(name)

            # TODO: The search results
            self.ui.listWidget.clear()
            results = {}
            for n in names:
                if search in n:
                    results[n] = [n, names.index(n)]
                    self.ui.listWidget.addItem(n)

            def searchRes(item):
                self.getStudent(results[item.text()][1])
                self.ui.stackedWidget.setCurrentIndex(3)

            self.ui.listWidget.itemClicked.connect(searchRes)



        def switch_screen(screen: int):
            self.ui.stackedWidget.setCurrentIndex(screen)

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    # APP EVENTS
    ########################################################################

    def get_image_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.jpeg *.jpg *.png)", options=options)
        return file_name

    def getStudent(self, id=0):
        sql = "SELECT * FROM student_details WHERE school = ?"
        CURSOR.execute(sql, (self.school_name,))
        data = []
        for d in CURSOR:
            data.append(d)
        self.studentsNo = len(data)
        self.currentStudentId = id
        self.studentData = data[id]

        def previous_block():
            if self.currentStudentId == 0:
                self.ui.previous_data_button.setStyleSheet(
                    "background-color: rgb(200, 200, 200);"
                )
                self.ui.previous_data_button.setDisabled(True)
            else:
                self.ui.previous_data_button.setStyleSheet(
                    """QWidget {
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
                self.ui.next_data_button.setStyleSheet(
                    """QWidget {
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
                    "background-color: rgb(70, 70, 70);"
                )
                self.ui.next_data_button.setDisabled(True)

        next_block()
        previous_block()

        if len(data) != 0:
            name = f"{data[id][1]} {data[id][2]} {data[id][3]}"
            self.ui.student_name.setText(name.strip())
            self.ui.student_school.setText(data[id][9])
            self.ui.student_class.setText(data[id][5])
            self.ui.student_course.setText(data[id][4])
            self.ui.student_gender.setText(data[id][10].title())
            date = data[id][12]
            date = date.split("/")
            day = int(date[0])
            suffix = ""
            if 11 <= (day % 100) <= 13:
                suffix = 'th'
            else:
                suffix = ['th', 'st', 'nd', 'rd', 'th'][min(day % 10, 4)]
            day = f"{str(day)}{suffix}"

            month = ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"][int(date[1])-1]

            self.currentStudentId = id

            date = f"{day} {month} {date[2]}"
            self.ui.date_of_birth_label.setText(date)
            self.ui.parent_contact.setText(data[id][11])
            self.ui.index_number_bece.setText(data[id][6])
            electives_array = data[id][8].split(",")
            self.ui.elective_1.setText(electives_array[0])
            self.ui.elective_2.setText(electives_array[1])
            self.ui.elective_3.setText(electives_array[2])
            self.ui.elective_4.setText(electives_array[3])

            saveDir = SAVE_PATH / self.studentData[9]
            saveFolder = saveDir / self.studentData[5]
            fileName = f'{self.studentData[1]} {self.studentData[2]} {self.studentData[3]}'.strip(
            ) + '.jpg'
            savePath = saveFolder / fileName
            if savePath.exists():
                pixmap = QtGui.QPixmap(str(savePath))
            else:
                pixmap = QtGui.QPixmap(
                    'Include/img/user-sign-icon-person-symbol-human-avatar-vector-12693195.jpg')
            self.ui.label_12.setPixmap(pixmap)

            # FIXME: Getting image from database
            """ if type(data[id][14]) == bytes:
                if len(data[id][14]) > 0:
                    ba = QtCore.QByteArray(data[id][14])
                    pixmap = QtGui.QPixmap()
                    ok = pixmap.loadFromData(ba, "JPG")
                    assert ok
                else:
                    pixmap = QtGui.QPixmap('Include/img/user-sign-icon-person-symbol-human-avatar-vector-12693195.jpg')
                self.ui.label_12.setPixmap(pixmap) """

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
        fileName = f'{self.studentData[1]} {self.studentData[2]} {self.studentData[3]}'.strip(
        ) + '.jpg'
        saveDir = SAVE_PATH / self.studentData[9]
        saveDir.mkdir(exist_ok=True, parents=True)
        saveFolder = saveDir / self.studentData[5]
        saveFolder.mkdir(exist_ok=True, parents=True)
        savePath = saveFolder / fileName
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
                    sql = "UPDATE student_details SET image = ? WHERE index_number = ?"
                    CURSOR.execute(
                        sql, (mariadb.Binary(ablob), self.studentData[6]))
                    CONNECTION.commit()
                self.savePath = None
                self.getStudent(self.currentStudentId)
                self.ui.stackedWidget.setCurrentIndex(3)
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
