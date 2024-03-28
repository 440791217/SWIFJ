import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo

from ui.ui_fault_injection import Ui_Fault


class SettingFault(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Fault()
        self.m_ui.setupUi(self) 

        self.fill_fault_parameters()
        self.m_ui.ApplyButton.clicked.connect(self.Apply)   #点击确定按钮




    def  Apply(self):
        print("确认提交按钮被点击！")
 
    def fill_fault_parameters(self):
        self.m_ui.exe_timesBox.addItem("100")
        self.m_ui.exe_timesBox.addItem("1000")
        self.m_ui.exe_timesBox.addItem("10000")
        self.m_ui.exe_timesBox.addItem("100000")
        self.m_ui.exe_timesBox.setCurrentIndex(1)
 
        self.m_ui.modeBox.addItem("0")
        self.m_ui.modeBox.addItem("1")
        self.m_ui.modeBox.setCurrentIndex(1)
 
        self.m_ui.erBox.addItem("None")
        self.m_ui.erBox.addItem("Even")
        self.m_ui.erBox.addItem("Space")
        self.m_ui.bfmBox.setCurrentIndex(1)
 
        self.m_ui.bfmBox.addItem("1")
        self.m_ui.bfmBox.addItem("2")
        self.m_ui.bfmBox.setCurrentIndex(1)

        self.m_ui.mem_startBox.addItem("None")
        self.m_ui.mem_startBox.addItem("Even")
        self.m_ui.mem_startBox.addItem("Space")
        self.m_ui.mem_startBox.setCurrentIndex(1)

        self.m_ui.mem_sizeBox.addItem("None")
        self.m_ui.mem_sizeBox.addItem("Even")
        self.m_ui.mem_sizeBox.addItem("Space")
        self.m_ui.mem_sizeBox.setCurrentIndex(1)
 



   
         

  
         