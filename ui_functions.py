from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showMaximized()

        self.ui.email_error.setHidden(True)
        self.ui.school_name_error.setHidden(True)
        self.ui.school_code_error.setHidden(True)
        self.ui.password_error.setHidden(True)