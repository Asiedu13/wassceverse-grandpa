# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainuiKqqX.ui'
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

from PySide2.QtMultimediaWidgets import QCameraViewfinder


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
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
        self.SignInFrame.setMinimumSize(QSize(500, 350))
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
        self.SignInFrame_2.setMinimumSize(QSize(500, 0))
        self.SignInFrame_2.setFrameShape(QFrame.StyledPanel)
        self.SignInFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.SignInFrame_2)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, 9, -1)
        self.frame_13 = QFrame(self.SignInFrame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 120))
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
        self.SchoolNameFrame_2.setMaximumSize(QSize(500, 90))
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

        self.school_name_error = QLabel(self.SchoolNameFrame_2)
        self.school_name_error.setObjectName(u"school_name_error")
        self.school_name_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_12.addWidget(self.school_name_error)


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

        self.email_error = QLabel(self.EmailSignInFrame_2)
        self.email_error.setObjectName(u"email_error")
        self.email_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_14.addWidget(self.email_error)


        self.verticalLayout_11.addWidget(self.EmailSignInFrame_2)

        self.frame_21 = QFrame(self.SignInFrame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setMaximumSize(QSize(500, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.PasswordSignInFrame_2 = QFrame(self.frame_21)
        self.PasswordSignInFrame_2.setObjectName(u"PasswordSignInFrame_2")
        self.PasswordSignInFrame_2.setMaximumSize(QSize(250, 90))
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
        self.schoolCodeSignUp = QLineEdit(self.frame_16)
        self.schoolCodeSignUp.setObjectName(u"schoolCodeSignUp")
        self.schoolCodeSignUp.setMinimumSize(QSize(0, 25))

        self.verticalLayout_17.addWidget(self.schoolCodeSignUp)


        self.horizontalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_16.addWidget(self.SchoolNameBorder_6)

        self.school_code_error = QLabel(self.PasswordSignInFrame_2)
        self.school_code_error.setObjectName(u"school_code_error")
        self.school_code_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_16.addWidget(self.school_code_error)


        self.horizontalLayout_13.addWidget(self.PasswordSignInFrame_2)

        self.PasswordSignInFrame_3 = QFrame(self.frame_21)
        self.PasswordSignInFrame_3.setObjectName(u"PasswordSignInFrame_3")
        self.PasswordSignInFrame_3.setMaximumSize(QSize(250, 90))
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

        self.password_error = QLabel(self.PasswordSignInFrame_3)
        self.password_error.setObjectName(u"password_error")
        self.password_error.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")

        self.verticalLayout_18.addWidget(self.password_error)


        self.horizontalLayout_13.addWidget(self.PasswordSignInFrame_3)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.frame_17 = QFrame(self.SignInFrame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(500, 70))
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
        self.frame_20.setMinimumSize(QSize(0, 100))
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
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.verticalLayout_20 = QVBoxLayout(self.camera)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_19 = QFrame(self.camera)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_19)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame = QFrame(self.frame_19)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_24)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.comboBox)

        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_25)


        self.verticalLayout_21.addWidget(self.frame)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.camera_input = QCameraViewfinder(self.frame_23)
        self.camera_input.setObjectName(u"camera_input")
        self.camera_input.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_18.addWidget(self.camera_input)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.frame_19)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 80))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_27)

        self.capture = QFrame(self.frame_26)
        self.capture.setObjectName(u"capture")
        self.capture.setMinimumSize(QSize(400, 0))
        self.capture.setMaximumSize(QSize(400, 60))
        self.capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.capture.setStyleSheet(u"background-color: #707070;\n"
"border-radius: 30px;")
        self.capture.setFrameShape(QFrame.StyledPanel)
        self.capture.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.capture)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.capture)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 40))
        self.label_13.setMaximumSize(QSize(50, 50))
        self.label_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);")
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setPixmap(QPixmap(u"Include/img/camera.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setMargin(0)

        self.horizontalLayout_17.addWidget(self.label_13)


        self.horizontalLayout_19.addWidget(self.capture)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_28)


        self.verticalLayout_21.addWidget(self.frame_26)


        self.verticalLayout_20.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.camera)
        self.student_details = QWidget()
        self.student_details.setObjectName(u"student_details")
        self.verticalLayout_22 = QVBoxLayout(self.student_details)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(14, 14, 14, 14)
        self.search_frame = QFrame(self.student_details)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMaximumSize(QSize(16777215, 60))
        self.search_frame.setStyleSheet(u"background-color:#f2f4ee;")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.SchoolNameBorder_8 = QFrame(self.search_frame)
        self.SchoolNameBorder_8.setObjectName(u"SchoolNameBorder_8")
        self.SchoolNameBorder_8.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_8.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_8.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.SchoolNameBorder_8)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, 1, 1, 1)
        self.frame_55 = QFrame(self.SchoolNameBorder_8)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(600, 35))
        self.frame_55.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.searchbar_main = QLineEdit(self.frame_55)
        self.searchbar_main.setObjectName(u"searchbar_main")
        sizePolicy.setHeightForWidth(self.searchbar_main.sizePolicy().hasHeightForWidth())
        self.searchbar_main.setSizePolicy(sizePolicy)
        self.searchbar_main.setFont(font6)
        self.searchbar_main.setCursor(QCursor(Qt.IBeamCursor))
        self.searchbar_main.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_37.addWidget(self.searchbar_main)

        self.close_search = QLabel(self.frame_55)
        self.close_search.setObjectName(u"close_search")
        self.close_search.setMinimumSize(QSize(25, 25))
        self.close_search.setMaximumSize(QSize(25, 25))
        self.close_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_search.setPixmap(QPixmap(u"Include/img/close.jpg"))
        self.close_search.setScaledContents(True)

        self.horizontalLayout_37.addWidget(self.close_search, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_35.addWidget(self.frame_55)


        self.horizontalLayout_36.addWidget(self.SchoolNameBorder_8)


        self.verticalLayout_22.addWidget(self.search_frame)

        self.frame_29 = QFrame(self.student_details)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(350, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.previous_data_widget = QWidget(self.frame_30)
        self.previous_data_widget.setObjectName(u"previous_data_widget")
        self.previous_data_widget.setMaximumSize(QSize(50, 16777215))
        self.previous_data_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(112, 112, 112);\n"
"padding: 0px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"	background-color: rgb(168, 168, 168);\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.previous_data_widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.previous_data = QLabel(self.previous_data_widget)
        self.previous_data.setObjectName(u"previous_data")
        self.previous_data.setMinimumSize(QSize(45, 45))
        self.previous_data.setMaximumSize(QSize(45, 45))
        self.previous_data.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.previous_data.setPixmap(QPixmap(u"Include/img/arrow_left.png"))
        self.previous_data.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.previous_data, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_21.addWidget(self.previous_data_widget)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_33)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_7 = QFrame(self.frame_33)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(180, 240))
        self.label_12.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_12)

        self.frame_32 = QFrame(self.frame_7)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.take_photo = QPushButton(self.frame_32)
        self.take_photo.setObjectName(u"take_photo")
        font8 = QFont()
        font8.setFamily(u"JetBrains Mono NL Medium")
        self.take_photo.setFont(font8)
        self.take_photo.setCursor(QCursor(Qt.PointingHandCursor))
        self.take_photo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 72, 68);\n"
