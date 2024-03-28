import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo

from ui.ui_fault_injection import Ui_Fault


class SettingFault(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Fault()
        self.m_ui.setupUi(self) 

        # self.fill_fault_parameters()

 
    def fill_fault_parameters(self):
        self.m_ui.exe_timesBox.addItem("100", QSerialPort.Baud1200)
        self.m_ui.exe_timesBox.addItem("1000", QSerialPort.Baud1000)
        self.m_ui.exe_timesBox.addItem("10000", QSerialPort.Baud10000)
        self.m_ui.exe_timesBox.addItem("100000", QSerialPort.Baud10000)
        self.m_ui.exe_timesBox.setCurrentIndex(3)
 
        self.m_ui.modeBox.addItem("0", QSerialPort.zero)
        self.m_ui.modeBox.addItem("1", QSerialPort.one)
        self.m_ui.modeBox.setCurrentIndex(3)
 
        self.m_ui.erBox.addItem("None", QSerialPort.NoParity)
        self.m_ui.erBox.addItem("Even", QSerialPort.EvenParity)
        self.m_ui.erBox.addItem("Space", QSerialPort.SpaceParity)
 
        self.m_ui.bfmBox.addItem("0", QSerialPort.zero)
        self.m_ui.bfmBox.addItem("1", QSerialPort.one)
        self.m_ui.bfmBox.setCurrentIndex(3)
 



   
         

  
         