from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showMaximized()

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())