"padding: 6px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;")

        self.horizontalLayout_23.addWidget(self.take_photo)

        self.import_file = QPushButton(self.frame_32)
        self.import_file.setObjectName(u"import_file")
        self.import_file.setFont(font8)
        self.import_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_file.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 72, 68);\n"
"padding: 6px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")

        self.horizontalLayout_23.addWidget(self.import_file)


        self.verticalLayout_27.addWidget(self.frame_32)


        self.verticalLayout_26.addWidget(self.frame_7)

        self.frame_38 = QFrame(self.frame_33)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 280))
        self.frame_38.setMaximumSize(QSize(16777215, 600))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_38)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_38)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 70))
        self.frame_51.setMaximumSize(QSize(16777215, 70))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label71 = QLabel(self.frame_51)
        self.label71.setObjectName(u"label71")
        self.label71.setMaximumSize(QSize(90, 16777215))
        self.label71.setSizeIncrement(QSize(0, 0))
        font9 = QFont()
        font9.setFamily(u"JetBrains Mono Medium")
        font9.setPointSize(10)
        self.label71.setFont(font9)

        self.horizontalLayout_31.addWidget(self.label71)

        self.signature = QLabel(self.frame_51)
        self.signature.setObjectName(u"signature")
        self.signature.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.signature)


        self.verticalLayout_35.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_38)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 100))
        self.frame_52.setMaximumSize(QSize(16777215, 100))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_52)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 30))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_53)
        self.label_29.setObjectName(u"label_29")
        font10 = QFont()
        font10.setFamily(u"JetBrains Mono NL ExtraBold")
        self.label_29.setFont(font10)

        self.horizontalLayout_32.addWidget(self.label_29)


        self.verticalLayout_36.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 120))
        self.frame_54.setMaximumSize(QSize(16777215, 120))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.left_thumb = QLabel(self.frame_54)
        self.left_thumb.setObjectName(u"left_thumb")
        self.left_thumb.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.left_thumb)

        self.right_thumb = QLabel(self.frame_54)
        self.right_thumb.setObjectName(u"right_thumb")
        self.right_thumb.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.right_thumb)


        self.verticalLayout_36.addWidget(self.frame_54)


        self.verticalLayout_35.addWidget(self.frame_52)


        self.verticalLayout_26.addWidget(self.frame_38)


        self.horizontalLayout_21.addWidget(self.frame_33)


        self.horizontalLayout_20.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_31)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.student_details_name = QFrame(self.frame_31)
        self.student_details_name.setObjectName(u"student_details_name")
        self.student_details_name.setMaximumSize(QSize(16777215, 70))
        self.student_details_name.setFrameShape(QFrame.StyledPanel)
        self.student_details_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.student_details_name)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_18 = QLabel(self.student_details_name)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font10)

        self.verticalLayout_25.addWidget(self.label_18)

        self.student_name = QLabel(self.student_details_name)
        self.student_name.setObjectName(u"student_name")
        self.student_name.setFont(font9)

        self.verticalLayout_25.addWidget(self.student_name)


        self.verticalLayout_23.addWidget(self.student_details_name)

        self.frame_35 = QFrame(self.frame_31)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 70))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_35)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_19 = QLabel(self.frame_35)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)

        self.verticalLayout_29.addWidget(self.label_19)

        self.student_school = QLabel(self.frame_35)
        self.student_school.setObjectName(u"student_school")
        self.student_school.setFont(font9)

        self.verticalLayout_29.addWidget(self.student_school)


        self.verticalLayout_23.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_31)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 70))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_36)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_34)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_20 = QLabel(self.frame_34)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font10)

        self.verticalLayout_30.addWidget(self.label_20)

        self.student_class = QLabel(self.frame_34)
        self.student_class.setObjectName(u"student_class")
        self.student_class.setFont(font9)

        self.verticalLayout_30.addWidget(self.student_class)


        self.horizontalLayout_24.addWidget(self.frame_34)

        self.frame_43 = QFrame(self.frame_36)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_43)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_22 = QLabel(self.frame_43)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font10)

        self.verticalLayout_31.addWidget(self.label_22)

        self.student_course = QLabel(self.frame_43)
        self.student_course.setObjectName(u"student_course")
        self.student_course.setFont(font9)

        self.verticalLayout_31.addWidget(self.student_course)


        self.horizontalLayout_24.addWidget(self.frame_43)


        self.verticalLayout_23.addWidget(self.frame_36)

        self.frame_40 = QFrame(self.frame_31)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 300))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_40)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 60))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_41)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_23 = QLabel(self.frame_41)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font10)
        self.label_23.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_32.addWidget(self.label_23)

        self.widget = QWidget(self.frame_41)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 2))
        self.widget.setStyleSheet(u"background-color: rgb(66, 72, 68);\n"
"border-radius: 1px;\n"
"margin-left: 20px;\n"
"margin-right:20px;")

        self.verticalLayout_32.addWidget(self.widget)


        self.verticalLayout_28.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_44)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.frame_46)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)

        self.horizontalLayout_26.addWidget(self.label_21)


        self.verticalLayout_33.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.frame_48)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(190, 16777215))
        self.label_24.setFont(font10)

        self.horizontalLayout_27.addWidget(self.label_24)

        self.student_gender = QLabel(self.frame_48)
        self.student_gender.setObjectName(u"student_gender")
        font11 = QFont()
        font11.setFamily(u"JetBrains Mono Medium")
        font11.setPointSize(11)
        self.student_gender.setFont(font11)

        self.horizontalLayout_27.addWidget(self.student_gender)


        self.verticalLayout_33.addWidget(self.frame_48)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_25 = QLabel(self.frame_47)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(190, 16777215))
        self.label_25.setFont(font10)

        self.horizontalLayout_28.addWidget(self.label_25)

        self.date_of_birth_label = QLabel(self.frame_47)
        self.date_of_birth_label.setObjectName(u"date_of_birth_label")
        self.date_of_birth_label.setFont(font11)

        self.horizontalLayout_28.addWidget(self.date_of_birth_label)


        self.verticalLayout_33.addWidget(self.frame_47)

        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_26 = QLabel(self.frame_50)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(190, 16777215))
        self.label_26.setFont(font10)

        self.horizontalLayout_29.addWidget(self.label_26)

        self.parent_contact = QLabel(self.frame_50)
        self.parent_contact.setObjectName(u"parent_contact")
        self.parent_contact.setFont(font11)

        self.horizontalLayout_29.addWidget(self.parent_contact)


        self.verticalLayout_33.addWidget(self.frame_50)

        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_27 = QLabel(self.frame_49)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(190, 16777215))
        self.label_27.setFont(font10)

        self.horizontalLayout_30.addWidget(self.label_27)

        self.index_number_bece = QLabel(self.frame_49)
        self.index_number_bece.setObjectName(u"index_number_bece")
        self.index_number_bece.setFont(font11)

        self.horizontalLayout_30.addWidget(self.index_number_bece)


        self.verticalLayout_33.addWidget(self.frame_49)


        self.horizontalLayout_25.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(300, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_45)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_28 = QLabel(self.frame_45)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font10)

        self.verticalLayout_34.addWidget(self.label_28)

        self.elective_1 = QLabel(self.frame_45)
        self.elective_1.setObjectName(u"elective_1")
        self.elective_1.setFont(font11)

        self.verticalLayout_34.addWidget(self.elective_1)

        self.elective_2 = QLabel(self.frame_45)
        self.elective_2.setObjectName(u"elective_2")
        self.elective_2.setFont(font11)

        self.verticalLayout_34.addWidget(self.elective_2)

        self.elective_3 = QLabel(self.frame_45)
        self.elective_3.setObjectName(u"elective_3")
        self.elective_3.setFont(font11)

        self.verticalLayout_34.addWidget(self.elective_3)

        self.elective_4 = QLabel(self.frame_45)
        self.elective_4.setObjectName(u"elective_4")
        self.elective_4.setFont(font11)

        self.verticalLayout_34.addWidget(self.elective_4)


        self.horizontalLayout_25.addWidget(self.frame_45)


        self.verticalLayout_28.addWidget(self.frame_42)


        self.verticalLayout_23.addWidget(self.frame_40)

        self.frame_56 = QFrame(self.frame_31)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_56)

        self.frame_37 = QFrame(self.frame_31)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 90))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setSpacing(1)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_34.setSpacing(1)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.edit_student_button = QPushButton(self.frame_39)
        self.edit_student_button.setObjectName(u"edit_student_button")
        self.edit_student_button.setMaximumSize(QSize(16777215, 40))
        font12 = QFont()
        font12.setFamily(u"JetBrains Mono NL Medium")
        font12.setPointSize(10)
        self.edit_student_button.setFont(font12)
        self.edit_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);\n"
