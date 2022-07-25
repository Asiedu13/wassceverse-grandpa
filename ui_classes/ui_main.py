# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainsVwzhF.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius: 16px;")
        self.centralWidgetLaayout = QVBoxLayout(self.centralwidget)
        self.centralWidgetLaayout.setSpacing(1)
        self.centralWidgetLaayout.setObjectName(u"centralWidgetLaayout")
        self.centralWidgetLaayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 22))
        self.title_bar.setMaximumSize(QSize(16777215, 22))
        self.title_bar.setStyleSheet(u"background-color: #f2f4ee;")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.title_bar)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.title_bar)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.title_bar)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(100, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_12)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(18, 18))
        self.btn_minimize.setMaximumSize(QSize(18, 18))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"border-radius: 9px;\n"
"background-color: rgb(0, 189, 91);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 255, 119);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_12)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(18, 18))
        self.btn_maximize.setMaximumSize(QSize(18, 18))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"border-radius: 9px;\n"
"background-color: rgb(0, 133, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 170, 255);\n"
"}")
        self.btn_maximize.setProperty("Maximized", False)

        self.horizontalLayout_6.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_12)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(18, 18))
        self.btn_close.setMaximumSize(QSize(18, 18))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"border-radius: 9px;\n"
"background-color: rgb(227, 20, 20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 22, 22);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.horizontalLayout_5.addWidget(self.frame_12)


        self.centralWidgetLaayout.addWidget(self.title_bar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setFamily(u"Arial")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"border-radius: 0 0 20px 20px;\n"
"background-color:#f2f4ee;")
        self.signIn = QWidget()
        self.signIn.setObjectName(u"signIn")
        self.signIn.setStyleSheet(u"background-color: #f2f4ee;")
        self.signInLayout = QVBoxLayout(self.signIn)
        self.signInLayout.setSpacing(0)
        self.signInLayout.setObjectName(u"signInLayout")
        self.signInLayout.setContentsMargins(70, 70, 70, 70)
        self.background = QFrame(self.signIn)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 30px;")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.SignInBackgroundLayout = QHBoxLayout(self.background)
        self.SignInBackgroundLayout.setSpacing(0)
        self.SignInBackgroundLayout.setObjectName(u"SignInBackgroundLayout")
        self.SignInBackgroundLayout.setContentsMargins(0, 0, 0, 0)
        self.SignInInfoFrame = QFrame(self.background)
        self.SignInInfoFrame.setObjectName(u"SignInInfoFrame")
        self.SignInInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.SignInInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.SignInInfoFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signInLeftTopSpacer = QFrame(self.SignInInfoFrame)
        self.signInLeftTopSpacer.setObjectName(u"signInLeftTopSpacer")
        self.signInLeftTopSpacer.setFrameShape(QFrame.StyledPanel)
        self.signInLeftTopSpacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.signInLeftTopSpacer)

        self.SignInInfoTop = QLabel(self.SignInInfoFrame)
        self.SignInInfoTop.setObjectName(u"SignInInfoTop")
        self.SignInInfoTop.setMaximumSize(QSize(16777215, 80))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(16)
        self.SignInInfoTop.setFont(font1)
        self.SignInInfoTop.setTextFormat(Qt.AutoText)
        self.SignInInfoTop.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.SignInInfoTop)

        self.SignInInfoBottom = QLabel(self.SignInInfoFrame)
        self.SignInInfoBottom.setObjectName(u"SignInInfoBottom")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(9)
        font2.setKerning(True)
        self.SignInInfoBottom.setFont(font2)
        self.SignInInfoBottom.setLineWidth(1)
        self.SignInInfoBottom.setMidLineWidth(0)
        self.SignInInfoBottom.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.SignInInfoBottom.setMargin(9)

        self.verticalLayout.addWidget(self.SignInInfoBottom)

        self.signInLeftBottomSpacer = QFrame(self.SignInInfoFrame)
        self.signInLeftBottomSpacer.setObjectName(u"signInLeftBottomSpacer")
        self.signInLeftBottomSpacer.setFrameShape(QFrame.StyledPanel)
        self.signInLeftBottomSpacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.signInLeftBottomSpacer)


        self.SignInBackgroundLayout.addWidget(self.SignInInfoFrame)

        self.divider = QFrame(self.background)
        self.divider.setObjectName(u"divider")
        self.divider.setMaximumSize(QSize(3, 16777215))
        self.divider.setSizeIncrement(QSize(0, 0))
        self.divider.setAutoFillBackground(False)
        self.divider.setStyleSheet(u"background-color:#414844;\n"
"border-radius:3px;\n"
"margin-top: 20px;\n"
"margin-bottom: 20px;")
        self.divider.setFrameShape(QFrame.StyledPanel)
        self.divider.setFrameShadow(QFrame.Raised)
        self.divider.setLineWidth(0)

        self.SignInBackgroundLayout.addWidget(self.divider)

        self.SignInFrame = QFrame(self.background)
        self.SignInFrame.setObjectName(u"SignInFrame")
        self.SignInFrame.setMinimumSize(QSize(0, 350))
        self.SignInFrame.setFrameShape(QFrame.StyledPanel)
        self.SignInFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SignInFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.frame_9 = QFrame(self.SignInFrame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(400, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(22)
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.SchoolNameFrame = QFrame(self.SignInFrame)
        self.SchoolNameFrame.setObjectName(u"SchoolNameFrame")
        self.SchoolNameFrame.setMinimumSize(QSize(400, 70))
        self.SchoolNameFrame.setMaximumSize(QSize(16777215, 70))
        self.SchoolNameFrame.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.SchoolNameFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SchoolNameSignInLabel = QLabel(self.SchoolNameFrame)
        self.SchoolNameSignInLabel.setObjectName(u"SchoolNameSignInLabel")
        self.SchoolNameSignInLabel.setMaximumSize(QSize(16777215, 19))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.SchoolNameSignInLabel.setFont(font4)

        self.verticalLayout_3.addWidget(self.SchoolNameSignInLabel)

        self.SchoolNameBorder = QFrame(self.SchoolNameFrame)
        self.SchoolNameBorder.setObjectName(u"SchoolNameBorder")
        self.SchoolNameBorder.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.SchoolNameBorder)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame_2 = QFrame(self.SchoolNameBorder)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.schoolNameSignIn = QLineEdit(self.frame_2)
        self.schoolNameSignIn.setObjectName(u"schoolNameSignIn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schoolNameSignIn.sizePolicy().hasHeightForWidth())
        self.schoolNameSignIn.setSizePolicy(sizePolicy)
        self.schoolNameSignIn.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_4.addWidget(self.schoolNameSignIn)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.SchoolNameBorder)

        self.SchoolNameBorder.raise_()
        self.SchoolNameSignInLabel.raise_()

        self.verticalLayout_2.addWidget(self.SchoolNameFrame)

        self.EmailSignInFrame = QFrame(self.SignInFrame)
        self.EmailSignInFrame.setObjectName(u"EmailSignInFrame")
        self.EmailSignInFrame.setMinimumSize(QSize(400, 70))
        self.EmailSignInFrame.setMaximumSize(QSize(16777215, 70))
        self.EmailSignInFrame.setFrameShape(QFrame.StyledPanel)
        self.EmailSignInFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.EmailSignInFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.EmailSignInFrame)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_3.setFont(font5)

        self.verticalLayout_8.addWidget(self.label_3)

        self.SchoolNameBorder_3 = QFrame(self.EmailSignInFrame)
        self.SchoolNameBorder_3.setObjectName(u"SchoolNameBorder_3")
        self.SchoolNameBorder_3.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_3.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_3.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.SchoolNameBorder_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.frame_4 = QFrame(self.SchoolNameBorder_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(600, 35))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.emailSignIn = QLineEdit(self.frame_4)
        self.emailSignIn.setObjectName(u"emailSignIn")
        sizePolicy.setHeightForWidth(self.emailSignIn.sizePolicy().hasHeightForWidth())
        self.emailSignIn.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setStyleStrategy(QFont.PreferDefault)
        self.emailSignIn.setFont(font6)

        self.verticalLayout_7.addWidget(self.emailSignIn)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.SchoolNameBorder_3)


        self.verticalLayout_2.addWidget(self.EmailSignInFrame)

        self.PasswordSignInFrame = QFrame(self.SignInFrame)
        self.PasswordSignInFrame.setObjectName(u"PasswordSignInFrame")
        self.PasswordSignInFrame.setMinimumSize(QSize(400, 70))
        self.PasswordSignInFrame.setMaximumSize(QSize(16777215, 70))
        self.PasswordSignInFrame.setFrameShape(QFrame.StyledPanel)
        self.PasswordSignInFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.PasswordSignInFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.PasswordSignInFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.SchoolNameBorder_2 = QFrame(self.PasswordSignInFrame)
        self.SchoolNameBorder_2.setObjectName(u"SchoolNameBorder_2")
        self.SchoolNameBorder_2.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_2.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_2.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.SchoolNameBorder_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame_3 = QFrame(self.SchoolNameBorder_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 35))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.passwordSignIn = QLineEdit(self.frame_3)
        self.passwordSignIn.setObjectName(u"passwordSignIn")
        sizePolicy.setHeightForWidth(self.passwordSignIn.sizePolicy().hasHeightForWidth())
        self.passwordSignIn.setSizePolicy(sizePolicy)
        self.passwordSignIn.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.passwordSignIn)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.SchoolNameBorder_2)


        self.verticalLayout_2.addWidget(self.PasswordSignInFrame)

        self.frame_5 = QFrame(self.SignInFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(63, 16777215))
        self.label_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.SignUpButton = QPushButton(self.frame_5)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setMaximumSize(QSize(108, 16777215))
        self.SignUpButton.setFont(font4)
        self.SignUpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignUpButton.setStyleSheet(u"color:#414844;")
        self.SignUpButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.SignUpButton)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_6)

        self.SignInSubmit = QPushButton(self.frame_5)
        self.SignInSubmit.setObjectName(u"SignInSubmit")
        self.SignInSubmit.setMinimumSize(QSize(80, 40))
        self.SignInSubmit.setMaximumSize(QSize(80, 16777215))
        font7 = QFont()
        font7.setFamily(u"Arial Black")
        font7.setPointSize(10)
        self.SignInSubmit.setFont(font7)
        self.SignInSubmit.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(213, 93, 33);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(185, 80, 28);\n"
