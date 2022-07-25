from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            self.ui.EmailSignInFrame_2.setMaximumSize(QSize(600, 70))
            self.ui.SchoolNameFrame_2.setMaximumSize(QSize(600, 70))
            self.ui.frame_17.setMaximumSize(QSize(600, 70))
            self.ui.frame_21.setMaximumSize(QSize(600, 70))
            self.ui.PasswordSignInFrame_3.setMaximumSize(QSize(290, 70))
            self.ui.PasswordSignInFrame_2.setMaximumSize(QSize(290, 70))

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(1000, 600)
            self.ui.EmailSignInFrame_2.setMaximumSize(QSize(420, 90))
            self.ui.SchoolNameFrame_2.setMaximumSize(QSize(420, 90))
            self.ui.frame_17.setMaximumSize(QSize(420, 70))
            self.ui.frame_21.setMaximumSize(QSize(420, 70))
            self.ui.PasswordSignInFrame_3.setMaximumSize(QSize(200, 90))
            self.ui.PasswordSignInFrame_2.setMaximumSize(QSize(200, 90))

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
