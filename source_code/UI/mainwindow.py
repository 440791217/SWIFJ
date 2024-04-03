import json
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox,QPlainTextEdit
from ui.ui_mainwindow import Ui_MainWindow
from settingdialog import SettingDialog
from fault_injection import SettingFault
from connect import Connect
from fault_mode import Mode
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice
from source_code.script.utils import utils
from loguru import logger
 
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
 
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)

        self.m_serial = QSerialPort(self)
        self.m_settings = SettingDialog(self)#创建一个SettingDialog实例，创建串口配置界面

        self.m_settingfault = SettingFault(self)#创建一个SettingFault实例，故障注入参数设置
        self.m_ui.actionFault.triggered.connect(self.m_settingfault.show)

        self.m_settingcon = Connect(self)#创建一个设备连接Connect实例
        self.m_ui.actionCon.triggered.connect(self.m_settingcon.show)

        self.m_settingmode = Mode(self)#创建故障注入模式选择的页面
        self.m_ui.actionMode.triggered.connect(self.m_settingmode.show)

        self.m_ui.actionAbout.triggered.connect(self.on_about)#创建关于按钮

        self.m_textEdit = QPlainTextEdit(self) 
        self.setCentralWidget(self.m_textEdit)   
 
        self.m_ui.actionConnect.setEnabled(True)#启动打开串口状态
        self.m_ui.actionDisconnect.setEnabled(False)#关闭串口状态
        self.m_ui.actionQuit.setEnabled(True)#清除按钮
        self.m_ui.actionConfigure.setEnabled(True)#串口配置按钮状态
 
        self.m_ui.actionConfigure.triggered.connect(self.m_settings.show)
        self.m_ui.actionConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionDisconnect.triggered.connect(self.close_serial_port)
        self.m_serial.readyRead.connect(self.read_data)
 
    def on_about(self):
        QMessageBox.about(self, '关于', '这是一个关于对话框示例')

    def open_serial_port(self):
        uart_file=utils.get_dir_path('config')
        file_uart=os.path.join(uart_file,'uart.json')
        if os.path.exists(file_uart):
            logger.debug('文件存在')
            with open(file_uart, 'rb') as f:
                value = json.load(f)
            crc32_value = value['crc']
            data = value['data']
            value_crc = utils.crc32_of_string(data)
            logger.debug('value_crc',value_crc)
            if crc32_value == value_crc:
                logger.debug('crc校验值相等')
                with open(file_uart, 'r') as file:
                    data = json.load(file)
                self.m_serial.setPortName(str(data['data']['uart']['com']))
                self.m_serial.setBaudRate(int(data['data']['uart']['baud_rate']))
                parity_text  = str(data['data']['uart']['Parity'])
                if parity_text == "None":
                     parity = QSerialPort.NoParity
                elif parity_text == "Even":
                    parity = QSerialPort.EvenParity
                elif parity_text == "Odd":
                    parity = QSerialPort.OddParity
                elif parity_text == "Mark":
                    parity = QSerialPort.MarkParity
                elif parity_text == "Space":
                    parity = QSerialPort.SpaceParity
                else:
                    parity = QSerialPort.NoParity
                self.m_serial.setParity(parity)

                databits_text = str(data['data']['uart']['dataBits'])
                if databits_text == "5":
                    databits = QSerialPort.Data5
                elif databits_text == "6":
                    databits = QSerialPort.Data6
                elif databits_text == "7":
                    databits = QSerialPort.Data7
                elif databits_text == "8":
                    databits = QSerialPort.Data8
                else:
                    databits = QSerialPort.Data8
                self.m_serial.setDataBits(databits)

                stopbits_text = str(data['data']['uart']['stopBits'])
                if stopbits_text == "1":
                    stopbits = QSerialPort.OneStop
                elif stopbits_text == "1.5":
                    stopbits = QSerialPort.OneAndHalfStop
                elif stopbits_text == "2":
                    stopbits = QSerialPort.TwoStop
                else:
                    stopbits = QSerialPort.OneStop
                self.m_serial.setStopBits(stopbits)

                flowcontrol_text = str(data['data']['uart']['flowControl'])
                if flowcontrol_text == "NoFlowControl":
                    flowcontrol = QSerialPort.NoFlowControl
                elif flowcontrol_text == "HardwareControl":
                    flowcontrol = QSerialPort.HardwareControl
                elif flowcontrol_text == "SoftwareControl":
                    flowcontrol = QSerialPort.SoftwareControl
                else:
                    flowcontrol = QSerialPort.NoFlowControl
                self.m_serial.setFlowControl(flowcontrol)
            else:
                logger.debug('crc校验值不相等')
                # self.fill_ports_parameters() 
        else:
            logger.debug('文件不存在')
            # self.fill_ports_parameters()

        try:
            # if self.m_serial.open(QIODevice.ReadWrite):
            if self.m_serial.open(QSerialPort.ReadWrite):
                self.m_ui.actionConnect.setEnabled(False)
                self.m_ui.actionDisconnect.setEnabled(True)
                self.m_ui.actionConfigure.setEnabled(False)
                print("open success")
            else:
                QMessageBox.critical(self, "Error", self.m_serial.errorString())
                self.show_status_message("Open error")
                print("open failed")
        except:
            print("can not open this serial")
 
    def close_serial_port(self):
        print("close_serial_port")
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)
        self.m_ui.actionConfigure.setEnabled(True)

    def read_data(self):
        data = self.m_serial.readAll().data().decode("utf8")
        self.m_textEdit.insertPlainText(data)
        bar = self.m_textEdit.verticalScrollBar()
        bar.setValue(bar.maximum())

