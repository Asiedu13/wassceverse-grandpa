import sqlite3
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_classes.ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        # GET DATA FROM TEXTEDITS
        def getSignInInfo():
            schoolName = self.ui.schoolNameSignIn.toPlainText()
            email = self.ui.emailSignIn.toPlainText()
            password = self.ui.passwordSignIn.toPlainText()
            return schoolName, email, password

        # CHECK INFO
        def signIn(schoolName: str, email: str, password: str, db: str):
            connection = sqlite3.connect(db)
            cursor = connection.cursor()

            sql = """
            SELECT * FROM registered_schools WHERE schoolName = "?" AND email = "?"
            """
            cursor.execute(sql, (schoolName, email))
            data = cursor.fetchall()
            print(data)

        def submitSignIn(db: str):
            schoolName, email, password = getSignInInfo()
            signIn(schoolName, email, password, db)

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.ui.SignUpButton.clicked.connect(lambda: switch_screen(1))
        self.ui.SignUpButton_2.clicked.connect(lambda:switch_screen(0))
        self.ui.SignInSubmit.clicked.connect(lambda: submitSignIn("server2.db"))

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