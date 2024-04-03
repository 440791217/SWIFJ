import os
import json
from PyQt5.QtWidgets import QDialog,QCheckBox
from ui.ui_faultmode import Ui_Mode
from loguru import logger
from source_code.script.utils import utils



class Mode(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.m_ui = Ui_Mode()
        self.m_ui.setupUi(self) 
        self.m_ui.checkboxes = []
        self.m_ui.names_values = []

        # values = ['cs', 'es', 'ds', 'eax', 'ebp', 'ebx', 'ecx', 'edi', 'edx', 'esp', 'eip', 'esi', 'fs', 'eflags', 'gs', 'ss']
        # for i in range(16):
        #     checkbox = QCheckBox(f'{values[i]}Button')
        #     checkbox.setChecked(False)
        checkbox_buttons = [
            self.m_ui.csButton, self.m_ui.esButton, self.m_ui.dsButton,
            self.m_ui.eaxButton, self.m_ui.ebpButton, self.m_ui.ebxButton,
            self.m_ui.ecxButton, self.m_ui.ediButton, self.m_ui.edxButton,
            self.m_ui.espButton, self.m_ui.eipButton, self.m_ui.esiButton,
            self.m_ui.fsButton, self.m_ui.eflagsButton, self.m_ui.gsButton,
            self.m_ui.ssButton
        ]
        for checkbox_button in checkbox_buttons:
            checkbox_button.stateChanged.connect(self.checkbox_changed)
            self.m_ui.checkboxes.append(checkbox_button)

        self.checkModeParameter()

        self.m_ui.selectAllBox.clicked.connect(self.selectAllBox)   #点击全选
        self.m_ui.deselectAllBox.clicked.connect(self.deselectAllBox) #点击全不选
        self.m_ui.saveSelection.clicked.connect(self.saveSelection)   #点击保存按钮

    def checkbox_changed(self, state):
        checkbox = self.sender()
        if state == 2:  # Checked
            logger.debug(f'{checkbox.text()} checked')
        else:  # Unchecked
           logger.debug(f'{checkbox.text()} unchecked')

    def selectAllBox(self):
        logger.debug("click selectAllBox Button!")
        checkbox_buttons = [
            self.m_ui.csButton, self.m_ui.esButton, self.m_ui.dsButton,
            self.m_ui.eaxButton, self.m_ui.ebpButton, self.m_ui.ebxButton,
            self.m_ui.ecxButton, self.m_ui.ediButton, self.m_ui.edxButton,
            self.m_ui.espButton, self.m_ui.eipButton, self.m_ui.esiButton,
            self.m_ui.fsButton, self.m_ui.eflagsButton, self.m_ui.gsButton,
            self.m_ui.ssButton
        ]
        for checkbox_button in checkbox_buttons:
            checkbox_button.setChecked(True)

    def deselectAllBox(self):
        logger.debug("click deselectAllBox Button!")
        checkbox_buttons = [
            self.m_ui.csButton, self.m_ui.esButton, self.m_ui.dsButton,
            self.m_ui.eaxButton, self.m_ui.ebpButton, self.m_ui.ebxButton,
            self.m_ui.ecxButton, self.m_ui.ediButton, self.m_ui.edxButton,
            self.m_ui.espButton, self.m_ui.eipButton, self.m_ui.esiButton,
            self.m_ui.fsButton, self.m_ui.eflagsButton, self.m_ui.gsButton,
            self.m_ui.ssButton
        ]
        for checkbox_button in checkbox_buttons:
            checkbox_button.setChecked(False)

    def saveSelection(self):
        logger.debug("click saveSelection Button!")
        arch_values = []
        for checkbox in self.m_ui.checkboxes:
            if checkbox.isChecked():
                arch_values.append({"name": checkbox.text()})

        file_path=utils.get_dir_path('config')
        file_path=os.path.join(file_path,'arch.json')
        data={
            'arch':arch_values
        }    
        utils.save_to_json(data,file_path)
        self.hide()

    def checkModeParameter(self):
        checkbox = []
        uart_file=utils.get_dir_path('config')
        file_arch=os.path.join(uart_file,'arch.json')
        if os.path.exists(file_arch):
            logger.debug('文件存在')
            with open(file_arch, 'rb') as f:
                value = json.load(f)
            crc32_value = value['crc']
            data = value['data']
            value_crc = utils.crc32_of_string(data)
            logger.debug('value_crc',value_crc)
            if crc32_value == value_crc:
                logger.debug('crc校验值相等')
                if len(data['arch']) == 0:
                    logger.debug('全不选')
                    self.deselectAllBox()
                elif len(data['arch']) == 16:
                    logger.debug('全选')
                    self.selectAllBox()
                else:
                    for item in data['arch']:  
                        checkbox.append(item['name'])
                        # name = item['name']
                        # self.m_ui.name.setChecked(True)

                    print("checkbox=",checkbox)
  
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    window = Mode()
    window.show()
    app.exec_()
 
 


         

  
         