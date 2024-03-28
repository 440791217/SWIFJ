import yaml
import os
from loguru import logger
from source_code.gdb import cmdline

class Application:
    uart={
        'name':{
            'val':'串口',
            'des':'串口配置',
            'name':'串口'
        },
        'com':{
            'val':'1',
            'des':'端口号，默认值为1',
            'name':'端口号'
        },
        'baudRate':{
            'val':'115200',
            'des':'波特率',
            'name':'波特率'
        },
        'dataBits':{
            'val':'8',
            'des':'数据宽度',
            'name':'数据位宽',            
        },
        'Parity':{
            'val':'none',
            'des':'奇偶校验',
            'name':'奇偶校验'       
        },
        'stopBits':{
            'val':'1',
            'des':'停止位宽度',
            'name':'停止位宽度'            
        },
        'flowControl':{
            'val':'none',
            'des':'流控制',
            'name':'流控制'            
        },
    }
    inj_params={
        'name':{
            'val':'故障注入参数',
            'des':'故障注入配置',
            'name':'故障注入配置'            
        },
        'exe_times':{
            'val':1000,
            'des':'故障注入执行次数，整型',
            'name':'执行次数'            
        },
        'mode':{
            'val':0,
            'des':'模式，0表示寄存器模式，1表示内存模式',
            'name':'模式'            
        },
        'er':{
            'val':0.0001,
            'des':'错误率，用于内存注错，小数表示，1表示对所有内存注错。注错单元数量等于内存总的字节数乘以错误率',
            'name':'错误率'            
        },
        'bfm':{
            'val':1,
            'des':'位翻转类型，1表示单位翻转，2表示双位翻转',
             'name':'位翻转模型'           
        },
        'mem_start':{
            'val':0x0,
            'des':'内存的起始地址',
             'name':'内存起始地址'           
        },
        'mem_size':{
            'val':0x0,
            'des':'内存的长度，单位字节',
            'name':'内存空间尺寸'            
        }
    }

    def __init__(self):
        self.init_yaml()
        # logger.debug('application')

    def init_yaml(self):
        sysfile=os.path.join(os.getcwd(),'config','sys.yaml')
        logger.debug(sysfile)
        if not os.path.exists(sysfile):
            with open(sysfile,'w',encoding='utf-8') as f:

                yaml.dump_all(documents=[self.uart,self.inj_params], stream=f, allow_unicode=True)
                # yaml.safe_dump(data, sysfile)

if __name__=='__main__':
    # print(os.environ['PYTHONPATH'])
    Application()