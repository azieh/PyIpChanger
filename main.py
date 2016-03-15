from PyQt5.QtWidgets import *


from mainwindow import MainWindow
from ipchanger import *

import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    #ipstaticchanger("192.168.1.1", "255.255.255.0")
    try:
        ipdhcp()
    except:
        raise print("asdasd")

    app.exec_()
