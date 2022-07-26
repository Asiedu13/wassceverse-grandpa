import sqlite3
import sys
import platform
from turtle import width
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
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

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(self.port)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

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
        ports = self.list_camera_ports()

        self.thread = VideoThread(0)

        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # CHECK INFO
        def signIn(db: str):
            schoolName = self.ui.schoolNameSignIn.text()
            email = self.ui.emailSignIn.text()
            password = self.ui.passwordSignIn.text()
            cursor = self.cursor

            sql = f"SELECT * FROM registered_schools WHERE school_name = '{schoolName}'"
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)

            if len(data) == 1:
                if password != data[6]:
                    dialog = PasswordIncorrectDialog(self)
                    dialog.exec()
                else:
                    "TODO"
            else:
                dialog = FailDialogOne(self)
                dialog.exec()

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.ui.SignUpButton.clicked.connect(lambda: switch_screen(1))
        self.ui.SignUpButton_2.clicked.connect(lambda:switch_screen(0))
        self.ui.SignInSubmit.clicked.connect(lambda: signIn("server2.db"))

        def switch_screen(screen: int):
            self.ui.stackedWidget.setCurrentIndex(screen)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)
        self.ui.stackedWidget.setCurrentIndex(5)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def list_camera_ports(self):
        non_working_ports = []
        test_port = 0
        available_ports = []

        while len(non_working_ports) < 6:
            camera = cv2.VideoCapture(test_port)
            if not camera.isOpened():
                non_working_ports.append(test_port)
            else:
                available_ports.append(test_port)
            test_port += 1
        return available_ports


    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the camera_input with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.camera_input.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.ui.camera_input.geometry().width(), self.ui.camera_input.geometry().height(), Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())