from PyQt5.QtWidgets import *


from mainwindow import MainWindow
from ipchanger import *

import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    #ip_static_changer("192.168.1.1", "255.255.255.0")
    try:
        device_list = get_network_device_list()
    except:
        raise print("Something goes wrong!")
    ui.add_device(device_list)
    #ui.add_device(device_list)
    app.exec_()
