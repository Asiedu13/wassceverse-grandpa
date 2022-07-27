import sqlite3
import sys
import pathlib
import platform
import time
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtMultimedia import QCameraInfo, QCamera, QCameraImageCapture
from PySide2.QtMultimediaWidgets import QCameraViewfinder
from PySide2.QtWidgets import *

import cv2
import numpy as np
import os
from PIL import Image
from autocrop import Cropper


# GUI FILES
from ui_classes.ui_main import Ui_MainWindow
from ui_classes.signInFailedOneDialog import Ui_signInFailedOneDialog
from ui_classes.ui_incorrectDialog import Ui_incorrectDialog


# IMPORT FUNCTIONS
from ui_functions import *

BASE_DIR = pathlib.Path().home()
FOLDER_NAME = '.TEMP'

SAVE_PATH = BASE_DIR / FOLDER_NAME
SAVE_PATH.mkdir(exist_ok=True, parents=True)


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
        self.selectCamera(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.comboBox.addItems([camera.description()
                                 for camera in self.availableCameras])
        connection = sqlite3.connect("server2.db")
        self.cursor = connection.cursor()
        statement = "SELECT school_name from registered_schools"
        self.cursor.execute(statement)
        data = self.cursor.fetchall()
        schools = []
        for d in data:
            schools.append(d[0])
        print(schools)
        completer = QCompleter(schools)
        self.ui.schoolNameSignIn.setCompleter(completer)

        # CHECK INFO
        def signIn(db: str):
            schoolName = self.ui.schoolNameSignIn.text()
            email = self.ui.emailSignIn.text()
            password = self.ui.passwordSignIn.text()
            cursor = self.cursor

            sql = f"""--sql
            SELECT * FROM registered_schools WHERE school_name = "{schoolName}" AND school_email = '{email}'
            """
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)

            if len(data) > 1:
                if password != data[0][6]:
                    dialog = PasswordIncorrectDialog(self)
                    dialog.exec()
                else:
                    self.school_name = schoolName
                    switch_screen(3)
            else:
                dialog = FailDialogOne(self)
                dialog.exec()

        # SET TITLE BAR
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
        self.camera = QCamera(self.availableCameras[i])
        self.camera.setViewfinder(self.viewFinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda:
                                  self.alert(self.camera.errorString()))
        self.camera.start()
        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda d, i:
                                   self.status.showMessage(
                                       f'Image Captured {str(self.saveSeq)}'))
        self.currentCameraName = self.availableCameras[i].description()
        self.saveSeq = 0

    def clickPhoto(self):
        timeStamp = time.strftime('Date %d %b %Y Time %H %M %S')
        fileName = f'Webcam {self.currentCameraName} {timeStamp} .jpg'
        if self.savePath:
            savePath = self.savePath / fileName
        else:
            savePath = SAVE_PATH / fileName
        self.saveImage(str(savePath))
        print('Image saved on ', str(savePath))
        self.saveSeq += 1

    def alert(self, msg):
        error = QErrorMessage(self)
        error.showMessage(msg)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())