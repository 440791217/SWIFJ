import sys
import json
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo

from ui.ui_settingdialog import Ui_Dialog


class Settings():
    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.string_baud_rate = ""
        self.data_bits = QSerialPort.Data8
        self.string_data_bits = ""
        self.parity = QSerialPort.NoParity
        self.string_parity = ""
        self.stop_bits =  QSerialPort.OneStop
        self.string_stop_bits = ""
        self.flow_control = QSerialPort.SoftwareControl
        self.string_flow_control = ""
        self.local_echo_enabled = False

class Settingtest():
    def __init__(self):
        self.name = ""
        self.baud_rate = 0
        self.data_bits = QSerialPort.Data8
        self.parity = QSerialPort.NoParity
        self.stop_bits =  QSerialPort.OneStop
        self.flow_control = QSerialPort.SoftwareControl


class SettingDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Dialog()
        self.m_ui.setupUi(self) 
        self.m_currentSettings = Settings() #m_currentSettings初始化
        self.m_currentSet = Settingtest() #m_currentSet初始化

        self.m_ui.applyButton.clicked.connect(self.apply)

        # self.serial_port_file()
        self.fill_ports_parameters()
        self.full_port_info()


    def apply(self):
        self.update_settings()   #更新m_currentSettings值
        self.hide() 

    def setting(self):
        self.update_setting()
        return self.m_currentSet

    def full_port_info(self):
        self.m_ui.serialPortInfoListBox.clear()
        for info in QSerialPortInfo.availablePorts():
            self.m_ui.serialPortInfoListBox.addItem(info.portName())

    # def serial_port_file():

 
    def fill_ports_parameters(self):
        self.m_ui.baudRateBox.addItem("9600", QSerialPort.Baud9600)
        self.m_ui.baudRateBox.addItem("19200", QSerialPort.Baud19200)
        self.m_ui.baudRateBox.addItem("38400", QSerialPort.Baud38400)
        self.m_ui.baudRateBox.addItem("115200", QSerialPort.Baud115200)
        self.m_ui.baudRateBox.addItem("Custom")
        self.m_ui.baudRateBox.setCurrentIndex(3)
 
        self.m_ui.dataBitsBox.addItem("5", QSerialPort.Data5)
        self.m_ui.dataBitsBox.addItem("6", QSerialPort.Data6)
        self.m_ui.dataBitsBox.addItem("7", QSerialPort.Data7)
        self.m_ui.dataBitsBox.addItem("8", QSerialPort.Data8)
        self.m_ui.dataBitsBox.setCurrentIndex(3)
 
        self.m_ui.parityBox.addItem("None", QSerialPort.NoParity)
        self.m_ui.parityBox.addItem("Even", QSerialPort.EvenParity)
        self.m_ui.parityBox.addItem("Odd", QSerialPort.OddParity)
        self.m_ui.parityBox.addItem("Mark", QSerialPort.MarkParity)
        self.m_ui.parityBox.addItem("Space", QSerialPort.SpaceParity)
 
        self.m_ui.stopBitsBox.addItem("1", QSerialPort.OneStop)
        if sys.platform == "win32":
            self.m_ui.stopBitsBox.addItem("1.5", QSerialPort.OneAndHalfStop)
 
        self.m_ui.stopBitsBox.addItem("2", QSerialPort.TwoStop)
 
        self.m_ui.flowControlBox.addItem("None", QSerialPort.NoFlowControl)
        self.m_ui.flowControlBox.addItem("RTS/CTS", QSerialPort.HardwareControl)
        self.m_ui.flowControlBox.addItem("XON/XOFF", QSerialPort.SoftwareControl)


    def update_settings(self):
        self.m_currentSettings.name = self.m_ui.serialPortInfoListBox.currentText()
 
        self.m_currentSettings.baud_rate = self.m_ui.baudRateBox.currentData()
        self.m_currentSettings.string_baud_rate = f"{self.m_currentSettings.baud_rate}"
 
        self.m_currentSettings.data_bits = self.m_ui.dataBitsBox.currentData()
        self.m_currentSettings.string_data_bits = self.m_ui.dataBitsBox.currentText()
 
        self.m_currentSettings.parity = self.m_ui.parityBox.currentData()
        self.m_currentSettings.string_parity = self.m_ui.parityBox.currentText()
 
        self.m_currentSettings.stop_bits = self.m_ui.stopBitsBox.currentData()
        self.m_currentSettings.string_stop_bits = self.m_ui.stopBitsBox.currentText()
 
        self.m_currentSettings.flow_control = self.m_ui.flowControlBox.currentData()
        self.m_currentSettings.string_flow_control = self.m_ui.flowControlBox.currentText()    
         
    def update_setting(self):
        self.m_currentSet.name = self.m_ui.serialPortInfoListBox.currentText()
        self.m_currentSet.baud_rate = self.m_ui.baudRateBox.currentData()
        self.m_currentSet.data_bits = self.m_ui.dataBitsBox.currentData()
        self.m_currentSet.parity = self.m_ui.parityBox.currentData()
        self.m_currentSet.stop_bits = self.m_ui.stopBitsBox.currentData()
        self.m_currentSet.flow_control = self.m_ui.flowControlBox.currentData()
  
         