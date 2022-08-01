# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editPDqZCQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect,QDate, QDateTime, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(597, 728)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 30))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_19)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout.addWidget(self.label_11)

        self.plainTextEdit = QPlainTextEdit(self.frame_19)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 30))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(110, 0))
        self.label_12.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_2.addWidget(self.label_12)

        self.plainTextEdit_2 = QPlainTextEdit(self.frame_18)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 30))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(110, 0))
        self.label_13.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_3.addWidget(self.label_13)

        self.plainTextEdit_3 = QPlainTextEdit(self.frame_17)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.horizontalLayout_3.addWidget(self.plainTextEdit_3)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(110, 0))
        self.label_14.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_4.addWidget(self.label_14)

        self.dateEdit = QDateEdit(self.frame_16)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEdit.setMaximumDate(QDate(2080, 12, 31))
        self.dateEdit.setMinimumDate(QDate(1980, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_4.addWidget(self.dateEdit)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(110, 0))
        self.label_15.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_5.addWidget(self.label_15)

        self.comboBox = QComboBox(self.frame_15)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_6.addWidget(self.label_16)

        self.textEdit = QTextEdit(self.frame_14)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_6.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 30))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_7.addWidget(self.label_17)

        self.plainTextEdit_4 = QPlainTextEdit(self.frame_13)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_7.addWidget(self.plainTextEdit_4)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(110, 0))
        self.label_18.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_8.addWidget(self.label_18)

        self.dateEdit_2 = QDateEdit(self.frame_12)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setDate(QDate(2019, 1, 1))

        self.horizontalLayout_8.addWidget(self.dateEdit_2)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_9.addWidget(self.label)

        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 150))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_24 = QCheckBox(self.frame_20)
        self.checkBox_24.setObjectName(u"checkBox_24")

        self.gridLayout.addWidget(self.checkBox_24, 8, 4, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_20)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 3, 2, 2, 1)

        self.checkBox_12 = QCheckBox(self.frame_20)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout.addWidget(self.checkBox_12, 13, 4, 1, 1)

        self.checkBox_21 = QCheckBox(self.frame_20)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.gridLayout.addWidget(self.checkBox_21, 5, 4, 3, 1)

        self.checkBox_2 = QCheckBox(self.frame_20)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)

        self.checkBox_17 = QCheckBox(self.frame_20)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout.addWidget(self.checkBox_17, 1, 2, 2, 1)

        self.checkBox_22 = QCheckBox(self.frame_20)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.gridLayout.addWidget(self.checkBox_22, 5, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.frame_20)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout.addWidget(self.checkBox_11, 11, 2, 3, 1)

        self.checkBox_14 = QCheckBox(self.frame_20)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout.addWidget(self.checkBox_14, 14, 2, 2, 2)

        self.checkBox_4 = QCheckBox(self.frame_20)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 2)

        self.checkBox_23 = QCheckBox(self.frame_20)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.gridLayout.addWidget(self.checkBox_23, 5, 2, 1, 1)

        self.checkBox = QCheckBox(self.frame_20)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)

        self.checkBox_20 = QCheckBox(self.frame_20)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout.addWidget(self.checkBox_20, 10, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.frame_20)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 9, 4, 2, 1)

        self.checkBox_3 = QCheckBox(self.frame_20)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 0, 4, 1, 1)

        self.checkBox_6 = QCheckBox(self.frame_20)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 3, 4, 2, 1)

        self.checkBox_19 = QCheckBox(self.frame_20)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout.addWidget(self.checkBox_19, 13, 0, 1, 1)

        self.checkBox_13 = QCheckBox(self.frame_20)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout.addWidget(self.checkBox_13, 14, 0, 2, 2)

        self.checkBox_8 = QCheckBox(self.frame_20)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_8, 7, 2, 3, 1)

        self.checkBox_7 = QCheckBox(self.frame_20)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 7, 0, 3, 2)

        self.checkBox_18 = QCheckBox(self.frame_20)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout.addWidget(self.checkBox_18, 2, 4, 1, 1)

        self.checkBox_16 = QCheckBox(self.frame_20)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout.addWidget(self.checkBox_16, 2, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.frame_20)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 10, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.frame_20)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout.addWidget(self.checkBox_15, 14, 4, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_20)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_12.addWidget(self.label_4)

        self.radioButton = QRadioButton(self.frame_8)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(110, 0))
        self.radioButton.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_12.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_8)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_12.addWidget(self.radioButton_2)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(110, 0))
        self.label_5.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_13.addWidget(self.label_5)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame_7)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(0, 25))
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_13.addWidget(self.plainTextEdit_5)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(110, 0))
        self.label_6.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_14.addWidget(self.label_6)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_14.addWidget(self.pushButton_2)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(140, 0))
        self.label_20.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_14.addWidget(self.label_20)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(110, 0))
        self.label_7.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_15.addWidget(self.label_7)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_15.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_15.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.save = QPushButton(self.frame_2)
        self.save.setObjectName(u"save")

        self.horizontalLayout_10.addWidget(self.save)

        self.close = QPushButton(self.frame_2)
        self.close.setObjectName(u"close")

        self.horizontalLayout_10.addWidget(self.close)


        self.verticalLayout.addWidget(self.frame_2)

        self.close.clicked.connect(Dialog.reject)


        self.retranslateUi(Dialog)

        def accept_dialog():
            Dialog.accept
        
        self.accept = accept_dialog()

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Surname:                   ", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"First Name:                ", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Other Names:            ", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Date of Birth:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd/MM/yyyy", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Course:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"General Science", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Business", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Home Economics", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"General Arts", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Visual Arts", None))

        self.label_16.setText(QCoreApplication.translate("Dialog", u"Class:", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"BECE Index Number:", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Year Completed:", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Electives", None))
        self.checkBox_24.setText(QCoreApplication.translate("Dialog", u"Textile", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Geography", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"Ceramics and Sculpture", None))
        self.checkBox_21.setText(QCoreApplication.translate("Dialog", u"Financial Accounting", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Chemistry", None))
        self.checkBox_17.setText(QCoreApplication.translate("Dialog", u"French", None))
        self.checkBox_22.setText(QCoreApplication.translate("Dialog", u"Government", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"Picture Making", None))
        self.checkBox_14.setText(QCoreApplication.translate("Dialog", u"Food and Nutrition", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Literature in English", None))
        self.checkBox_23.setText(QCoreApplication.translate("Dialog", u"Religious Studies", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Biology", None))
        self.checkBox_20.setText(QCoreApplication.translate("Dialog", u"Leather Works", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Graphic Design", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Physics", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"History", None))
        self.checkBox_19.setText(QCoreApplication.translate("Dialog", u"Basketry", None))
        self.checkBox_13.setText(QCoreApplication.translate("Dialog", u"Management in Living", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Principles of Costing", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Business Management", None))
        self.checkBox_18.setText(QCoreApplication.translate("Dialog", u"Economics", None))
        self.checkBox_16.setText(QCoreApplication.translate("Dialog", u"Elective Mathematics", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"General Knowledge in Arts", None))
        self.checkBox_15.setText(QCoreApplication.translate("Dialog", u"Elective ICT", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Gender:", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Female", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Parent's Contact:", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("Dialog", u"+233 (0) ", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Signature:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Record Signature", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"image path", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Fingerprint:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Take Left Thumb", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Take Right Thumb", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

