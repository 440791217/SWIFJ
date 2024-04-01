import os
import sys
import json
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo
from loguru import logger
from ui.ui_fault_injection import Ui_Fault
from source_code.script.utils import utils


class SettingFault(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Fault()
        self.m_ui.setupUi(self) 
        self.checkParameter_fault()#检查本地是否有串口的配置文件
        self.fill_fault_parameters()
        self.m_ui.ApplyButton.clicked.connect(self.Apply_fault)   #点击确定按钮




    def  Apply_fault(self):
        print("确认提交按钮被点击！")
        file_path=utils.get_dir_path('config')
        file_path=os.path.join(file_path,'inj_params.json')
        inj_params=self.to_dict()
        data={
            'inj_params':inj_params
        }    
        utils.save_to_json(data,file_path)
        self.hide() 
 
    def fill_fault_parameters(self):
        self.m_ui.exe_timesBox.addItem("100")
        self.m_ui.exe_timesBox.addItem("1000")
        self.m_ui.exe_timesBox.addItem("10000")
        self.m_ui.exe_timesBox.addItem("100000")
 
        self.m_ui.modeBox.addItem("0")
        self.m_ui.modeBox.addItem("1")
 
        self.m_ui.erBox.addItem("None")
        self.m_ui.erBox.addItem("Even")
        self.m_ui.erBox.addItem("Space")
 
        self.m_ui.bfmBox.addItem("1")
        self.m_ui.bfmBox.addItem("2")

        self.m_ui.mem_startBox.addItem("None")
        self.m_ui.mem_startBox.addItem("Even")
        self.m_ui.mem_startBox.addItem("Space")

        self.m_ui.mem_sizeBox.addItem("None")
        self.m_ui.mem_sizeBox.addItem("Even")
        self.m_ui.mem_sizeBox.addItem("Space")

    def to_dict(self):
        return {
           'exe_times': self.m_ui.exe_timesBox.currentText(),
           'mode':self.m_ui.modeBox.currentText(),
           'er':self.m_ui.erBox.currentText(),
           'bfm':self.m_ui.bfmBox.currentText(),
           'mem_start':self.m_ui.mem_startBox.currentText(),
           'mem_size':self.m_ui.mem_sizeBox.currentText()
        }
    def checkParameter_fault(self):
        uart_file=utils.get_dir_path('config')
        file_uart=os.path.join(uart_file,'inj_params.json')
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
                self.m_ui.exe_timesBox.addItem(str(data['data']['inj_params']['exe_times']))
                self.m_ui.modeBox.addItem(str(data['data']['inj_params']['mode']))
                self.m_ui.erBox.addItem(str(data['data']['inj_params']['er']))
                self.m_ui.bfmBox.addItem(str(data['data']['inj_params']['bfm']))
                self.m_ui.mem_startBox.addItem(str(data['data']['inj_params']['mem_start']))
                self.m_ui.mem_sizeBox.addItem(str(data['data']['inj_params']['mem_size']))
            else:
                logger.debug('crc校验值不相等')
                # self.fill_ports_parameters() 
        else:
            logger.debug('文件不存在')
            # self.fill_ports_parameters()



   
         

  
         