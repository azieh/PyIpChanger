from PyQt5.QtWidgets import *
import PyQt5.QtCore
import PyQt5.QtGui
from function_handler import *
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    fh = FunctionHandler()
    app.exec_()

