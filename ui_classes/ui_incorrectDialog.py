# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'incorrectDialogsoQYgL.ui'
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


class Ui_incorrectDialog(object):
    def setupUi(self, incorrectDialog):
        if incorrectDialog.objectName():
            incorrectDialog.setObjectName(u"incorrectDialog")
        incorrectDialog.resize(377, 113)
        self.verticalLayout = QVBoxLayout(incorrectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(incorrectDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(incorrectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(incorrectDialog)
        self.buttonBox.accepted.connect(incorrectDialog.accept)
        self.buttonBox.rejected.connect(incorrectDialog.reject)

        QMetaObject.connectSlotsByName(incorrectDialog)
    # setupUi

    def retranslateUi(self, incorrectDialog):
        incorrectDialog.setWindowTitle(QCoreApplication.translate("incorrectDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("incorrectDialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Your Password is incorrect</span></p></body></html>", None))
    # retranslateUi

