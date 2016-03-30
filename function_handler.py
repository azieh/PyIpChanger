from mainwindow import MainWindow
from ipchanger import IpChanger
from json_handler import *
import threading

class FunctionHandler:
    """Function handler
    Place to connect classes interfaces together
    """
    def __init__(self):
        self.ui = MainWindow()
        self.ipChanger = IpChanger()
        self.connections()

        self.ui.show()

        self.clients_list = read_json()

        self.ui.add_device(self.ipChanger.get_network_device_list())
        self.ui.add_line_parameters_data(self.clients_list)

    def connections(self):
        self.ui.treeWidget.itemChanged.connect(self.tree_list_add_update)
        self.ui.acceptButton.clicked.connect(self.ip_update)
        self.ui.dhcpButton.clicked.connect(self.dhcp_update)
        self.ui.treeWidget.customContextMenuRequested.connect(self.delete_line_parameter_menu)
        self.ui.delete_client_action.triggered.connect(self.tree_list_delete_update)

    def tree_list_add_update(self, item):
        write_json([item.text(0), item.text(1), item.text(2)])
        self.clients_list = read_json()
        self.ui.add_line_parameters_data(self.clients_list)

    def tree_list_delete_update(self):
        item_activated_in_qtree = self.ui.treeWidget.currentItem()
        if item_activated_in_qtree is not None:
            line = item_activated_in_qtree.text(0)
            ip = item_activated_in_qtree.text(1)
            subnet = item_activated_in_qtree.text(2)
            delete_data([line, ip, subnet])
            self.clients_list = read_json()
            self.ui.add_line_parameters_data(self.clients_list)

    def ip_update(self):
        item_activated_in_qtree = self.ui.treeWidget.currentItem()
        # check if is any item already selected
        result = 0
        if item_activated_in_qtree is not None:
            device = self.ui.comboBox.currentIndex()
            ip = item_activated_in_qtree.text(1)
            subnet = item_activated_in_qtree.text(2)

            result = self.ipChanger.ip_static_changer(device, ip, subnet)
        if result != 0:
            self.ui.show_warning_message_window("Ip address was not change. Check if u have administrator rights.")

    def dhcp_update(self):
        device = self.ui.comboBox.currentIndex()
        result = self.ipChanger.ip_dhcp(device)
        if result != 0:
            self.ui.show_warning_message_window("Ip address was not change. Check if u have administrator rights.")

    def delete_line_parameter_menu(self, position):
        self.ui.menu.addAction(self.ui.delete_client_action)
        self.ui.menu.exec_(self.ui.treeWidget.viewport().mapToGlobal(position))
