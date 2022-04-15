from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(870, 740))
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            " QScrollBar:vertical {\n"
                                "    border: none;\n"
                                "    background-color: rgb(45, 45, 68);\n"
                                "    width: 14px;\n"
                                "    margin: 15px 0 15px 0;\n"
                                "    border-radius: 0px;\n"
                                " }\n"
                                "\n"
                                "/*  HANDLE BAR VERTICAL */\n"
                                "QScrollBar::handle:vertical {    \n"
                                "    background-color: rgb(80, 80, 122);\n"
                                "    min-height: 30px;\n"
                                "    border-radius: 7px;\n"
                                "}\n"
                                "QScrollBar::handle:vertical:hover{\n"
                                "    background-color: rgb(92, 84, 112);\n"
                                "}\n"
                                "QScrollBar::handle:vertical:pressed {    \n"
                                "    background-color: rgb(65, 59, 79);\n"
                                "}\n"
                                "\n"
                                "/* BTN TOP - SCROLLBAR */\n"
                                "QScrollBar::sub-line:vertical {\n"
                                "    border: none;\n"
                                "    background-color: rgb(59, 59, 90);\n"
                                "    height: 15px;\n"
                                "    border-top-left-radius: 7px;\n"
                                "    border-top-right-radius: 7px;\n"
                                "    margin-bottom:2px;\n"
                                "    subcontrol-position: top;\n"
                                "    subcontrol-origin: margin;\n"
                                "}\n"
                                "QScrollBar::sub-line:vertical:hover {\n"
                                "    background-color: rgb(92, 84, 112);\n"
                                "}\n"
                                "QScrollBar::sub-line:vertical:pressed {    \n"
                                "    background-color: rgb(65, 59, 79);\n"
                                "}\n"
                                "\n"
                                "/* BTN BOTTOM - SCROLLBAR */\n"
                                "QScrollBar::add-line:vertical {\n"
                                "    border: none;\n"
                                "    background-color: rgb(59, 59, 90);\n"
                                "    height: 15px;\n"
                                "    border-bottom-left-radius: 7px;\n"
                                "    border-bottom-right-radius: 7px;\n"
                                "    subcontrol-position: bottom;\n"
                                "    subcontrol-origin: margin;\n"
                                "}\n"
                                "QScrollBar::add-line:vertical:hover {    \n"
                                "    background-color: rgb(92, 84, 112);\n"
                                "}\n"
                                "QScrollBar::add-line:vertical:pressed {\n"
                                "    background-color: rgb(65, 59, 79);\n"
                                "}\n"
                                "\n"
                                "/* RESET ARROW */\n"
                                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                "    background: none;\n"
                                "}\n"
                                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                "    background: none;\n"
                                "}"
        )
        self.drop_shadow_layout = QHBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.background = QFrame(self.centralwidget)
        self.background.setMinimumSize(QSize(870, 740))
        self.background.setStyleSheet("background-color: rgb(42, 36, 56);\n"
                                      "border-radius:  15px;")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.background.setObjectName("background")
        self.backgroundLayout = QVBoxLayout(self.background)
        self.backgroundLayout.setContentsMargins(0, 0, 0, 0)
        self.backgroundLayout.setSpacing(0)
        self.backgroundLayout.setObjectName("backgroundLayout")
        self.title_bar = QFrame(self.background)
        self.title_bar.setMaximumSize(QSize(16777215, 30))
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.title_barLayout = QHBoxLayout(self.title_bar)
        self.title_barLayout.setContentsMargins(0, 0, 0, 0)
        self.title_barLayout.setSpacing(0)
        self.title_barLayout.setObjectName("title_barLayout")
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.frame_titleLayout = QVBoxLayout(self.frame_title)
        self.frame_titleLayout.setContentsMargins(9, 0, 0, 0)
        self.frame_titleLayout.setSpacing(0)
        self.frame_titleLayout.setObjectName("frame_titleLayout")
        self.label_title = QLabel(self.frame_title)
        font = QFont()
        font.setFamily("Montserrat")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(219, 216, 227);")
        self.label_title.setOpenExternalLinks(False)
        self.label_title.setObjectName("label_title")
        self.frame_titleLayout.addWidget(self.label_title)
        self.title_barLayout.addWidget(self.frame_title)
        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QSize(120, 30))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.frame_btnsLayout = QHBoxLayout(self.frame_btns)
        self.frame_btnsLayout.setContentsMargins(-1, 4, -1, 4)
        self.frame_btnsLayout.setObjectName("frame_btnsLayout")
        self.btn_minimize = QPushButton(self.frame_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(22, 22))
        self.btn_minimize.setMaximumSize(QSize(22, 22))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "    border: none;\n"
                                        "    border-radius: 11px;\n"
                                        "    background-color: rgb(55, 74, 98);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    \n"
                                        "    background-color: rgb(89, 121, 159);\n"
                                        "}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.frame_btnsLayout.addWidget(self.btn_minimize)
        self.btn_maximize = QPushButton(self.frame_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setMinimumSize(QSize(22, 22))
        self.btn_maximize.setMaximumSize(QSize(22, 22))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
                                        "    border: none;\n"
                                        "    border-radius: 11px;\n"
                                        "    background-color: rgb(152, 140, 51);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    \n"
                                        "    background-color: rgb(198, 181, 66);\n"
                                        "}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.frame_btnsLayout.addWidget(self.btn_maximize)
        self.btn_close = QPushButton(self.frame_btns)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(22, 22))
        self.btn_close.setMaximumSize(QSize(22, 22))
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    border: none;\n"
                                     "    border-radius: 11px;\n"
                                     "    background-color: rgb(174, 0, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    \n"
                                     "    background-color: rgb(255, 0, 0);\n"
                                     "}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.frame_btnsLayout.addWidget(self.btn_close)
        self.title_barLayout.addWidget(self.frame_btns)
        self.backgroundLayout.addWidget(self.title_bar)
        self.content_bar = QFrame(self.background)
        self.content_bar.setStyleSheet("background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.content_bar.setObjectName("content_bar")
        self.content_barLayout = QHBoxLayout(self.content_bar)
        self.content_barLayout.setContentsMargins(0, 0, 0, 0)
        self.content_barLayout.setSpacing(0)
        self.content_barLayout.setObjectName("content_barLayout")
        self.frame = QFrame(self.content_bar)
        self.frame.setMaximumSize(QSize(180, 16777215))
        self.frame.setStyleSheet("background-color: #352f44;\n"
                                 "border-radius: 0px;\n"
                                 "border-bottom-left-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLayout.setObjectName("frameLayout")
        self.search_box = QPlainTextEdit(self.frame)
        self.search_box.setMinimumSize(QSize(0, 30))
        self.search_box.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        self.search_box.setFont(font)
        self.search_box.setStyleSheet("QPlainTextEdit {\n"
                                      "    border: 0;\n"
                                      "      border-bottom: 1px solid #dbd8e3;\n"
                                      "      outline: 0;\n"
                                      "      font-size: 16px;\n"
                                      "      color: #ffffff;\n"
                                      "    border-radius: 0;\n"
                                      "      background: transparent;\n"
                                      "    margin-left:4px;\n"
                                      "    margin-right: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "QPlainTextEdit::placeholder {\n"
                                      "    font-family: Monsterrat;\n"
                                      "    color: transparent;\n"
                                      "  }\n"
                                      "\n"
                                      "QPlainTextEdit:placeholder-shown {\n"
                                      "    font-size: 1.3rem;\n"
                                      "    cursor: text;\n"
                                      "    top: 20px;\n"
                                      "  }")
        self.search_box.setInputMethodHints(Qt.ImhNone)
        self.search_box.setMidLineWidth(1)
        self.search_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_box.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_box.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.search_box.setObjectName("search_box")
        self.frameLayout.addWidget(self.search_box)
        self.import_file = QPushButton(self.frame)
        self.import_file.setMinimumSize(QSize(0, 40))
        self.import_file.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.import_file.setFont(font)
        self.import_file.setStyleSheet("QPushButton {\n"
                                       "color: rgb(219, 216, 227);\n"
                                       "background-color: rgb(92, 84, 112);\n"
                                       "border-radius: 0;\n"
                                       "font-size: 16px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(111, 101, 135);\n"
                                       "}")
        self.import_file.setObjectName("import_file")
        self.frameLayout.addWidget(self.import_file)
        self.import_folder = QPushButton(self.frame)
        self.import_folder.setMinimumSize(QSize(0, 40))
        self.import_folder.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        self.import_folder.setFont(font)
        self.import_folder.setStyleSheet("QPushButton {\n"
                                         "color: rgb(219, 216, 227);\n"
                                         "background-color: rgb(92, 84, 112);\n"
                                         "border-radius: 0;\n"
                                         "font-size: 16px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(111, 101, 135);\n"
                                         "}")
        self.import_folder.setObjectName("import_folder")
        self.frameLayout.addWidget(self.import_folder)
        self.server_info = QPushButton(self.frame)
        self.server_info.setMinimumSize(QSize(0, 40))
        self.server_info.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(17)
        self.server_info.setFont(font)
        self.server_info.setStyleSheet("QPushButton {\n"
                                       "color: rgb(219, 216, 227);\n"
                                       "background-color: rgb(92, 84, 112);\n"
                                       "border-radius: 0;\n"
                                       "font-size: 16px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(111, 101, 135);\n"
                                       "}")
        self.server_info.setObjectName("server_info")
        self.frameLayout.addWidget(self.server_info)
        self.search_results = QFrame(self.frame)
        self.search_results.setFrameShape(QFrame.StyledPanel)
        self.search_results.setFrameShadow(QFrame.Raised)
        self.search_results.setObjectName("search_results")
        self.frameLayout.addWidget(self.search_results)
        self.content_barLayout.addWidget(self.frame)
        self.frame_2 = QFrame(self.content_bar)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2Layout = QVBoxLayout(self.frame_2)
        self.frame_2Layout.setContentsMargins(-1, 0, 0, 0)
        self.frame_2Layout.setSpacing(0)
        self.frame_2Layout.setObjectName("frame_2Layout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QSize(610, 200))
        self.frame_3.setMaximumSize(QSize(16777215, 220))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3Layout = QHBoxLayout(self.frame_3)
        self.frame_3Layout.setSpacing(20)
        self.frame_3Layout.setObjectName("frame_3Layout")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_3Layout.addWidget(self.frame_5)
        self.previous_arrow = QPushButton(self.frame_3)
        self.previous_arrow.setMinimumSize(QSize(70, 70))
        self.previous_arrow.setMaximumSize(QSize(70, 70))
        self.previous_arrow.setStyleSheet("QPushButton {\n"
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
        self.previous_arrow.setObjectName("previous_arrow")
        self.frame_3Layout.addWidget(self.previous_arrow)
        self.pic = QLabel(self.frame_3)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy)
        self.pic.setMaximumSize(QSize(150, 200))
        self.pic.setText("")
        self.pic.setPixmap(QPixmap(
            "Include/img/user-sign-icon-person-symbol-human-avatar-vector-12693195.jpg"))
        self.pic.setScaledContents(True)
        self.pic.setObjectName("pic")
        self.frame_3Layout.addWidget(self.pic)
        self.next_arrow = QPushButton(self.frame_3)
        self.next_arrow.setMinimumSize(QSize(70, 70))
        self.next_arrow.setMaximumSize(QSize(70, 70))
        self.next_arrow.setStyleSheet("QPushButton {\n"
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
        self.next_arrow.setObjectName("next_arrow")
        self.frame_3Layout.addWidget(self.next_arrow)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_3Layout.addWidget(self.frame_6)
        self.frame_2Layout.addWidget(self.frame_3)
        self.student_info = QFrame(self.frame_2)
        self.student_info.setStyleSheet("font-size:17px;font-family: Montserrat;\n"
                                        "color: rgb(219, 216, 227);")
        self.student_info.setFrameShape(QFrame.StyledPanel)
        self.student_info.setFrameShadow(QFrame.Raised)
        self.student_info.setObjectName("student_info")
        self.student_infoLayout = QVBoxLayout(self.student_info)
        self.student_infoLayout.setContentsMargins(2, 2, 2, 2)
        self.student_infoLayout.setSpacing(2)
        self.student_infoLayout.setObjectName("student_infoLayout")
        self.info = QListWidget(self.student_info)
        self.info.setStyleSheet("QListWidget {\n"
                                "    background-color: rgb(42, 36, 56);\n"
                                "    color: rgb(219, 216, 227);\n"
                                "}\n"
                                "\n"
                                )
        self.info.setSelectionMode(QAbstractItemView.NoSelection)
        self.info.setObjectName("info")
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        item = QListWidgetItem()
        self.info.addItem(item)
        self.student_infoLayout.addWidget(self.info)
        self.signature_frame = QFrame(self.student_info)
        self.signature_frame.setMaximumSize(QSize(16777215, 100))
        self.signature_frame.setMinimumSize(QSize(16777215, 100))
        self.signature_frame.setFrameShape(QFrame.StyledPanel)
        self.signature_frame.setFrameShadow(QFrame.Raised)
        self.signature_frame.setObjectName("signature_frame")
        self.signature_frameLayout = QVBoxLayout(self.signature_frame)
        self.signature_frameLayout.setContentsMargins(0, 0, 0, 0)
        self.signature_frameLayout.setSpacing(0)
        self.signature_frameLayout.setObjectName("signature_frameLayout")
        self.signature_text = QLabel(self.signature_frame)
        self.signature_text.setObjectName("signature_text")
        self.signature_text.setMaximumSize(QSize(16777215, 40))
        self.signature_text.setMinimumSize(QSize(0, 40))
        self.signature_frameLayout.addWidget(self.signature_text)
        self.frame_4 = QFrame(self.signature_frame)
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4Layout = QVBoxLayout(self.frame_4)
        self.frame_4Layout.setObjectName("frame_4Layout")
        self.label = QLabel(self.frame_4)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_4Layout.addWidget(
            self.label, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.signature_frameLayout.addWidget(self.frame_4)
        self.student_infoLayout.addWidget(self.signature_frame)
        self.fingerprint_frame = QFrame(self.student_info)
        self.fingerprint_frame.setFrameShape(QFrame.StyledPanel)
        self.fingerprint_frame.setFrameShadow(QFrame.Raised)
        self.fingerprint_frame.setObjectName("fingerprint_frame")
        self.frameLayout_7 = QVBoxLayout(self.fingerprint_frame)
        self.frameLayout_7.setObjectName("frameLayout_7")
        self.fingerprint_text = QLabel(self.fingerprint_frame)
        self.fingerprint_text.setObjectName("fingerprint_text")
        self.frameLayout_7.addWidget(self.fingerprint_text)
        self.frame_7 = QFrame(self.fingerprint_frame)
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.title_barLayout_6 = QHBoxLayout(self.frame_7)
        self.title_barLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title_barLayout_6.setObjectName("title_barLayout_6")
        self.left_thumb = QLabel(self.frame_7)
        self.left_thumb.setMinimumSize(QSize(0, 100))
        self.left_thumb.setMaximumSize(QSize(100, 100))
        self.left_thumb.setObjectName("left_thumb")
        self.left_thumb.setPixmap(QPixmap("Include/img/finger-left.jpg"))
        self.left_thumb.setScaledContents(True)
        self.title_barLayout_6.addWidget(
            self.left_thumb, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.right_thumb = QLabel(self.frame_7)
        self.right_thumb.setMinimumSize(QSize(0, 100))
        self.right_thumb.setMaximumSize(QSize(100, 100))
        self.right_thumb.setObjectName("right_thumb")
        self.right_thumb.setPixmap(QPixmap("Include/img/finger-right.jpg"))
        self.right_thumb.setScaledContents(True)
        self.title_barLayout_6.addWidget(
            self.right_thumb, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.frameLayout_7.addWidget(self.frame_7)
        self.student_infoLayout.addWidget(self.fingerprint_frame)
        self.edit_btn = QPushButton(self.student_info)
        self.edit_btn.setMinimumSize(QSize(0, 50))
        self.edit_btn.setMaximumSize(QSize(16777215, 50))
        self.edit_btn.setStyleSheet("QPushButton {\n"
                                    "color: rgb(219, 216, 227);\n"
                                    "background-color: rgb(92, 84, 112);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(109, 100, 145);\n"
                                    "}")
        self.edit_btn.setObjectName("edit_btn")
        self.student_infoLayout.addWidget(self.edit_btn)
        self.frame_2Layout.addWidget(self.student_info)
        self.content_barLayout.addWidget(self.frame_2)
        self.backgroundLayout.addWidget(self.content_bar)
        self.drop_shadow_layout.addWidget(self.background)

        self.credits_bar = QFrame(self.background)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(
            u"background-color: rgb(42, 36, 56); border-radius: 0px; border-bottom-left-radius: 15px;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.credits_barLayout = QHBoxLayout(self.credits_bar)
        self.credits_barLayout.setSpacing(0)
        self.credits_barLayout.setObjectName(u"credits_barLayout")
        self.credits_barLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.credits_barLayout.addWidget(self.frame_grip)

        self.backgroundLayout.addWidget(self.credits_bar)

        self.drop_shadow_layout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "AppName"))
        self.search_box.setPlaceholderText(
            _translate("MainWindow", "Search Student"))
        self.import_file.setText(_translate("MainWindow", "Import File"))
        self.import_folder.setText(_translate("MainWindow", "Import Folder"))
        self.server_info.setText(_translate("MainWindow", "Get From Server"))
        self.previous_arrow.setText(_translate("MainWindow", "Previous"))
        self.next_arrow.setText(_translate("MainWindow", "Next"))
        __sortingEnabled = self.info.isSortingEnabled()
        self.info.setSortingEnabled(False)
        item = self.info.item(0)
        item.setTextAlignment(Qt.AlignHCenter)
        item.setTextColor(QColor(47,174,195))
        item.setText(_translate("MainWindow", "Name:"))
        item = self.info.item(1)
        item.setText(_translate("MainWindow", "School:"))
        item = self.info.item(2)
        item.setText(_translate("MainWindow", "Class:"))
        item = self.info.item(3)
        item.setText(_translate("MainWindow", "Course:"))
        item = self.info.item(4)
        item.setText(_translate("MainWindow", "Electives:"))
        item = self.info.item(5)
        item.setText(_translate("MainWindow", "    Elective 1"))
        item = self.info.item(6)
        item.setText(_translate("MainWindow", "    Elective 2"))
        item = self.info.item(7)
        item.setText(_translate("MainWindow", "    Elective 3"))
        item = self.info.item(8)
        item.setText(_translate("MainWindow", "    Elective 4"))
        item = self.info.item(9)
        item.setText(_translate("MainWindow", "Date of Birth:"))
        item = self.info.item(10)
        item.setText(_translate("MainWindow", "Gender:"))
        item = self.info.item(11)
        item.setText(_translate("MainWindow", "BECE Index Number:"))
        item = self.info.item(12)
        item.setText(_translate("MainWindow", "Parent\'s Contact:"))
        self.info.setSortingEnabled(__sortingEnabled)
        self.signature_text.setText(_translate("MainWindow", "Signature:"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.fingerprint_text.setText(_translate("MainWindow", "Fingerprint"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
