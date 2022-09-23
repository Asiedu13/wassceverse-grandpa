import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(681, 150)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_item = QFrame(Form)
        self.list_item.setObjectName(u"list_item")
        self.list_item.setFrameShape(QFrame.StyledPanel)
        self.list_item.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.list_item)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pic_side = QFrame(self.list_item)
        self.pic_side.setObjectName(u"pic_side")
        self.pic_side.setMinimumSize(QSize(100, 130))
        self.pic_side.setMaximumSize(QSize(100, 130))
        self.pic_side.setFrameShape(QFrame.StyledPanel)
        self.pic_side.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.pic_side)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.pic_side)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.pic_side)

        self.info_side = QFrame(self.list_item)
        self.info_side.setObjectName(u"info_side")
        self.info_side.setFrameShape(QFrame.StyledPanel)
        self.info_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.info_side)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(self.info_side)
        self.label_18.setObjectName(u"label_18")
        font = QFont()
        font.setFamily(u"JetBrains Mono ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(65, 72, 100);")

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.info_side)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setFamily(u"JetBrains Mono Medium")
        font1.setPointSize(11)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(65, 72, 100);")

        self.verticalLayout.addWidget(self.label_19)

        self.label_20 = QLabel(self.info_side)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: rgb(65, 72, 100);")

        self.verticalLayout.addWidget(self.label_20)


        self.horizontalLayout_2.addWidget(self.info_side)


        self.horizontalLayout.addWidget(self.list_item)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"Flash Barry Allen", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"General Science", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"3 Science 2", None))
    # retranslateUi



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    list = QListWidget()

    item = QListWidgetItem(list)
    item_widget = Ui_Form()
    item.setSizeHint(item_widget.sizeHint())
    list.addItem(item)
    list.setItemWidget(item, item_widget)

    list.addItem("string displayed as string")

    item2 = QListWidgetItem(list)
    item_widget2 = Ui_Form()
    item2.setSizeHint(item_widget2.sizeHint())
    list.addItem(item2)
    list.setItemWidget(item2, item_widget2)

    window_layout = QVBoxLayout(window)
    window_layout.addWidget(title)
    window_layout.addWidget(list)
    window.setLayout(window_layout)

    def searchRes(item):
        print(item.title.text())

    list.itemClicked.connect(searchRes)

    window.show()
    sys.exit(app.exec_())

