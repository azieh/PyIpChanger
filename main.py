from PyQt5.QtWidgets import *
from function_handler import *
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    fh = FunctionHandler()
    app.exec_()

