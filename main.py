import re
from PIL import Image
from autocrop import Cropper
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtMultimedia import QCameraInfo, QCamera, QCameraImageCapture
from PySide2.QtMultimediaWidgets import QCameraViewfinder
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


# IMPORT FUNCTIONS
from ui_functions import *

class PasswordIncorrectDialog(QDialog):
    def __init__(self, parent = None):
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
        self.school_name = ""
        self.students = []
        self.currentStudentId = 0
        self.studentsNo = 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.comboBox.addItems([camera.description()
                                  for camera in self.availableCameras])
        self.connection = sqlite3.connect("server2.db")
        self.cursor = self.connection.cursor()

        statement = "SELECT school_name from registered_schools"
        self.cursor.execute(statement)
        data = self.cursor.fetchall()
        self.schools = [d[0]
        for d in data]
        print(self.schools)


        statement = "SELECT school_code from registered_schools"
        self.cursor.execute(statement)
        data = self.cursor.fetchall()
        self.codes = [d[0]
        for d in data]
        print(self.codes)


        statement = "SELECT school_email from registered_schools"
        self.cursor.execute(statement)
        data = self.cursor.fetchall()
        self.emails = [d[0]
        for d in data]
        print(self.emails)


        completer = QCompleter(self.schools)
        self.ui.schoolNameSignIn.setCompleter(completer)

        def camera_screen():
            self.selectCamera(0)
            self.ui.stackedWidget.setCurrentIndex(3)

        # CHECK INFO
        def signIn(db: str):
           schoolName = self.ui.schoolNameSignIn.text()
           if "'" in schoolName:
               schoolName = schoolName.replace("'", "''")
           email = self.ui.emailSignIn.text()
           password = self.ui.passwordSignIn.text()

           sql = f"SELECT * FROM registered_schools WHERE school_name = '{schoolName}' AND school_email = '{email}'"
           self.cursor.execute(sql)
           data = self.cursor.fetchall()
           print(data)

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
            school_name = self.ui.schoolNameSignUp.text().replace("'","''")
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
                    sql = f"INSERT INTO registered_schools (school_name, school_code, school_email, password, verified, country, location) VALUES ('{school_name}', {school_code}, '{email}', '{password}', 1, 'Ghana', 'nowhere')"
                    print(sql)
                    self.cursor.execute(sql)
                    self.connection.commit()
                    switch_screen(0)

        def getStudent(id = self.currentStudentId):
            sql = f"SELECT * FROM student_details WHERE school = '{self.school_name}'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.studentsNo = len(data)
            if self.currentStudentId == 0:
                self.ui.previous_data_button.setStyleSheet("background-color: rgb(200, 200, 200);")
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

            if self.currentStudentId == self.studentsNo:
                self.ui.next_data_button.setStyleSheet("background-color: rgb(70, 70, 70);")
            else:
                self.ui.next_data_button.setStyleSheet("""QWidget {
                        background-color: rgb(112, 112, 112);
                        padding: 0px;
                        }

                        QWidget:hover {
                            background-color: rgb(168, 168, 168);
                        }
                    """
                )

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

                months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
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
            id = self.currentStudentId + 1
            getStudent(id)

        def previousStudent():
            id = 0
            if self.currentStudentId > 1:
                id = self.currentStudentId - 1
            getStudent(id)


        self.ui.SignInSubmit_2.clicked.connect(lambda: signUp("server2.db"))
        self.ui.next_data_button.clicked.connect(lambda: nextStudent())
        self.ui.previous_data_button.clicked.connect(lambda: previousStudent())
        self.ui.take_photo.clicked.connect(lambda: camera_screen())
        self.ui.SignUpButton.clicked.connect(lambda: switch_screen(1))
        self.ui.SignUpButton_2.clicked.connect(lambda:switch_screen(0))
        self.ui.SignInSubmit.clicked.connect(lambda: signIn("server2.db"))

        def switch_screen(screen: int):
            self.ui.stackedWidget.setCurrentIndex(screen)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################

    def selectCamera(self, i):
        # self.camera = QCamera(self.availableCameras[i])
        # self.camera.setViewfinder(self.viewFinder)
        # self.camera.setCaptureMode(QCamera.CaptureStillImage)
        # self.camera.error.connect(lambda:
        #                           self.alert(self.camera.errorString()))
        # self.camera.start()
        # self.capture = QCameraImageCapture(self.camera)
        # self.capture.error.connect(lambda d, i:
        #                            self.status.showMessage(
        #                                f'Image Captured {str(self.saveSeq)}'))
        # self.currentCameraName = self.availableCameras[i].description()
        # self.saveSeq = 0
        "TODO"

    def clickPhoto(self):
        "TODO"

    def alert(self, msg):
        error = QErrorMessage(self)
        error.showMessage(msg)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())