"}")

        self.horizontalLayout_4.addWidget(self.SignInSubmit)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(90, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.SignInFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_8)


        self.SignInBackgroundLayout.addWidget(self.SignInFrame, 0, Qt.AlignHCenter)


        self.signInLayout.addWidget(self.background)

        self.stackedWidget.addWidget(self.signIn)
        self.signUp = QWidget()
        self.signUp.setObjectName(u"signUp")
        self.horizontalLayout_11 = QHBoxLayout(self.signUp)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(70, 70, 70, 70)
        self.background_2 = QFrame(self.signUp)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 30px;")
        self.background_2.setFrameShape(QFrame.StyledPanel)
        self.background_2.setFrameShadow(QFrame.Raised)
        self.SignInBackgroundLayout_2 = QHBoxLayout(self.background_2)
        self.SignInBackgroundLayout_2.setSpacing(0)
        self.SignInBackgroundLayout_2.setObjectName(u"SignInBackgroundLayout_2")
        self.SignInBackgroundLayout_2.setContentsMargins(0, 0, 0, 0)
        self.SignInFrame_2 = QFrame(self.background_2)
        self.SignInFrame_2.setObjectName(u"SignInFrame_2")
        self.SignInFrame_2.setFrameShape(QFrame.StyledPanel)
        self.SignInFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.SignInFrame_2)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, 9, -1)
        self.frame_13 = QFrame(self.SignInFrame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.SchoolNameFrame_2 = QFrame(self.SignInFrame_2)
        self.SchoolNameFrame_2.setObjectName(u"SchoolNameFrame_2")
        self.SchoolNameFrame_2.setMaximumSize(QSize(420, 90))
        self.SchoolNameFrame_2.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.SchoolNameFrame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.SchoolNameSignInLabel_2 = QLabel(self.SchoolNameFrame_2)
        self.SchoolNameSignInLabel_2.setObjectName(u"SchoolNameSignInLabel_2")
        self.SchoolNameSignInLabel_2.setMaximumSize(QSize(16777215, 19))
        self.SchoolNameSignInLabel_2.setFont(font4)

        self.verticalLayout_12.addWidget(self.SchoolNameSignInLabel_2)

        self.SchoolNameBorder_4 = QFrame(self.SchoolNameFrame_2)
        self.SchoolNameBorder_4.setObjectName(u"SchoolNameBorder_4")
        self.SchoolNameBorder_4.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_4.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_4.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.SchoolNameBorder_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.frame_14 = QFrame(self.SchoolNameBorder_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 35))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.schoolNameSignUp = QLineEdit(self.frame_14)
        self.schoolNameSignUp.setObjectName(u"schoolNameSignUp")
        sizePolicy.setHeightForWidth(self.schoolNameSignUp.sizePolicy().hasHeightForWidth())
        self.schoolNameSignUp.setSizePolicy(sizePolicy)
        self.schoolNameSignUp.setMinimumSize(QSize(0, 25))

        self.verticalLayout_13.addWidget(self.schoolNameSignUp)


        self.horizontalLayout_7.addWidget(self.frame_14)


        self.verticalLayout_12.addWidget(self.SchoolNameBorder_4)


        self.verticalLayout_11.addWidget(self.SchoolNameFrame_2)

        self.EmailSignInFrame_2 = QFrame(self.SignInFrame_2)
        self.EmailSignInFrame_2.setObjectName(u"EmailSignInFrame_2")
        self.EmailSignInFrame_2.setMaximumSize(QSize(600, 90))
        self.EmailSignInFrame_2.setFrameShape(QFrame.StyledPanel)
        self.EmailSignInFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.EmailSignInFrame_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.EmailSignInFrame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_5)

        self.SchoolNameBorder_5 = QFrame(self.EmailSignInFrame_2)
        self.SchoolNameBorder_5.setObjectName(u"SchoolNameBorder_5")
        self.SchoolNameBorder_5.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_5.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_5.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.SchoolNameBorder_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.frame_15 = QFrame(self.SchoolNameBorder_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(600, 35))
        self.frame_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.emailSignUp = QLineEdit(self.frame_15)
        self.emailSignUp.setObjectName(u"emailSignUp")
        self.emailSignUp.setMinimumSize(QSize(0, 25))

        self.verticalLayout_15.addWidget(self.emailSignUp)


        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_14.addWidget(self.SchoolNameBorder_5)


        self.verticalLayout_11.addWidget(self.EmailSignInFrame_2)

        self.frame_21 = QFrame(self.SignInFrame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setMaximumSize(QSize(420, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PasswordSignInFrame_2 = QFrame(self.frame_21)
        self.PasswordSignInFrame_2.setObjectName(u"PasswordSignInFrame_2")
        self.PasswordSignInFrame_2.setMaximumSize(QSize(200, 90))
        self.PasswordSignInFrame_2.setFrameShape(QFrame.StyledPanel)
        self.PasswordSignInFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.PasswordSignInFrame_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.PasswordSignInFrame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.SchoolNameBorder_6 = QFrame(self.PasswordSignInFrame_2)
        self.SchoolNameBorder_6.setObjectName(u"SchoolNameBorder_6")
        self.SchoolNameBorder_6.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_6.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_6.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.SchoolNameBorder_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.frame_16 = QFrame(self.SchoolNameBorder_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 35))
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.schoolTelSignUp = QLineEdit(self.frame_16)
        self.schoolTelSignUp.setObjectName(u"schoolTelSignUp")
        self.schoolTelSignUp.setMinimumSize(QSize(0, 25))

        self.verticalLayout_17.addWidget(self.schoolTelSignUp)


        self.horizontalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_16.addWidget(self.SchoolNameBorder_6)


        self.horizontalLayout_13.addWidget(self.PasswordSignInFrame_2)

        self.PasswordSignInFrame_3 = QFrame(self.frame_21)
        self.PasswordSignInFrame_3.setObjectName(u"PasswordSignInFrame_3")
        self.PasswordSignInFrame_3.setMaximumSize(QSize(200, 90))
        self.PasswordSignInFrame_3.setFrameShape(QFrame.StyledPanel)
        self.PasswordSignInFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.PasswordSignInFrame_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.PasswordSignInFrame_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_18.addWidget(self.label_8)

        self.SchoolNameBorder_7 = QFrame(self.PasswordSignInFrame_3)
        self.SchoolNameBorder_7.setObjectName(u"SchoolNameBorder_7")
        self.SchoolNameBorder_7.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_7.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_7.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.SchoolNameBorder_7)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.frame_22 = QFrame(self.SchoolNameBorder_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 35))
        self.frame_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.passwordSignUp = QLineEdit(self.frame_22)
        self.passwordSignUp.setObjectName(u"passwordSignUp")
        self.passwordSignUp.setMinimumSize(QSize(0, 25))
        self.passwordSignUp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_19.addWidget(self.passwordSignUp)


        self.horizontalLayout_12.addWidget(self.frame_22)


        self.verticalLayout_18.addWidget(self.SchoolNameBorder_7)


        self.horizontalLayout_13.addWidget(self.PasswordSignInFrame_3)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.frame_17 = QFrame(self.SignInFrame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(420, 70))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 16777215))
        self.label_7.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.SignUpButton_2 = QPushButton(self.frame_17)
        self.SignUpButton_2.setObjectName(u"SignUpButton_2")
        self.SignUpButton_2.setMinimumSize(QSize(80, 0))
        self.SignUpButton_2.setMaximumSize(QSize(80, 16777215))
        self.SignUpButton_2.setFont(font4)
        self.SignUpButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignUpButton_2.setStyleSheet(u"color:#414844;")
        self.SignUpButton_2.setFlat(True)

        self.horizontalLayout_10.addWidget(self.SignUpButton_2)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(200, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_18)

        self.SignInSubmit_2 = QPushButton(self.frame_17)
        self.SignInSubmit_2.setObjectName(u"SignInSubmit_2")
        self.SignInSubmit_2.setMinimumSize(QSize(80, 40))
        self.SignInSubmit_2.setMaximumSize(QSize(80, 16777215))
        self.SignInSubmit_2.setFont(font7)
        self.SignInSubmit_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(213, 93, 33);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(185, 80, 28);\n"
