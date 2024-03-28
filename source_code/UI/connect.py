import sys
import json
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QPushButton
from PyQt5.QtSerialPort import QSerialPort ,QSerialPortInfo
from ui.ui_connect import Ui_Form



class Connect(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Form()
        self.m_ui.setupUi(self) 
        self.full_port_info()   #初始化端口，可以扫描端口号



        self.m_ui.firstButton.clicked.connect(self.first)   #点击确定按钮
        
        self.m_ui.secondButton.clicked.connect(self.second) #secondButton
        self.m_ui.thirdButton.clicked.connect(self.third)   #thirdButton
        self.m_ui.fileButton.clicked.connect(self.open_file_dialog) #点击上传文件按钮


    def first(self):
        print("点击了确认按钮！")

    def second(self):
        print("点击了初始化按钮！")

    def third(self):
        print("点击了确认按钮!！")

    def full_port_info(self):
        self.m_ui.chipBox.addItem("国产1")
        self.m_ui.chipBox.addItem("国产2")
        self.m_ui.chipBox.addItem("国产3")
        self.m_ui.serialconnectBox.clear()
        for info in QSerialPortInfo.availablePorts():
            self.m_ui.serialconnectBox.addItem(info.portName())


    def open_file_dialog(self):     #上传文件
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if filename:
            print(f"Selected file: {filename}")


  
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    window = Connect()
    window.show()
    app.exec_()
 
 


         

  
         