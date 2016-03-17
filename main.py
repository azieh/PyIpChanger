from PyQt5.QtWidgets import *


from mainwindow import MainWindow
from ipchanger import *
from json_handler import *

import sys


def connections():
    ui.treeWidget.itemChanged.connect(tree_list_update)


def tree_list_update(item):
        client_list = [[item.text(0), item.text(1), item.text(2)]]
        write_json([item.text(0), item.text(1), item.text(2)])
        ui.add_line_parameters_data(client_list)
        return [item.text(0), item.text(1), item.text(2)]

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()
    connections()
    device_list = get_network_device_list()
    ui.add_device(device_list)
    ip_static_changer()
    clients_list = read_json()
    ui.add_line_parameters_data(clients_list)
    app.exec_()