"}")

        self.horizontalLayout_10.addWidget(self.SignInSubmit_2)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_20 = QFrame(self.SignInFrame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_20)


        self.SignInBackgroundLayout_2.addWidget(self.SignInFrame_2, 0, Qt.AlignHCenter)

        self.divider_2 = QFrame(self.background_2)
        self.divider_2.setObjectName(u"divider_2")
        self.divider_2.setMaximumSize(QSize(3, 16777215))
        self.divider_2.setSizeIncrement(QSize(0, 0))
        self.divider_2.setAutoFillBackground(False)
        self.divider_2.setStyleSheet(u"background-color:#414844;\n"
"border-radius:3px;\n"
"margin-top: 20px;\n"
"margin-bottom: 20px;")
        self.divider_2.setFrameShape(QFrame.StyledPanel)
        self.divider_2.setFrameShadow(QFrame.Raised)
        self.divider_2.setLineWidth(0)

        self.SignInBackgroundLayout_2.addWidget(self.divider_2)

        self.SignInInfoFrame_2 = QFrame(self.background_2)
        self.SignInInfoFrame_2.setObjectName(u"SignInInfoFrame_2")
        self.SignInInfoFrame_2.setMinimumSize(QSize(250, 0))
        self.SignInInfoFrame_2.setMaximumSize(QSize(16777215, 600))
        self.SignInInfoFrame_2.setFrameShape(QFrame.StyledPanel)
        self.SignInInfoFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.SignInInfoFrame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.signInLeftTopSpacer_2 = QFrame(self.SignInInfoFrame_2)
        self.signInLeftTopSpacer_2.setObjectName(u"signInLeftTopSpacer_2")
        self.signInLeftTopSpacer_2.setFrameShape(QFrame.StyledPanel)
        self.signInLeftTopSpacer_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.signInLeftTopSpacer_2)

        self.SignInInfoTop_2 = QLabel(self.SignInInfoFrame_2)
        self.SignInInfoTop_2.setObjectName(u"SignInInfoTop_2")
        self.SignInInfoTop_2.setMaximumSize(QSize(16777215, 80))
        self.SignInInfoTop_2.setFont(font1)
        self.SignInInfoTop_2.setTextFormat(Qt.AutoText)
        self.SignInInfoTop_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_10.addWidget(self.SignInInfoTop_2)

        self.SignInInfoBottom_2 = QLabel(self.SignInInfoFrame_2)
        self.SignInInfoBottom_2.setObjectName(u"SignInInfoBottom_2")
        self.SignInInfoBottom_2.setFont(font2)
        self.SignInInfoBottom_2.setLineWidth(1)
        self.SignInInfoBottom_2.setMidLineWidth(0)
        self.SignInInfoBottom_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.SignInInfoBottom_2.setMargin(9)

        self.verticalLayout_10.addWidget(self.SignInInfoBottom_2)

        self.signInLeftBottomSpacer_2 = QFrame(self.SignInInfoFrame_2)
        self.signInLeftBottomSpacer_2.setObjectName(u"signInLeftBottomSpacer_2")
        self.signInLeftBottomSpacer_2.setFrameShape(QFrame.StyledPanel)
        self.signInLeftBottomSpacer_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.signInLeftBottomSpacer_2)


        self.SignInBackgroundLayout_2.addWidget(self.SignInInfoFrame_2)


        self.horizontalLayout_11.addWidget(self.background_2)

        self.stackedWidget.addWidget(self.signUp)

        self.centralWidgetLaayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_maximize.clicked.connect(MainWindow.showMaximized)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#414844;\">WASSCEVerse</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.SignInInfoTop.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#414844;\">WELOME BACK!</span></p></body></html>", None))
        self.SignInInfoBottom.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">To keep connected with us</span><span style=\" font-size:12pt;\"><br/></span><span style=\" font-size:12pt; color:#000000;\">Please sign in with your</span><span style=\" font-size:12pt;\"><br/></span><span style=\" font-size:12pt; color:#000000;\">personal info</span><span style=\" font-size:12pt;\"/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.SchoolNameSignInLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">School Name:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Email:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Password:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New User?", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"Create an Account", None))
        self.SignInSubmit.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#414844;\">Create Account</span></p></body></html>", None))
        self.SchoolNameSignInLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">School Name:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Email:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">School Tel:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Password:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Already A User?", None))
        self.SignUpButton_2.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.SignInSubmit_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.SignInInfoTop_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">HELLO, ADMIN!</span></p></body></html>", None))
        self.SignInInfoBottom_2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<head/>\n"
"<body>\n"
"<p  style=\"line-height: 1\">\n"
"<span align=\"center\" style=\" color:black;\">Enter school details to start</span><br>\n"
"<span align=\"center\" style=\" color:black;\">your journey with us</span>\n"
"</p>\n"
"</body>\n"
"</html>", None))
    # retranslateUi