"border-top-left-radius: 20px;")

        self.horizontalLayout_34.addWidget(self.edit_student_button)

        self.delete_student_button = QPushButton(self.frame_39)
        self.delete_student_button.setObjectName(u"delete_student_button")
        self.delete_student_button.setMaximumSize(QSize(16777215, 40))
        self.delete_student_button.setFont(font12)
        self.delete_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);\n"
"border-top-right-radius: 20px;")

        self.horizontalLayout_34.addWidget(self.delete_student_button)


        self.verticalLayout_37.addWidget(self.frame_39)

        self.add_student_button = QPushButton(self.frame_37)
        self.add_student_button.setObjectName(u"add_student_button")
        self.add_student_button.setMaximumSize(QSize(16777215, 50))
        self.add_student_button.setFont(font12)
        self.add_student_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(213, 93, 33);\n"
"border-bottom-left-radius: 20px; \n"
"border-bottom-right-radius: 20px; ")

        self.verticalLayout_37.addWidget(self.add_student_button)


        self.verticalLayout_23.addWidget(self.frame_37)


        self.horizontalLayout_20.addWidget(self.frame_31)

        self.next_button_widget = QWidget(self.frame_29)
        self.next_button_widget.setObjectName(u"next_button_widget")
        self.next_button_widget.setMaximumSize(QSize(50, 16777215))
        self.next_button_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(112, 112, 112);\n"
