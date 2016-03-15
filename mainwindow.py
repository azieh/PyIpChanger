from PyQt5.QtWidgets import *

from ui import gui


class MainWindow(QDialog, gui.Ui_PyIpChanger):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.closeButton.clicked.connect(self.close)
