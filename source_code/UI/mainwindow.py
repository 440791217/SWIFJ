from PyQt5.QtWidgets import QMainWindow, QMessageBox,QPlainTextEdit
from ui.ui_mainwindow import Ui_MainWindow
from settingdialog import SettingDialog
from fault_injection import SettingFault
from connect import Connect
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice,Qt
 
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
 
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)

        self.m_serial = QSerialPort(self)
        self.m_settings = SettingDialog(self)

        self.m_settingfault = SettingFault(self)#创建一个SettingDialog实例
        self.m_ui.actionFault.triggered.connect(self.m_settingfault.show)

        self.m_settingcon = Connect(self)#创建一个Connect实例
        self.m_ui.actionCon.triggered.connect(self.m_settingcon.show)

        self.m_textEdit = QPlainTextEdit(self) 
        self.setCentralWidget(self.m_textEdit)   
 
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)
        self.m_ui.actionQuit.setEnabled(True)
        self.m_ui.actionConfigure.setEnabled(True)
 
        self.m_ui.actionConfigure.triggered.connect(self.m_settings.show)
        self.m_ui.actionConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionDisconnect.triggered.connect(self.close_serial_port)
        self.m_serial.readyRead.connect(self.read_data)
 
    def open_serial_port(self):
        s = self.m_settings.setting()
        self.m_serial.setPortName(s.name)
        self.m_serial.setBaudRate(s.baud_rate)
        self.m_serial.setParity(s.parity)
        self.m_serial.setDataBits(s.data_bits)
        self.m_serial.setStopBits(s.stop_bits)
        self.m_serial.setFlowControl(s.flow_control)
        try:
            if self.m_serial.open(QIODevice.ReadWrite):
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

