# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signInFailedOneDialogRzSozL.ui'
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


class Ui_signInFailedOneDialog(object):
    def setupUi(self, signInFailedOneDialog):
        if signInFailedOneDialog.objectName():
            signInFailedOneDialog.setObjectName(u"signInFailedOneDialog")
        signInFailedOneDialog.resize(377, 167)
        self.verticalLayout = QVBoxLayout(signInFailedOneDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(signInFailedOneDialog)
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

        self.buttonBox = QDialogButtonBox(signInFailedOneDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(signInFailedOneDialog)
        self.buttonBox.accepted.connect(signInFailedOneDialog.accept)
        self.buttonBox.rejected.connect(signInFailedOneDialog.reject)

        QMetaObject.connectSlotsByName(signInFailedOneDialog)
    # setupUi

    def retranslateUi(self, signInFailedOneDialog):
        signInFailedOneDialog.setWindowTitle(QCoreApplication.translate("signInFailedOneDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("signInFailedOneDialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Your school name does not exist on our servers or does not match with the email you provided</span></p></body></html>", None))
    # retranslateUi
