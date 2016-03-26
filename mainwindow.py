from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import gui


class MainWindow(QDialog, gui.Ui_PyIpChanger):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.connections()
        self.treeWidget.setSortingEnabled(True)

        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(["Line", "Ip", "Subnet"])

    def connections(self):
        self.closeButton.clicked.connect(self.close)
        self.addButton.clicked.connect(self.add_blank_line_parameters)

    def add_device(self, elements_list):
        for element in elements_list:
            self.comboBox.addItem(element[0] + ": " + element[1])

    def add_line_parameters_data(self, elements_list):

        self.treeWidget.clear()

        # for element in elements_list:
        #    item = self.treeWidget.findItems(element[0], Qt.MatchExactly, int(0))
        #    if len(item) >= 0:
        #        break

        for element in elements_list:
            tree_widget_data = QTreeWidgetItem(element)
            tree_widget_data.setFlags(Qt.ItemIsEditable |
                                      Qt.ItemIsEnabled |
                                      Qt.ItemIsSelectable)
            self.treeWidget.insertTopLevelItem(0, tree_widget_data)

    def add_blank_line_parameters(self):
        element = ['Null', 'Null', 'Null']
        tree_widget_data = QTreeWidgetItem(element)
        tree_widget_data.setFlags(Qt.ItemIsEditable |
                                  Qt.ItemIsEnabled |
                                  Qt.ItemIsSelectable)
        self.treeWidget.insertTopLevelItem(0, tree_widget_data)

    def delete_line_parameter(self):
        pass

    def show_warning_message_window(self, text):
        title = "ERROR"
        QMessageBox.critical(self, title, text, QMessageBox.Close)
