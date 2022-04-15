import json
from multiprocessing.connection import Connection
import sys
import glob
import os
import sqlite3
import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from numpy import double

# GUI FILE
import ui_classes.edit
from ui_classes.ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

rows_ = None
edit_pic_path = ""


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def getId(connection: Connection):
            cursor = connection.cursor()
            num = self.ui.info.item(11).text().replace(
                "BECE Index Number: ", "")
            cursor.execute(
                f"SELECT id from student_details WHERE indexNum = '{num}'")
            id = cursor.fetchall()[0][0]
            return id

        def getRows(connection: Connection):
            cursor = connection.cursor()
            num = self.ui.info.item(11).text().replace(
                "BECE Index Number: ", "")
            cursor.execute(
                f"SELECT id from student_details")
            length = cursor.fetchall()
            return len(length)

        def ButtonGone(id, connection):
            if getRows(connection) <= 1:
                self.ui.previous_arrow.setStyleSheet(
                    "QPushButton {\n"
                    "color: rgb(219, 216, 227);\n"
                    "background-color: rgb(104, 105, 107);\n"
                    "border-radius: 15px;\n"
                    "font-size: 14px;\n"
                    "font-family: Montserrat;\n"
                    "}\n")
                self.ui.next_arrow.setStyleSheet(
                    "QPushButton {\n"
                    "color: rgb(219, 216, 227);\n"
                    "background-color: rgb(104, 105, 107);\n"
                    "border-radius: 15px;\n"
                    "font-size: 14px;\n"
                    "font-family: Montserrat;\n"
                    "}\n")
            else:
                if id == 1:
                    self.ui.previous_arrow.setStyleSheet(
                        "QPushButton {\n"
                        "color: rgb(219, 216, 227);\n"
                        "background-color: rgb(104, 105, 107);\n"
                        "border-radius: 15px;\n"
                        "font-size: 14px;\n"
                        "font-family: Montserrat;\n"
                        "}\n")
                    self.ui.next_arrow.setStyleSheet("QPushButton {\n"
                                                     "color: rgb(219, 216, 227);\n"
                                                     "background-color: rgb(92, 84, 112);\n"
                                                     "border-radius: 15px;\n"
                                                     "font-size: 14px;\n"
                                                     "font-family: Montserrat;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: rgb(111, 101, 135);\n"
                                                     "}")
                elif id == getRows(connection):
                    self.ui.next_arrow.setStyleSheet(
                        "QPushButton {\n"
                        "color: rgb(219, 216, 227);\n"
                        "background-color: rgb(104, 105, 107);\n"
                        "border-radius: 15px;\n"
                        "font-size: 14px;\n"
                        "font-family: Montserrat;\n"
                        "}\n")
                    self.ui.previous_arrow.setStyleSheet("QPushButton {\n"
                                                         "color: rgb(219, 216, 227);\n"
                                                         "background-color: rgb(92, 84, 112);\n"
                                                         "border-radius: 15px;\n"
                                                         "font-size: 14px;\n"
                                                         "font-family: Montserrat;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton:hover {\n"
                                                         "    background-color: rgb(111, 101, 135);\n"
                                                         "}")
                else:
                    self.ui.previous_arrow.setStyleSheet("QPushButton {\n"
                                                         "color: rgb(219, 216, 227);\n"
                                                         "background-color: rgb(92, 84, 112);\n"
                                                         "border-radius: 15px;\n"
                                                         "font-size: 14px;\n"
                                                         "font-family: Montserrat;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton:hover {\n"
                                                         "    background-color: rgb(111, 101, 135);\n"
                                                         "}")
                    self.ui.next_arrow.setStyleSheet("QPushButton {\n"
                                                     "color: rgb(219, 216, 227);\n"
                                                     "background-color: rgb(92, 84, 112);\n"
                                                     "border-radius: 15px;\n"
                                                     "font-size: 14px;\n"
                                                     "font-family: Montserrat;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: rgb(111, 101, 135);\n"
                                                     "}")

        def getFromServer(connection, id=1):
            global rows_
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student_details")
            rows = cursor.fetchall()
            rows_ = rows
            pic_data = rows[id-1][9]
            qImg = QtGui.QImage.fromData(pic_data)
            pixmap = QtGui.QPixmap.fromImage(qImg)

            self.ui.pic.setPixmap(pixmap)
            self.ui.info.item(0).setText(QCoreApplication.translate(
                "MainWindow", f"Name: {rows[id-1][0]} {rows[id-1][1]} {rows[id-1][2]}"))
            self.ui.info.item(1).setText(QCoreApplication.translate(
                "MainWindow", f"School: {rows[id-1][10]}"))
            self.ui.info.item(2).setText(QCoreApplication.translate(
                "MainWindow", f"Class: {rows[id-1][5]}"))
            self.ui.info.item(3).setText(QCoreApplication.translate(
                "MainWindow", f"Course: {rows[id-1][4]}"))
            list_ = rows[id-1][8].strip('][').split(', ')
            self.ui.info.item(5).setText(QCoreApplication.translate(
                "MainWindow", f"    {list_[0]}"))
            self.ui.info.item(6).setText(QCoreApplication.translate(
                "MainWindow", f"    {list_[1]}"))
            self.ui.info.item(7).setText(QCoreApplication.translate(
                "MainWindow", f"    {list_[2]}"))
            self.ui.info.item(8).setText(QCoreApplication.translate(
                "MainWindow", f"    {list_[3]}"))
            self.ui.info.item(9).setText(QCoreApplication.translate(
                "MainWindow", f"Date of Birth: {rows[id-1][3]}"))
            self.ui.info.item(10).setText(QCoreApplication.translate(
                "MainWindow", f"Gender: {rows[id-1][11]}"))
            self.ui.info.item(11).setText(QCoreApplication.translate(
                "MainWindow", f"BECE Index Number: {rows[id-1][6]}"))
            self.ui.info.item(12).setText(QCoreApplication.translate(
                "MainWindow", f"Parent's Contact: {rows[id-1][12]}"))
            ButtonGone(getId(connection), connection)

        try:
            connection = sqlite3.connect('server.db')
            cursor = connection.cursor()
            jsonFile = open("web/details.txt", "r")
            jsonContent = jsonFile.readlines()
            for line in jsonContent:
                dict_ = json.loads(line)
                surname = dict_['lastName']
                first_name = dict_['firstName']
                other_names = dict_['otherNames']
                dob = dict_['DOB']
                course = dict_['course'][0]
                class_ = None
                indexNum = dict_['beceIndex']
                yearCompleted = dict_['yearCompleted']
                electives = dict_['electives']
                image_ = None
                school = dict_['school']
                gender = dict_['gender'][0].title()
                parent_contact = dict_['parentContact']
                signature = None
                fingerprint = None
                if line != "":
                    cursor.execute(
                        f"INSERT INTO student_details (surname, first_name, other_names, date_of_birth, course, class, indexNum, yearCompleted, electives, school, gender, parents_contact) VALUES ({surname}, {first_name}, {other_names}, {dob}, {course}, {class_}, {indexNum}, {yearCompleted}, {electives}, {school}', {gender}, {parent_contact});")

        except sqlite3.Error:
            print(sqlite3.Error)
        getFromServer(connection)

        def cropFile(mode="normal"):
            global edit_pic_path
            fname = QFileDialog.getOpenFileName(self, 'Select file',
                                                'c:\\', "Image files (*.jpg *.png *.tiff)")
            fpath = fname[0]

            img = cv2.imread(fpath)

            width, height = 150, 200
            imgResized = cv2.resize(img, (width, height))
            if os.path.isdir(os.path.dirname(fpath)+"/edited/") == False:
                os.makedirs(os.path.dirname(fpath)+"/edited/")
            new_path = os.path.dirname(
                fpath)+"/edited/"+fpath.replace(os.path.dirname(fpath)+"/", "")+".png"
            cv2.imwrite(new_path, imgResized)

        def cropFolder():
            fname = QFileDialog.getExistingDirectory(
                self, 'Select Folder', 'c:\\')
            print(fname)
            files = glob.glob(f'{fname}/**/*.jpg', recursive=True) + \
                glob.glob(f'{fname}/**/*.png', recursive=True) + \
                glob.glob(f'{fname}/**/*.', recursive=True)

            # For each image
            for file in files:
                fpath = file.replace("\\", "/")
                print(fpath)
                img = cv2.imread(fpath)

                width, height = 150, 200
                imgResized = cv2.resize(img, (width, height))
                if os.path.isdir(os.path.dirname(fpath)+"/edited/") == False:
                    os.makedirs(os.path.dirname(fpath)+"/edited/")
                new_path = os.path.dirname(
                    fpath)+"/edited/"+fpath.replace(os.path.dirname(fpath)+"/.temp/", "")+".png"
                cv2.imwrite(new_path, imgResized)

        def save(connection, id):
            cursor = connection.cursor()
            dlg = QtWidgets.QDialog()
            dlg.ui = ui_classes.edit.Ui_Dialog()
            surname = dlg.ui.plainTextEdit.text()
            first_name = dlg.ui.plainTextEdit_2.text()
            other_names = dlg.ui.plainTextEdit_3.text()
            school = dlg.ui.plainTextEdit_6.text()
            date = str(dlg.ui.dateEdit.date())
            """index = dlg.ui.comboBox.findText(
                f"{row[id-1][4]}", QtCore.Qt.MatchFixedString)
            if index >= 0:
                dlg.ui.comboBox.setCurrentIndex(index)
            dlg.ui.textEdit.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][5]}"))
            dlg.ui.plainTextEdit_4.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][6]}"))
            year = int(row[id-1][7])
            dlg.ui.dateEdit.setDate(
                QDate(year, 0, 0))
            checks = dlg.ui.frame_20.findChildren(QCheckBox)
            elect = row[id-1][8].strip('][').split(', ')
            for check in checks:
                if check.text() in elect:
                    check.setChecked(True)
                else:
                    check.setChecked(False)
            radio = dlg.ui.frame_8.findChildren(QRadioButton)
            for r in radio:
                if r.text() == row[id-1][11]:
                    r.setChecked(True)
                else:
                    r.setChecked(False)
            dlg.ui.plainTextEdit_5.setPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][12]}"))"""

        def edit(connection, id, row):
            print("click")
            dlg = QtWidgets.QDialog()
            dlg.ui = ui_classes.edit.Ui_Dialog()
            dlg.ui.setupUi(dlg)
            print(row[id-1][1])

            def editCropFile():
                global edit_pic_path
                fname = QFileDialog.getOpenFileName(self, 'Select file',
                                                    'c:\\', "Image files (*.jpg *.png *.tiff)")
                fpath = fname[0]

                img = cv2.imread(fpath)

                width, height = 150, 200
                imgResized = cv2.resize(img, (width, height))
                if os.path.isdir(os.path.dirname(fpath)+"/edited/") == False:
                    os.makedirs(os.path.dirname(fpath)+"/edited/")
                new_path = os.path.dirname(
                    fpath)+"/edited/"+fpath.replace(os.path.dirname(fpath)+"/", "")+".png"
                cv2.imwrite(new_path, imgResized)
                dlg.ui.label_19.setText(QCoreApplication.translate(
                    "Dialog", f"{new_path}"))
            getFromServer(connection, id)
            dlg.ui.plainTextEdit.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][0]}"))
            dlg.ui.plainTextEdit_2.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][1]}"))
            dlg.ui.plainTextEdit_3.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][2]}"))
            dlg.ui.plainTextEdit_6.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][10]}"))
            date = row[id-1][3].split("/")
            dlg.ui.dateEdit.setDate(
                QDate(int(date[2]), int(date[1]), int(date[0])))
            index = dlg.ui.comboBox.findText(
                f"{row[id-1][4]}", QtCore.Qt.MatchFixedString)
            if index >= 0:
                dlg.ui.comboBox.setCurrentIndex(index)
            dlg.ui.textEdit.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][5]}"))
            dlg.ui.plainTextEdit_4.insertPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][6]}"))
            year = int(row[id-1][7])
            dlg.ui.dateEdit.setDate(
                QDate(year, 0, 0))
            checks = dlg.ui.frame_20.findChildren(QCheckBox)
            elect = row[id-1][8].strip('][').split(', ')
            for check in checks:
                if check.text() in elect:
                    check.setChecked(True)
                else:
                    check.setChecked(False)
            radio = dlg.ui.frame_8.findChildren(QRadioButton)
            for r in radio:
                if r.text() == row[id-1][11]:
                    r.setChecked(True)
                else:
                    r.setChecked(False)
            dlg.ui.plainTextEdit_5.setPlainText(QCoreApplication.translate(
                "Dialog", f"{row[id-1][12]}"))
            dlg.ui.pushButton.clicked.connect(lambda: editCropFile())

            dlg.ui.buttonBox.clicked.connect(dlg.accept)
            dlg.ui.buttonBox.accepted.connect(
                lambda: save(connection, getId(connection)))
            dlg.ui.buttonBox.rejected.connect(dlg.reject)

            dlg.exec_()
            dlg.show()
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

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        # SET BUTTON FUNCTIONS
        self.ui.import_file.clicked.connect(lambda: cropFile())
        self.ui.import_folder.clicked.connect(lambda: cropFolder())
        self.ui.server_info.clicked.connect(lambda: getFromServer(connection))
        self.ui.previous_arrow.clicked.connect(
            lambda: getFromServer(connection, (getId(connection) - 1) if getId(connection) > 1 else 1))
        self.ui.next_arrow.clicked.connect(
            lambda: getFromServer(connection, (getId(connection) + 1) if getRows(connection) < getId(connection) else getRows(connection)))
        self.ui.edit_btn.clicked.connect(
            lambda: edit(connection, getId(connection), rows_))

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    # APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
