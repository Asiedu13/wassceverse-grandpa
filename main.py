import sqlite3
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

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

        connection = sqlite3.connect("server2.db")
        cursor = connection.cursor()
        statement = "SELECT school_name from registered_schools"
        cursor.execute(statement)
        data = cursor.fetchall()
        schools = []
        for d in data:
            schools.append(d[0])
        cursor.close()
        print(schools)
        completer = QCompleter(schools)
        self.ui.schoolNameSignIn.setCompleter(completer)

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
            connection = sqlite3.connect(db)
            cursor = connection.cursor()

            sql = f"SELECT * FROM registered_schools WHERE school_name = '{schoolName}' AND school_email = '{email}'"
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)

            if len(data) == 1:
                "TODO"
                # if password != data[6]:
                #     dialog = PasswordIncorrectDialog(self)
                #     dialog.exec()
                # else:
                #     "TODO"
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
        self.ui.stackedWidget.setCurrentIndex(0)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())