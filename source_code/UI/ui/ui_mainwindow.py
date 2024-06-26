# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 529)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 764, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigure.setIcon(icon)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../images/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../images/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisconnect.setIcon(icon2)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../images/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon3)
        self.actionQuit.setObjectName("actionQuit")
        self.actionFault = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../images/fault.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFault.setIcon(icon4)
        self.actionFault.setObjectName("actionFault")
        self.actionCon = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\../images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCon.setIcon(icon5)
        self.actionCon.setObjectName("actionCon")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMode = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\../images/mode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMode.setIcon(icon6)
        self.actionMode.setObjectName("actionMode")
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionConfigure)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionFault)
        self.toolBar.addAction(self.actionCon)
        self.toolBar.addAction(self.actionMode)
        self.menu.addAction(self.actionCon)
        self.menu.addAction(self.actionFault)
        self.menu.addAction(self.actionConfigure)
        self.menu.addAction(self.actionMode)
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口调试助手"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu.setTitle(_translate("MainWindow", "编辑"))
        self.actionConfigure.setText(_translate("MainWindow", "串口配置"))
        self.actionConnect.setText(_translate("MainWindow", "打开串口"))
        self.actionDisconnect.setText(_translate("MainWindow", "关闭串口"))
        self.actionQuit.setText(_translate("MainWindow", "清除显示"))
        self.actionFault.setText(_translate("MainWindow", "故障注入参数"))
        self.actionCon.setText(_translate("MainWindow", "设备连接"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionMode.setText(_translate("MainWindow", "故障注入模式"))
