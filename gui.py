# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyIpChanger(object):
    def setupUi(self, PyIpChanger):
        PyIpChanger.setObjectName("PyIpChanger")
        PyIpChanger.resize(426, 333)
        PyIpChanger.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PyIpChanger.setWindowIcon(icon)
        PyIpChanger.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PyIpChanger)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(PyIpChanger)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(250, 250, 250, 90), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom: 1px solid darkgrey;\n"
"}\n"
"QLabel{\n"
"background-color: transparent;\n"
"border: none;\n"
"}\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border: none;\n"
"max-width: 64px;\n"
"max-height: 64px;\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: grey;\n"
"border-radius: 30px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: dark grey;\n"
"border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QtCore.QSize(64, 64))
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 4, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setText("")
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(self.icon2)
        self.closeButton.setIconSize(QtCore.QSize(64, 64))
        self.closeButton.setFlat(False)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 1, 6, 1, 1)
        self.acceptButton = QtWidgets.QPushButton(self.frame)
        self.acceptButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceptButton.setIcon(icon3)
        self.acceptButton.setIconSize(QtCore.QSize(64, 64))
        self.acceptButton.setObjectName("acceptButton")
        self.gridLayout.addWidget(self.acceptButton, 1, 3, 1, 1)
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMaximumSize(QtCore.QSize(64, 64))
        self.logo.setLineWidth(0)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setIndent(0)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 1, 0, 1, 1)
        self.dhcpButton = QtWidgets.QPushButton(self.frame)
        self.dhcpButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/dhcp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dhcpButton.setIcon(icon4)
        self.dhcpButton.setIconSize(QtCore.QSize(64, 64))
        self.dhcpButton.setObjectName("dhcpButton")
        self.gridLayout.addWidget(self.dhcpButton, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.comboBox = QtWidgets.QComboBox(PyIpChanger)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.treeWidget = QtWidgets.QTreeWidget(PyIpChanger)
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.headerItem().setText(2, "3")
        self.verticalLayout.addWidget(self.treeWidget)

        self.retranslateUi(PyIpChanger)
        QtCore.QMetaObject.connectSlotsByName(PyIpChanger)

    def retranslateUi(self, PyIpChanger):
        _translate = QtCore.QCoreApplication.translate
        PyIpChanger.setWindowTitle(_translate("PyIpChanger", "PyIpChanger"))
        self.treeWidget.setSortingEnabled(True)

import icons_rc
