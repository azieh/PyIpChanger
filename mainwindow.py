from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui import gui


class MainWindow(QDialog, gui.Ui_PyIpChanger):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.connections()
        self.treeWidget.setSortingEnabled(True)

    def connections(self):
        self.closeButton.clicked.connect(self.close)

    def add_device(self, elements_list):
        for element in elements_list:
            self.comboBox.addItem(element[0] + ": " + element[1])

    def add_line_parameters_data(self, elements_list):
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(["Line", "Ip", "Subnet"])

        for element in elements_list:
            tree_widget_data = QTreeWidgetItem(element)
            tree_widget_data.setFlags(Qt.ItemIsEditable |
                                      Qt.ItemIsEnabled |
                                      Qt.ItemIsSelectable)
            self.treeWidget.insertTopLevelItem(0, tree_widget_data)
