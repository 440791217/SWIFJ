# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_connect.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 372)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 180, 311, 181))
        self.groupBox.setObjectName("groupBox")
        self.secondButton = QtWidgets.QPushButton(self.groupBox)
        self.secondButton.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.secondButton.setObjectName("secondButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 54, 21))
        self.label.setObjectName("label")
        self.fileButton = QtWidgets.QPushButton(self.groupBox)
        self.fileButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.fileButton.setObjectName("fileButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 54, 16))
        self.label_2.setObjectName("label_2")
        self.thirdButton = QtWidgets.QPushButton(self.groupBox)
        self.thirdButton.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.thirdButton.setObjectName("thirdButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(102, 120, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 311, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 54, 21))
        self.label_3.setObjectName("label_3")
        self.serialconnectBox = QtWidgets.QComboBox(self.groupBox_2)
        self.serialconnectBox.setGeometry(QtCore.QRect(160, 30, 131, 22))
        self.serialconnectBox.setObjectName("serialconnectBox")
        self.firstButton = QtWidgets.QPushButton(self.groupBox_2)
        self.firstButton.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.firstButton.setObjectName("firstButton")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 54, 21))
        self.label_4.setObjectName("label_4")
        self.chipBox = QtWidgets.QComboBox(self.groupBox_2)
        self.chipBox.setGeometry(QtCore.QRect(160, 70, 131, 22))
        self.chipBox.setObjectName("chipBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "设备连接"))
        self.groupBox.setTitle(_translate("Form", "操作"))
        self.secondButton.setText(_translate("Form", "初始化"))
        self.label.setText(_translate("Form", "烧写："))
        self.fileButton.setText(_translate("Form", "选择文件"))
        self.label_2.setText(_translate("Form", "初始化："))
        self.thirdButton.setText(_translate("Form", "确定"))
        self.groupBox_2.setTitle(_translate("Form", "串口选择："))
        self.label_3.setText(_translate("Form", "端口号："))
        self.firstButton.setText(_translate("Form", "确定"))
        self.label_4.setText(_translate("Form", "芯片选择："))
