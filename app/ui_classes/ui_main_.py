# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainmvxdro.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QCameraViewfinder
from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1512, 1048)
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
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
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
        self.SignInInfoTop.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

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
        self.SignInInfoBottom.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
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
        sizePolicy.setHeightForWidth(
            self.schoolNameSignIn.sizePolicy().hasHeightForWidth())
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
        sizePolicy.setHeightForWidth(
            self.emailSignIn.sizePolicy().hasHeightForWidth())
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
        sizePolicy.setHeightForWidth(
            self.passwordSignIn.sizePolicy().hasHeightForWidth())
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
        self.label_2.setMaximumSize(QSize(70, 16777215))
        self.label_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.SignUpButton = QPushButton(self.frame_5)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setMaximumSize(QSize(300, 16777215))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.SignInSubmit.sizePolicy().hasHeightForWidth())
        self.SignInSubmit.setSizePolicy(sizePolicy1)
        self.SignInSubmit.setMinimumSize(QSize(100, 40))
        self.SignInSubmit.setMaximumSize(QSize(250, 16777215))
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

        self.SignInBackgroundLayout.addWidget(
            self.SignInFrame, 0, Qt.AlignHCenter)

        self.signInLayout.addWidget(self.background)

        self.stackedWidget.addWidget(self.signIn)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_44 = QVBoxLayout(self.page_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_79 = QFrame(self.page_2)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_79)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_100 = QFrame(self.frame_79)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMaximumSize(QSize(16777215, 50))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_62.setSpacing(3)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_100)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(150, 40))
        font8 = QFont()
        font8.setFamily(u"Inter Medium")
        font8.setPointSize(12)
        self.pushButton_7.setFont(font8)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(148, 22, 24);\n"
                                        "border-top-left-radius: 20px;\n"
                                        "padding: 10px 20px;")

        self.horizontalLayout_62.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_100)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(16777215, 40))
        self.pushButton_6.setFont(font8)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(100, 100, 100);\n"
                                        "padding: 10px 20px;")

        self.horizontalLayout_62.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.frame_100)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(255, 40))
        self.pushButton_9.setFont(font8)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(213, 93, 33);\n"
                                        "border-top-right-radius: 20px;\n"
                                        "padding: 10px 20px;")

        self.horizontalLayout_62.addWidget(self.pushButton_9)

        self.verticalLayout_45.addWidget(self.frame_100)

        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMaximumSize(QSize(16777215, 400))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_80)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.widget_2 = QWebEngineView(self.frame_80)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_46.addWidget(self.widget_2)

        self.verticalLayout_45.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_79)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_81)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_82)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_85 = QFrame(self.frame_82)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMaximumSize(QSize(16777215, 40))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.frame_84 = QFrame(self.frame_85)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_54.addWidget(self.frame_84)

        self.label_41 = QLabel(self.frame_85)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(121, 16777215))
        font9 = QFont()
        font9.setFamily(u"Inter Medium")
        font9.setPointSize(10)
        self.label_41.setFont(font9)

        self.horizontalLayout_54.addWidget(self.label_41)

        self.year_group = QComboBox(self.frame_85)
        self.year_group.addItem("")
        self.year_group.setObjectName(u"year_group")
        self.year_group.setMaximumSize(QSize(117, 16777215))
        self.year_group.setFont(font9)

        self.horizontalLayout_54.addWidget(self.year_group)

        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_54.addWidget(self.frame_86)

        self.verticalLayout_48.addWidget(self.frame_85)

        self.frame_87 = QFrame(self.frame_82)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_87)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.frame_94 = QFrame(self.frame_89)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_40 = QLabel(self.frame_94)
        self.label_40.setObjectName(u"label_40")
        font10 = QFont()
        font10.setFamily(u"Inter Medium")
        font10.setPointSize(11)
        self.label_40.setFont(font10)

        self.horizontalLayout_59.addWidget(self.label_40)

        self.horizontalLayout_55.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_89)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_43 = QLabel(self.frame_95)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font10)

        self.horizontalLayout_60.addWidget(self.label_43)

        self.horizontalLayout_55.addWidget(self.frame_95)

        self.verticalLayout_49.addWidget(self.frame_89)

        self.frame_91 = QFrame(self.frame_87)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.frame_96 = QFrame(self.frame_91)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_44 = QLabel(self.frame_96)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font10)

        self.horizontalLayout_61.addWidget(self.label_44)

        self.horizontalLayout_56.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_91)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_97)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_46 = QLabel(self.frame_97)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_50.addWidget(self.label_46)

        self.horizontalLayout_56.addWidget(self.frame_97)

        self.verticalLayout_49.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_87)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.frame_98 = QFrame(self.frame_92)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_98)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_45 = QLabel(self.frame_98)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_54.addWidget(self.label_45)

        self.horizontalLayout_58.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_92)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_99)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_47 = QLabel(self.frame_99)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_55.addWidget(self.label_47)

        self.horizontalLayout_58.addWidget(self.frame_99)

        self.verticalLayout_49.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_87)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.verticalLayout_49.addWidget(self.frame_93)

        self.verticalLayout_48.addWidget(self.frame_87)

        self.verticalLayout_47.addWidget(self.frame_82)

        self.frame_83 = QFrame(self.frame_81)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(16777215, 70))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.view_data = QPushButton(self.frame_83)
        self.view_data.setObjectName(u"view_data")
        self.view_data.setMinimumSize(QSize(0, 50))
        font11 = QFont()
        font11.setFamily(u"Inter SemiBold")
        font11.setPointSize(13)
        self.view_data.setFont(font11)
        self.view_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_data.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(213, 93, 33);\n"
                                     "border-bottom-right-radius: 20px;\n"
                                     "border-bottom-left-radius: 20px;")

        self.horizontalLayout_53.addWidget(self.view_data)

        self.verticalLayout_47.addWidget(self.frame_83)

        self.verticalLayout_45.addWidget(self.frame_81)

        self.verticalLayout_44.addWidget(self.frame_79)

        self.stackedWidget.addWidget(self.page_2)
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
        self.SignInBackgroundLayout_2.setObjectName(
            u"SignInBackgroundLayout_2")
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
        sizePolicy.setHeightForWidth(
            self.schoolNameSignUp.sizePolicy().hasHeightForWidth())
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

        self.frame_88 = QFrame(self.SignInFrame_2)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_88)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.EmailSignInFrame_3 = QFrame(self.frame_88)
        self.EmailSignInFrame_3.setObjectName(u"EmailSignInFrame_3")
        self.EmailSignInFrame_3.setMaximumSize(QSize(600, 90))
        self.EmailSignInFrame_3.setFrameShape(QFrame.StyledPanel)
        self.EmailSignInFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.EmailSignInFrame_3)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.EmailSignInFrame_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font5)

        self.verticalLayout_51.addWidget(self.label_42)

        self.SchoolNameBorder_11 = QFrame(self.EmailSignInFrame_3)
        self.SchoolNameBorder_11.setObjectName(u"SchoolNameBorder_11")
        self.SchoolNameBorder_11.setMaximumSize(QSize(600, 35))
        self.SchoolNameBorder_11.setStyleSheet(u"background-color: #414844;\n"
                                               "border-radius:8px;")
        self.SchoolNameBorder_11.setFrameShape(QFrame.StyledPanel)
        self.SchoolNameBorder_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.SchoolNameBorder_11)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(1, 1, 1, 1)
        self.frame_90 = QFrame(self.SchoolNameBorder_11)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(600, 35))
        self.frame_90.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 8px;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_90)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(5, 5, 5, 5)
        self.passwordSignUp = QLineEdit(self.frame_90)
        self.passwordSignUp.setObjectName(u"passwordSignUp")
        self.passwordSignUp.setMinimumSize(QSize(0, 25))
        self.passwordSignUp.setEchoMode(QLineEdit.Password)

        self.verticalLayout_52.addWidget(self.passwordSignUp)

        self.horizontalLayout_57.addWidget(self.frame_90)

        self.verticalLayout_51.addWidget(self.SchoolNameBorder_11)

        self.password_error = QLabel(self.EmailSignInFrame_3)
        self.password_error.setObjectName(u"password_error")
        self.password_error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_51.addWidget(self.password_error)

        self.verticalLayout_53.addWidget(self.EmailSignInFrame_3)

        self.verticalLayout_11.addWidget(self.frame_88)

        self.frame_21 = QFrame(self.SignInFrame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
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
        self.locationSignUp = QLineEdit(self.frame_16)
        self.locationSignUp.setObjectName(u"locationSignUp")
        self.locationSignUp.setMinimumSize(QSize(0, 25))

        self.verticalLayout_17.addWidget(self.locationSignUp)

        self.horizontalLayout_9.addWidget(self.frame_16)

        self.verticalLayout_16.addWidget(self.SchoolNameBorder_6)

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
        self.countrySignUp = QLineEdit(self.frame_22)
        self.countrySignUp.setObjectName(u"countrySignUp")
        self.countrySignUp.setMinimumSize(QSize(0, 25))
        self.countrySignUp.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_19.addWidget(self.countrySignUp)

        self.horizontalLayout_12.addWidget(self.frame_22)

        self.verticalLayout_18.addWidget(self.SchoolNameBorder_7)

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
        self.label_7.setMaximumSize(QSize(200, 16777215))
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
        self.SignInSubmit_2.setMaximumSize(QSize(200, 16777215))
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

        self.SignInBackgroundLayout_2.addWidget(
            self.SignInFrame_2, 0, Qt.AlignHCenter)

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
        self.SignInInfoTop_2.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.verticalLayout_10.addWidget(self.SignInInfoTop_2)

        self.SignInInfoBottom_2 = QLabel(self.SignInInfoFrame_2)
        self.SignInInfoBottom_2.setObjectName(u"SignInInfoBottom_2")
        self.SignInInfoBottom_2.setFont(font2)
        self.SignInInfoBottom_2.setLineWidth(1)
        self.SignInInfoBottom_2.setMidLineWidth(0)
        self.SignInInfoBottom_2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.SignInInfoBottom_2.setMargin(9)

        self.verticalLayout_10.addWidget(self.SignInInfoBottom_2)

        self.signInLeftBottomSpacer_2 = QFrame(self.SignInInfoFrame_2)
        self.signInLeftBottomSpacer_2.setObjectName(
            u"signInLeftBottomSpacer_2")
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
        self.close_camera = QPushButton(self.frame)
        self.close_camera.setObjectName(u"close_camera")
        self.close_camera.setMinimumSize(QSize(30, 30))
        self.close_camera.setMaximumSize(QSize(30, 30))
        font12 = QFont()
        font12.setPointSize(15)
        font12.setBold(True)
        font12.setWeight(75)
        self.close_camera.setFont(font12)
        self.close_camera.setStyleSheet(u"QPushButton {\n"
                                        "	color: rgb(95, 95, 95);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	\n"
                                        "	background-color: rgb(200, 200, 200);\n"
                                        "}")

        self.horizontalLayout_16.addWidget(self.close_camera)

        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_24)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.comboBox)

        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        font13 = QFont()
        font13.setFamily(u"Niagara Engraved")
        self.frame_25.setFont(font13)
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
        font14 = QFont()
        font14.setFamily(u"Agency FB")
        self.frame_26.setFont(font14)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_27)

        self.capture = QPushButton(self.frame_26)
        self.capture.setObjectName(u"capture")
        self.capture.setMinimumSize(QSize(400, 60))
        self.capture.setMaximumSize(QSize(400, 60))
        font15 = QFont()
        font15.setFamily(u"CAMERA - FOTOGRAAMI")
        font15.setPointSize(35)
        self.capture.setFont(font15)
        self.capture.setStyleSheet(u"QPushButton{\n"
                                   "color: #fff;\n"
                                   "background-color: #707070;\n"
                                   "border-radius: 30px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgb(152, 152, 152);\n"
                                   "}")

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
        self.pushButton_5 = QPushButton(self.student_details)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(100, 16777215))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
                                        "color: #ffffff;\n"
                                        "background-color: rgb(112, 112, 112);\n"
                                        "padding: 10px 20px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(168, 168, 168);\n"
                                        "}")

        self.verticalLayout_22.addWidget(self.pushButton_5)

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
        self.SchoolNameBorder_8.setMinimumSize(QSize(0, 35))
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
        self.search_student_button = QPushButton(self.frame_55)
        self.search_student_button.setObjectName(u"search_student_button")
        sizePolicy2.setHeightForWidth(
            self.search_student_button.sizePolicy().hasHeightForWidth())
        self.search_student_button.setSizePolicy(sizePolicy2)
        self.search_student_button.setCursor(QCursor(Qt.IBeamCursor))
        self.search_student_button.setStyleSheet(u"padding-left: 10px;\n"
                                                 "text-align: left;\n"
                                                 "color: rgb(165, 165, 165);")

        self.horizontalLayout_37.addWidget(self.search_student_button)

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
        self.previous_data_button = QPushButton(self.frame_30)
        self.previous_data_button.setObjectName(u"previous_data_button")
        self.previous_data_button.setMinimumSize(QSize(80, 800))
        self.previous_data_button.setMaximumSize(QSize(100, 16777215))
        font16 = QFont()
        font16.setFamily(u"Californian FB")
        font16.setPointSize(100)
        self.previous_data_button.setFont(font16)
        self.previous_data_button.setStyleSheet(u"QPushButton {\n"
                                                "color: #ffffff;\n"
                                                "background-color: rgb(112, 112, 112);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "	background-color: rgb(168, 168, 168);\n"
                                                "}")

        self.horizontalLayout_21.addWidget(self.previous_data_button)

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
        self.label_12.setMaximumSize(QSize(180, 240))
        self.label_12.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_12)

        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 30))
        font17 = QFont()
        font17.setFamily(u"JetBrains Mono NL SemiBold")
        font17.setPointSize(11)
        self.label_48.setFont(font17)

        self.verticalLayout_27.addWidget(self.label_48)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 30))
        self.pushButton_8.setMaximumSize(QSize(16777215, 30))
        font18 = QFont()
        font18.setFamily(u"JetBrains Mono NL Medium")
        font18.setPointSize(10)
        self.pushButton_8.setFont(font18)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(213, 93, 33);")

        self.verticalLayout_27.addWidget(self.pushButton_8)

        self.individual_student_key = QPushButton(self.frame_7)
        self.individual_student_key.setObjectName(u"individual_student_key")
        self.individual_student_key.setMinimumSize(QSize(0, 30))
        font19 = QFont()
        font19.setFamily(u"JetBrains Mono NL Medium")
        font19.setPointSize(9)
        self.individual_student_key.setFont(font19)
        self.individual_student_key.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                  "background-color: rgb(213, 93, 33);")

        self.verticalLayout_27.addWidget(self.individual_student_key)

        self.student_key_label = QLabel(self.frame_7)
        self.student_key_label.setObjectName(u"student_key_label")
        font20 = QFont()
        font20.setFamily(u"JetBrains Mono NL SemiBold")
        font20.setPointSize(9)
        self.student_key_label.setFont(font20)

        self.verticalLayout_27.addWidget(self.student_key_label)

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
        font21 = QFont()
        font21.setFamily(u"JetBrains Mono NL Medium")
        self.take_photo.setFont(font21)
        self.take_photo.setCursor(QCursor(Qt.PointingHandCursor))
        self.take_photo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(66, 72, 68);\n"
                                      "padding: 6px;\n"
                                      "border-top-left-radius: 10px;\n"
                                      "border-bottom-left-radius: 10px;")

        self.horizontalLayout_23.addWidget(self.take_photo)

        self.import_file = QPushButton(self.frame_32)
        self.import_file.setObjectName(u"import_file")
        self.import_file.setFont(font21)
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
        font22 = QFont()
        font22.setFamily(u"JetBrains Mono Medium")
        font22.setPointSize(10)
        self.label71.setFont(font22)

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
        font23 = QFont()
        font23.setFamily(u"JetBrains Mono NL ExtraBold")
        self.label_29.setFont(font23)

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
        self.label_18.setFont(font23)

        self.verticalLayout_25.addWidget(self.label_18)

        self.student_name = QLabel(self.student_details_name)
        self.student_name.setObjectName(u"student_name")
        self.student_name.setFont(font22)

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
        self.label_19.setFont(font23)

        self.verticalLayout_29.addWidget(self.label_19)

        self.student_school = QLabel(self.frame_35)
        self.student_school.setObjectName(u"student_school")
        self.student_school.setFont(font22)

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
        self.label_20.setFont(font23)

        self.verticalLayout_30.addWidget(self.label_20)

        self.student_class = QLabel(self.frame_34)
        self.student_class.setObjectName(u"student_class")
        self.student_class.setFont(font22)

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
        self.label_22.setFont(font23)

        self.verticalLayout_31.addWidget(self.label_22)

        self.student_course = QLabel(self.frame_43)
        self.student_course.setObjectName(u"student_course")
        self.student_course.setFont(font22)

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
        self.label_23.setFont(font23)
        self.label_23.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

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
        self.label_21.setFont(font23)

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
        self.label_24.setFont(font23)

        self.horizontalLayout_27.addWidget(self.label_24)

        self.student_gender = QLabel(self.frame_48)
        self.student_gender.setObjectName(u"student_gender")
        font24 = QFont()
        font24.setFamily(u"JetBrains Mono Medium")
        font24.setPointSize(11)
        self.student_gender.setFont(font24)

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
        self.label_25.setFont(font23)

        self.horizontalLayout_28.addWidget(self.label_25)

        self.date_of_birth_label = QLabel(self.frame_47)
        self.date_of_birth_label.setObjectName(u"date_of_birth_label")
        self.date_of_birth_label.setFont(font24)

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
        self.label_26.setFont(font23)

        self.horizontalLayout_29.addWidget(self.label_26)

        self.parent_contact = QLabel(self.frame_50)
        self.parent_contact.setObjectName(u"parent_contact")
        self.parent_contact.setFont(font24)

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
        self.label_27.setFont(font23)

        self.horizontalLayout_30.addWidget(self.label_27)

        self.index_number_bece = QLabel(self.frame_49)
        self.index_number_bece.setObjectName(u"index_number_bece")
        self.index_number_bece.setFont(font24)

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
        self.label_28.setFont(font23)

        self.verticalLayout_34.addWidget(self.label_28)

        self.elective_1 = QLabel(self.frame_45)
        self.elective_1.setObjectName(u"elective_1")
        self.elective_1.setFont(font24)

        self.verticalLayout_34.addWidget(self.elective_1)

        self.elective_2 = QLabel(self.frame_45)
        self.elective_2.setObjectName(u"elective_2")
        self.elective_2.setFont(font24)

        self.verticalLayout_34.addWidget(self.elective_2)

        self.elective_3 = QLabel(self.frame_45)
        self.elective_3.setObjectName(u"elective_3")
        self.elective_3.setFont(font24)

        self.verticalLayout_34.addWidget(self.elective_3)

        self.elective_4 = QLabel(self.frame_45)
        self.elective_4.setObjectName(u"elective_4")
        self.elective_4.setFont(font24)

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
        self.frame_39.setMaximumSize(QSize(16777215, 60))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_34.setSpacing(1)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.edit_student_button = QPushButton(self.frame_39)
        self.edit_student_button.setObjectName(u"edit_student_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.edit_student_button.sizePolicy().hasHeightForWidth())
        self.edit_student_button.setSizePolicy(sizePolicy3)
        self.edit_student_button.setMaximumSize(QSize(16777215, 16777215))
        self.edit_student_button.setFont(font18)
        self.edit_student_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(107, 107, 107);\n"
                                               "border-top-left-radius: 20px;")

        self.horizontalLayout_34.addWidget(self.edit_student_button)

        self.delete_student_button = QPushButton(self.frame_39)
        self.delete_student_button.setObjectName(u"delete_student_button")
        sizePolicy3.setHeightForWidth(
            self.delete_student_button.sizePolicy().hasHeightForWidth())
        self.delete_student_button.setSizePolicy(sizePolicy3)
        self.delete_student_button.setMaximumSize(QSize(16777215, 16777215))
        self.delete_student_button.setFont(font18)
        self.delete_student_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                 "background-color: rgb(107, 107, 107);\n"
                                                 "border-top-right-radius: 20px;")

        self.horizontalLayout_34.addWidget(self.delete_student_button)

        self.verticalLayout_37.addWidget(self.frame_39)

        self.add_student_button = QPushButton(self.frame_37)
        self.add_student_button.setObjectName(u"add_student_button")
        self.add_student_button.setMaximumSize(QSize(16777215, 50))
        self.add_student_button.setFont(font18)
        self.add_student_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_student_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(213, 93, 33);\n"
                                              "border-bottom-left-radius: 20px; \n"
                                              "border-bottom-right-radius: 20px; ")

        self.verticalLayout_37.addWidget(self.add_student_button)

        self.frame_78 = QFrame(self.frame_37)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.frame_78)

        self.verticalLayout_23.addWidget(self.frame_37)

        self.horizontalLayout_20.addWidget(self.frame_31)

        self.next_data_button = QPushButton(self.frame_29)
        self.next_data_button.setObjectName(u"next_data_button")
        sizePolicy3.setHeightForWidth(
            self.next_data_button.sizePolicy().hasHeightForWidth())
        self.next_data_button.setSizePolicy(sizePolicy3)
        self.next_data_button.setMinimumSize(QSize(80, 800))
        self.next_data_button.setMaximumSize(QSize(80, 16777215))
        self.next_data_button.setFont(font16)
        self.next_data_button.setStyleSheet(u"QPushButton {\n"
                                            "color: #ffffff;\n"
                                            "background-color: rgb(112, 112, 112);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "	background-color: rgb(168, 168, 168);\n"
                                            "}")

        self.horizontalLayout_20.addWidget(
            self.next_data_button, 0, Qt.AlignVCenter)

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
        self.search_frame_2.setMaximumSize(QSize(16777215, 85))
        self.search_frame_2.setStyleSheet(u"background-color:#f2f4ee;")
        self.search_frame_2.setFrameShape(QFrame.StyledPanel)
        self.search_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.search_frame_2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, 25, -1, -1)
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
        self.searchbar_main = QLineEdit(self.frame_57)
        self.searchbar_main.setObjectName(u"searchbar_main")
        sizePolicy.setHeightForWidth(
            self.searchbar_main.sizePolicy().hasHeightForWidth())
        self.searchbar_main.setSizePolicy(sizePolicy)
        self.searchbar_main.setFont(font6)
        self.searchbar_main.setCursor(QCursor(Qt.IBeamCursor))
        self.searchbar_main.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_40.addWidget(self.searchbar_main)

        self.close_search = QPushButton(self.frame_57)
        self.close_search.setObjectName(u"close_search")
        self.close_search.setMinimumSize(QSize(25, 25))
        self.close_search.setMaximumSize(QSize(25, 25))
        font25 = QFont()
        font25.setFamily(u"Arial")
        font25.setPointSize(11)
        font25.setBold(True)
        font25.setWeight(75)
        self.close_search.setFont(font25)

        self.horizontalLayout_40.addWidget(self.close_search)

        self.horizontalLayout_39.addWidget(self.frame_57)

        self.horizontalLayout_38.addWidget(self.SchoolNameBorder_9)

        self.verticalLayout_38.addWidget(self.search_frame_2)

        self.frame_58 = QFrame(self.search_screen)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_58)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.listWidget = QListWidget(self.frame_58)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        font26 = QFont()
        font26.setFamily(u"JetBrains Mono NL SemiBold")
        font26.setPointSize(16)
        self.listWidget.setFont(font26)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_39.addWidget(self.listWidget)

        self.verticalLayout_38.addWidget(self.frame_58)

        self.stackedWidget.addWidget(self.search_screen)
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.verticalLayout_43 = QVBoxLayout(self.edit)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_59 = QFrame(self.edit)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_59)
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 30))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_62)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(110, 0))
        self.label_14.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_17.addWidget(self.label_14)

        self.plainTextEdit = QPlainTextEdit(self.frame_62)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                         "border-radius: 4px;")
        self.plainTextEdit.setBackgroundVisible(False)

        self.horizontalLayout_17.addWidget(self.plainTextEdit)

        self.verticalLayout_40.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_59)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(16777215, 30))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_63)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(110, 0))
        self.label_15.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_22.addWidget(self.label_15)

        self.plainTextEdit_2 = QPlainTextEdit(self.frame_63)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                           "border-radius: 4px;")

        self.horizontalLayout_22.addWidget(self.plainTextEdit_2)

        self.verticalLayout_40.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_59)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 30))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_64)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))
        self.label_16.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_41.addWidget(self.label_16)

        self.plainTextEdit_3 = QPlainTextEdit(self.frame_64)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                           "border-radius: 4px;")

        self.horizontalLayout_41.addWidget(self.plainTextEdit_3)

        self.verticalLayout_40.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.frame_59)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(16777215, 30))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_65)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(110, 0))
        self.label_17.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_42.addWidget(self.label_17)

        self.dateEdit = QDateEdit(self.frame_65)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCorrectionMode(
            QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setMaximumDate(QDate(2080, 12, 31))
        self.dateEdit.setMinimumDate(QDate(1980, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_42.addWidget(self.dateEdit)

        self.verticalLayout_40.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_59)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(16777215, 60))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_66)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(110, 0))
        self.label_30.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_43.addWidget(self.label_30)

        self.comboBox_2 = QComboBox(self.frame_66)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                      "border-radius: 4px;")

        self.horizontalLayout_43.addWidget(self.comboBox_2)

        self.verticalLayout_40.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_59)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMaximumSize(QSize(16777215, 30))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_67)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_44.addWidget(self.label_31)

        self.textEdit = QTextEdit(self.frame_67)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                    "border-radius: 4px;")

        self.horizontalLayout_44.addWidget(self.textEdit)

        self.verticalLayout_40.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_59)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMaximumSize(QSize(16777215, 30))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_68)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_45.addWidget(self.label_32)

        self.plainTextEdit_4 = QPlainTextEdit(self.frame_68)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_4.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                           "border-radius: 4px;")

        self.horizontalLayout_45.addWidget(self.plainTextEdit_4)

        self.verticalLayout_40.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_59)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMaximumSize(QSize(16777215, 30))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_69)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(110, 0))
        self.label_33.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_46.addWidget(self.label_33)

        self.dateEdit_2 = QDateEdit(self.frame_69)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                      "border-radius: 4px;")
        self.dateEdit_2.setDate(QDate(2019, 1, 1))

        self.horizontalLayout_46.addWidget(self.dateEdit_2)

        self.verticalLayout_40.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_59)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_70)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(110, 0))
        self.label_34.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_47.addWidget(self.label_34)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 150))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_71)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_24 = QCheckBox(self.frame_71)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout.addWidget(self.checkBox_24, 8, 4, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_71)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 3, 2, 2, 1)

        self.checkBox_12 = QCheckBox(self.frame_71)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout.addWidget(self.checkBox_12, 13, 4, 1, 1)

        self.checkBox_21 = QCheckBox(self.frame_71)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout.addWidget(self.checkBox_21, 5, 4, 3, 1)

        self.checkBox_2 = QCheckBox(self.frame_71)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)

        self.checkBox_17 = QCheckBox(self.frame_71)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout.addWidget(self.checkBox_17, 1, 2, 2, 1)

        self.checkBox_22 = QCheckBox(self.frame_71)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout.addWidget(self.checkBox_22, 5, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.frame_71)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout.addWidget(self.checkBox_11, 11, 2, 3, 1)

        self.checkBox_14 = QCheckBox(self.frame_71)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout.addWidget(self.checkBox_14, 14, 2, 2, 2)

        self.checkBox_4 = QCheckBox(self.frame_71)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 2)

        self.checkBox_23 = QCheckBox(self.frame_71)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout.addWidget(self.checkBox_23, 5, 2, 1, 1)

        self.checkBox = QCheckBox(self.frame_71)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)

        self.checkBox_20 = QCheckBox(self.frame_71)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout.addWidget(self.checkBox_20, 10, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.frame_71)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 9, 4, 2, 1)

        self.checkBox_3 = QCheckBox(self.frame_71)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 0, 4, 1, 1)

        self.checkBox_6 = QCheckBox(self.frame_71)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 3, 4, 2, 1)

        self.checkBox_19 = QCheckBox(self.frame_71)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout.addWidget(self.checkBox_19, 13, 0, 1, 1)

        self.checkBox_13 = QCheckBox(self.frame_71)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout.addWidget(self.checkBox_13, 14, 0, 2, 2)

        self.checkBox_8 = QCheckBox(self.frame_71)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_8, 7, 2, 3, 1)

        self.checkBox_7 = QCheckBox(self.frame_71)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 7, 0, 3, 2)

        self.checkBox_18 = QCheckBox(self.frame_71)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout.addWidget(self.checkBox_18, 2, 4, 1, 1)

        self.checkBox_16 = QCheckBox(self.frame_71)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout.addWidget(self.checkBox_16, 2, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.frame_71)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 10, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.frame_71)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout.addWidget(self.checkBox_15, 14, 4, 1, 1)

        self.horizontalLayout_47.addWidget(self.frame_71)

        self.verticalLayout_40.addWidget(self.frame_70)

        self.frame_72 = QFrame(self.frame_59)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_72)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(110, 0))
        self.label_35.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_48.addWidget(self.label_35)

        self.radioButton = QRadioButton(self.frame_72)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(110, 0))
        self.radioButton.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_48.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_72)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_48.addWidget(self.radioButton_2)

        self.verticalLayout_40.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_59)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 30))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_73)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(110, 0))
        self.label_36.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_49.addWidget(self.label_36)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame_73)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(0, 25))
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 25))
        self.plainTextEdit_5.setStyleSheet(u"border-bottom: 1px solid #333333;\n"
                                           "border-radius: 4px;")

        self.horizontalLayout_49.addWidget(self.plainTextEdit_5)

        self.verticalLayout_40.addWidget(self.frame_73)

        self.frame_74 = QFrame(self.frame_59)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_74)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(110, 0))
        self.label_37.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_50.addWidget(self.label_37)

        self.pushButton_2 = QPushButton(self.frame_74)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(200, 16777215))
        self.pushButton_2.setStyleSheet(u"padding: 20px;\n"
                                        "background-color: rgb(119, 119, 119);\n"
                                        "color: white;")

        self.horizontalLayout_50.addWidget(self.pushButton_2)

        self.label_38 = QLabel(self.frame_74)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(140, 0))
        self.label_38.setMaximumSize(QSize(200, 16777215))
        self.label_38.setStyleSheet(u"margin-left:20px;")

        self.horizontalLayout_50.addWidget(self.label_38)

        self.frame_76 = QFrame(self.frame_74)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_50.addWidget(self.frame_76)

        self.verticalLayout_40.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_59)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_75)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(110, 0))
        self.label_39.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_51.addWidget(self.label_39)

        self.pushButton_3 = QPushButton(self.frame_75)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"padding: 20px;\n"
                                        "background-color: rgb(119, 119, 119);\n"
                                        "color: white;")

        self.horizontalLayout_51.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_75)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"padding: 20px;\n"
                                        "background-color: rgb(119, 119, 119);\n"
                                        "color: white;")

        self.horizontalLayout_51.addWidget(self.pushButton_4)

        self.verticalLayout_40.addWidget(self.frame_75)

        self.verticalLayout_43.addWidget(self.frame_59)

        self.frame_77 = QFrame(self.edit)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 60))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.save_edit = QPushButton(self.frame_77)
        self.save_edit.setObjectName(u"save_edit")
        self.save_edit.setStyleSheet(u"padding: 20px;\n"
                                     "background-color: rgb(119, 119, 119);\n"
                                     "color: white;")

        self.horizontalLayout_52.addWidget(self.save_edit)

        self.cancel_edit = QPushButton(self.frame_77)
        self.cancel_edit.setObjectName(u"cancel_edit")
        self.cancel_edit.setStyleSheet(u"padding: 20px;\n"
                                       "background-color: rgb(161, 79, 80);\n"
                                       "color: white;")

        self.horizontalLayout_52.addWidget(self.cancel_edit)

        self.verticalLayout_43.addWidget(self.frame_77)

        self.stackedWidget.addWidget(self.edit)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_24 = QVBoxLayout(self.page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_60 = QFrame(self.page)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_60)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 200))
        self.frame_61.setMaximumSize(QSize(16777215, 200))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_61)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_13 = QLabel(self.frame_61)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_42.addWidget(self.label_13)

        self.pushButton = QPushButton(self.frame_61)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 80))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(213, 93, 33);\n"
                                      "border-radius: 20px;")

        self.verticalLayout_42.addWidget(self.pushButton)

        self.verticalLayout_41.addWidget(self.frame_61, 0, Qt.AlignTop)

        self.verticalLayout_24.addWidget(self.frame_60)

        self.stackedWidget.addWidget(self.page)

        self.centralWidgetLaayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.SignUpButton)
        self.label_7.setBuddy(self.SignUpButton_2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#414844;\">WASSCEVERSE.COM</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.SignInInfoTop.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#414844;\">WELOME BACK!</span></p></body></html>", None))
        self.SignInInfoBottom.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#000000;\">To keep connected with us</span><span style=\" font-size:12pt;\"><br/></span><span style=\" font-size:12pt; color:#000000;\">Please sign in with your</span><span style=\" font-size:12pt;\"><br/></span><span style=\" font-size:12pt; color:#000000;\">personal info</span><span style=\" font-size:12pt;\"/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Sign In", None))
        self.SchoolNameSignInLabel.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">School Name:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Email:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Password:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"New User?", None))
        self.SignUpButton.setText(QCoreApplication.translate(
            "MainWindow", u"Create an Account", None))
        self.SignInSubmit.setText(
            QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_6.setText(QCoreApplication.translate(
            "MainWindow", u"Import Students Data", None))
        self.pushButton_9.setText(QCoreApplication.translate(
            "MainWindow", u"Generate Student Keys", None))
        self.label_41.setText(QCoreApplication.translate(
            "MainWindow", u"Select Year Group:", None))
        self.year_group.setItemText(
            0, QCoreApplication.translate("MainWindow", u"2019", None))

        self.label_40.setText(QCoreApplication.translate(
            "MainWindow", u"Number of Students: ", None))
        self.label_43.setText(QCoreApplication.translate(
            "MainWindow", u"Number of Students Registered:", None))
        self.label_44.setText(QCoreApplication.translate(
            "MainWindow", u"Number of Students Cleared:", None))
        self.label_46.setText("")
        self.label_45.setText("")
        self.label_47.setText("")
        self.view_data.setText(QCoreApplication.translate(
            "MainWindow", u"View Students' Data", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#414844;\">Create Account</span></p></body></html>", None))
        self.SchoolNameSignInLabel_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">School Name:</span></p></body></html>", None))
        self.school_name_error.setText(QCoreApplication.translate(
            "MainWindow", u"This school already exists", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Email:</span></p></body></html>", None))
        self.email_error.setText(QCoreApplication.translate(
            "MainWindow", u"This email has been used", None))
        self.label_42.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">Password:</span></p></body></html>", None))
        self.password_error.setText(QCoreApplication.translate(
            "MainWindow", u"Try a stronger password", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Location:</span></p></body></html>", None))
        self.locationSignUp.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Region, City", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#414844;\">Country:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Already A User?", None))
        self.SignUpButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.SignInSubmit_2.setText(
            QCoreApplication.translate("MainWindow", u"Next", None))
        self.SignInInfoTop_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" color:#414844;\">HELLO</span></p></body></html>", None))
        self.SignInInfoBottom_2.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
                                                                   "<head/>\n"
                                                                   "<body>\n"
                                                                   "<p  style=\"line-height: 1\">\n"
                                                                   "<span align=\"center\" style=\" color:black;\">Enter school details to start</span><br>\n"
                                                                   "<span align=\"center\" style=\" color:black;\">your journey with us</span>\n"
                                                                   "</p>\n"
                                                                   "</body>\n"
                                                                   "</html>", None))
        self.close_camera.setText(
            QCoreApplication.translate("MainWindow", u"x", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Select Your Camera", None))
        self.capture.setText(
            QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", u"Back", None))
        self.search_student_button.setText(
            QCoreApplication.translate("MainWindow", u"Search Student", None))
        self.previous_data_button.setText(
            QCoreApplication.translate("MainWindow", u"<", None))
        self.label_12.setText("")
        self.label_48.setText(QCoreApplication.translate(
            "MainWindow", u"Registered: ", None))
        self.pushButton_8.setText(QCoreApplication.translate(
            "MainWindow", u"Register", None))
        self.individual_student_key.setText(QCoreApplication.translate(
            "MainWindow", u"Generate Student Key", None))
        self.student_key_label.setText(
            QCoreApplication.translate("MainWindow", u"Student Key:", None))
        self.take_photo.setText(QCoreApplication.translate(
            "MainWindow", u"Take A Picture", None))
        self.import_file.setText(QCoreApplication.translate(
            "MainWindow", u"Import File", None))
        self.label71.setText(QCoreApplication.translate(
            "MainWindow", u"Signature:", None))
        self.signature.setText("")
        self.label_29.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#646464;\">Fingerprint</span></p></body></html>", None))
        self.left_thumb.setText("")
        self.right_thumb.setText("")
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Name:</span></p></body></html>", None))
        self.student_name.setText(QCoreApplication.translate(
            "MainWindow", u"Flash Barry Allen", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">School:</span></p></body></html>", None))
        self.student_school.setText(QCoreApplication.translate(
            "MainWindow", u"Presbyterian Boys' Secondary School", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Class:</span></p></body></html>", None))
        self.student_class.setText(QCoreApplication.translate(
            "MainWindow", u"3 Science 2", None))
        self.label_22.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Course:</span></p></body></html>", None))
        self.student_course.setText(QCoreApplication.translate(
            "MainWindow", u"General Science", None))
        self.label_23.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#707070;\">Details</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#646464;\">Basic Information</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Gender:</span></p></body></html>", None))
        self.student_gender.setText(
            QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_25.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Date of Birth:</span></p></body></html>", None))
        self.date_of_birth_label.setText(
            QCoreApplication.translate("MainWindow", u"3rd April 2003", None))
        self.label_26.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">Parent's Contact:</span></p></body></html>", None))
        self.parent_contact.setText(QCoreApplication.translate(
            "MainWindow", u"+233 XXX XXX XXXX", None))
        self.label_27.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#414844;\">BECE Index Number:</span></p></body></html>", None))
        self.index_number_bece.setText(
            QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.label_28.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#646464;\">Electives</span></p></body></html>", None))
        self.elective_1.setText(QCoreApplication.translate(
            "MainWindow", u"Elective ICT", None))
        self.elective_2.setText(QCoreApplication.translate(
            "MainWindow", u"Elective Mathematics", None))
        self.elective_3.setText(QCoreApplication.translate(
            "MainWindow", u"Chemistry", None))
        self.elective_4.setText(QCoreApplication.translate(
            "MainWindow", u"Physics", None))
        self.edit_student_button.setText(QCoreApplication.translate(
            "MainWindow", u"Edit Student Record", None))
        self.delete_student_button.setText(QCoreApplication.translate(
            "MainWindow", u"Delete Student Record", None))
        self.add_student_button.setText(QCoreApplication.translate(
            "MainWindow", u"Add Student Record", None))
        self.next_data_button.setText(
            QCoreApplication.translate("MainWindow", u">", None))
        self.searchbar_main.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Student", None))
        self.close_search.setText(
            QCoreApplication.translate("MainWindow", u"X", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_14.setText(QCoreApplication.translate(
            "MainWindow", u"Surname:                   ", None))
        self.label_15.setText(QCoreApplication.translate(
            "MainWindow", u"First Name:                ", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"Other Names:            ", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"Date of Birth:", None))
        self.dateEdit.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.label_30.setText(QCoreApplication.translate(
            "MainWindow", u"Course:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate(
            "MainWindow", u"General Science", None))
        self.comboBox_2.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Business", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate(
            "MainWindow", u"Home Economics", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate(
            "MainWindow", u"General Arts", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate(
            "MainWindow", u"Visual Arts", None))

        self.label_31.setText(QCoreApplication.translate(
            "MainWindow", u"Class:", None))
        self.label_32.setText(QCoreApplication.translate(
            "MainWindow", u"BECE Index Number:", None))
        self.label_33.setText(QCoreApplication.translate(
            "MainWindow", u"Year Completed:", None))
        self.dateEdit_2.setDisplayFormat(
            QCoreApplication.translate("MainWindow", u"yyyy", None))
        self.label_34.setText(QCoreApplication.translate(
            "MainWindow", u"Electives", None))
        self.checkBox_24.setText(QCoreApplication.translate(
            "MainWindow", u"Textile", None))
        self.checkBox_5.setText(QCoreApplication.translate(
            "MainWindow", u"Geography", None))
        self.checkBox_12.setText(QCoreApplication.translate(
            "MainWindow", u"Ceramics and Sculpture", None))
        self.checkBox_21.setText(QCoreApplication.translate(
            "MainWindow", u"Financial Accounting", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "MainWindow", u"Chemistry", None))
        self.checkBox_17.setText(
            QCoreApplication.translate("MainWindow", u"French", None))
        self.checkBox_22.setText(QCoreApplication.translate(
            "MainWindow", u"Government", None))
        self.checkBox_11.setText(QCoreApplication.translate(
            "MainWindow", u"Picture Making", None))
        self.checkBox_14.setText(QCoreApplication.translate(
            "MainWindow", u"Food and Nutrition", None))
        self.checkBox_4.setText(QCoreApplication.translate(
            "MainWindow", u"Literature in English", None))
        self.checkBox_23.setText(QCoreApplication.translate(
            "MainWindow", u"Religious Studies", None))
        self.checkBox.setText(QCoreApplication.translate(
            "MainWindow", u"Biology", None))
        self.checkBox_20.setText(QCoreApplication.translate(
            "MainWindow", u"Leather Works", None))
        self.checkBox_9.setText(QCoreApplication.translate(
            "MainWindow", u"Graphic Design", None))
        self.checkBox_3.setText(QCoreApplication.translate(
            "MainWindow", u"Physics", None))
        self.checkBox_6.setText(QCoreApplication.translate(
            "MainWindow", u"History", None))
        self.checkBox_19.setText(QCoreApplication.translate(
            "MainWindow", u"Basketry", None))
        self.checkBox_13.setText(QCoreApplication.translate(
            "MainWindow", u"Management in Living", None))
        self.checkBox_8.setText(QCoreApplication.translate(
            "MainWindow", u"Principles of Costing", None))
        self.checkBox_7.setText(QCoreApplication.translate(
            "MainWindow", u"Business Management", None))
        self.checkBox_18.setText(QCoreApplication.translate(
            "MainWindow", u"Economics", None))
        self.checkBox_16.setText(QCoreApplication.translate(
            "MainWindow", u"Elective Mathematics", None))
        self.checkBox_10.setText(QCoreApplication.translate(
            "MainWindow", u"General Knowledge in Arts", None))
        self.checkBox_15.setText(QCoreApplication.translate(
            "MainWindow", u"Elective ICT", None))
        self.label_35.setText(QCoreApplication.translate(
            "MainWindow", u"Gender:", None))
        self.radioButton.setText(
            QCoreApplication.translate("MainWindow", u"Male", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Female", None))
        self.label_36.setText(QCoreApplication.translate(
            "MainWindow", u"Parent's Contact:", None))
        self.plainTextEdit_5.setPlainText(
            QCoreApplication.translate("MainWindow", u"+233 (0) ", None))
        self.label_37.setText(QCoreApplication.translate(
            "MainWindow", u"Signature:", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Record Signature", None))
        self.label_38.setText(QCoreApplication.translate(
            "MainWindow", u"image path", None))
        self.label_39.setText(QCoreApplication.translate(
            "MainWindow", u"Fingerprint:", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"Take Left Thumb", None))
        self.pushButton_4.setText(QCoreApplication.translate(
            "MainWindow", u"Take Right Thumb", None))
        self.save_edit.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancel_edit.setText(
            QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#b45f4e;\">You do not have any data on your students, please click the button to continue </span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Add Student", None))
    # retranslateUi