"padding: 0px;\n"
"}\n"
"\n"
"QWidget:hover {\n"
"	background-color: rgb(168, 168, 168);\n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.next_button_widget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.next_button = QLabel(self.next_button_widget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(45, 45))
        self.next_button.setMaximumSize(QSize(45, 45))
        self.next_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.next_button.setPixmap(QPixmap(u"Include/img/arrow_right.png"))
        self.next_button.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.next_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.next_button_widget)


        self.verticalLayout_22.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.student_details)
        self.search_screen = QWidget()
        self.search_screen.setObjectName(u"search_screen")
        self.verticalLayout_38 = QVBoxLayout(self.search_screen)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.search_frame_2 = QFrame(self.search_screen)
        self.search_frame_2.setObjectName(u"search_frame_2")
        self.search_frame_2.setMaximumSize(QSize(16777215, 60))
        self.search_frame_2.setStyleSheet(u"background-color:#f2f4ee;")
        self.search_frame_2.setFrameShape(QFrame.StyledPanel)
        self.search_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.search_frame_2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.SchoolNameBorder_9 = QFrame(self.search_frame_2)
        self.SchoolNameBorder_9.setObjectName(u"SchoolNameBorder_9")
        self.SchoolNameBorder_9.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_9.setStyleSheet(u"background-color: #414844;\n"
"border-radius:8px;")
        self.SchoolNameBorder_9.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.SchoolNameBorder_9)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(1, 1, 1, 1)
        self.frame_57 = QFrame(self.SchoolNameBorder_9)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(600, 35))
        self.frame_57.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(5, 5, 5, 5)
        self.searchbar_main_2 = QLineEdit(self.frame_57)
        self.searchbar_main_2.setObjectName(u"searchbar_main_2")
        sizePolicy.setHeightForWidth(self.searchbar_main_2.sizePolicy().hasHeightForWidth())
        self.searchbar_main_2.setSizePolicy(sizePolicy)
        self.searchbar_main_2.setFont(font6)
        self.searchbar_main_2.setCursor(QCursor(Qt.IBeamCursor))
        self.searchbar_main_2.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_40.addWidget(self.searchbar_main_2)

        self.close_search_2 = QLabel(self.frame_57)
        self.close_search_2.setObjectName(u"close_search_2")
        self.close_search_2.setMinimumSize(QSize(25, 25))
        self.close_search_2.setMaximumSize(QSize(25, 25))
        self.close_search_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_search_2.setPixmap(QPixmap(u"Include/img/close.jpg"))
        self.close_search_2.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.close_search_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_39.addWidget(self.frame_57)


        self.horizontalLayout_38.addWidget(self.SchoolNameBorder_9)


        self.verticalLayout_38.addWidget(self.search_frame_2)

        self.frame_58 = QFrame(self.search_screen)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_58)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.scrollArea = QScrollArea(self.frame_58)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1262, 706))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.frame_59 = QFrame(self.scrollAreaWidgetContents)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 90))
        self.frame_59.setMaximumSize(QSize(16777215, 90))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.frame_59, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_39.addWidget(self.scrollArea)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.stackedWidget.addWidget(self.search_screen)

        self.centralWidgetLaayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.SignUpButton)
        self.label_7.setBuddy(self.SignUpButton_2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#414844;\">WASSCEVERSE</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
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
        self.school_name_error.setText(QCoreApplication.translate("MainWindow", u"This school already exists", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Email:</span></p></body></html>", None))
        self.email_error.setText(QCoreApplication.translate("MainWindow", u"This email has been used", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">School Code:</span></p></body></html>", None))
        self.school_code_error.setText(QCoreApplication.translate("MainWindow", u"This school code is already in use", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Password:</span></p></body></html>", None))
        self.password_error.setText(QCoreApplication.translate("MainWindow", u"Try a stronger password", None))
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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Select Your Camera", None))
        self.label_13.setText("")
        self.searchbar_main.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student", None))
        self.close_search.setText("")
        self.previous_data.setText("")
        self.label_12.setText("")
        self.take_photo.setText(QCoreApplication.translate("MainWindow", u"Take A Picture", None))
        self.import_file.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.label71.setText(QCoreApplication.translate("MainWindow", u"Signature:", None))
        self.signature.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#646464;\">Fingerprint</span></p></body></html>", None))
        self.left_thumb.setText("")
        self.right_thumb.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Name:</span></p></body></html>", None))
        self.student_name.setText(QCoreApplication.translate("MainWindow", u"Flash Barry Allen", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">School:</span></p></body></html>", None))
        self.student_school.setText(QCoreApplication.translate("MainWindow", u"Presbyterian Boys' Secondary School", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Class:</span></p></body></html>", None))
        self.student_class.setText(QCoreApplication.translate("MainWindow", u"3 Science 2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Course:</span></p></body></html>", None))
        self.student_course.setText(QCoreApplication.translate("MainWindow", u"General Science", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#707070;\">Details</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#646464;\">Basic Information</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Gender:</span></p></body></html>", None))
        self.student_gender.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Date of Birth:</span></p></body></html>", None))
        self.date_of_birth_label.setText(QCoreApplication.translate("MainWindow", u"3rd April 2003", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Parent's Contact:</span></p></body></html>", None))
        self.parent_contact.setText(QCoreApplication.translate("MainWindow", u"+233 XXX XXX XXXX", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">BECE Index Number:</span></p></body></html>", None))
        self.index_number_bece.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#646464;\">Electives</span></p></body></html>", None))
        self.elective_1.setText(QCoreApplication.translate("MainWindow", u"Elective ICT", None))
        self.elective_2.setText(QCoreApplication.translate("MainWindow", u"Elective Mathematics", None))
        self.elective_3.setText(QCoreApplication.translate("MainWindow", u"Chemistry", None))
        self.elective_4.setText(QCoreApplication.translate("MainWindow", u"Physics", None))
        self.edit_student_button.setText(QCoreApplication.translate("MainWindow", u"Edit Student Record", None))
        self.delete_student_button.setText(QCoreApplication.translate("MainWindow", u"Delete Student Record", None))
        self.add_student_button.setText(QCoreApplication.translate("MainWindow", u"Add Student Record", None))
        self.next_button.setText("")
        self.searchbar_main_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student", None))
        self.close_search_2.setText("")
    # retranslateUi

