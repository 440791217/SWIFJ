import binascii
import zlib
import os
import platform
import json
from loguru import logger
import multiprocessing


def get_home_path():
    f=''
    if platform.system() == "Windows":
        f= os.path.join(os.environ['USERPROFILE'], '')
    elif platform.system() == "Linux":
        f= os.path.join(os.path.expanduser('~'), '')
    elif platform.system() == "Darwin":
        f= os.path.join(os.path.expanduser('~'), '')
    else:
        raise OSError('Unsupported operating system')
    home=os.path.join(f,'.SWIFJ')
    print(home)
    if not os.path.exists(home):
        os.mkdir(home)   
    return home

def get_dir_path(dir_path):
    f=os.path.join(get_home_path(),dir_path)
    if not os.path.exists(f):
        os.mkdir(f)  
    return f

  
def set_process_name(new_name):  
    # 获取当前进程ID  
    pid = os.getpid()  
    # 设置进程名为新名称  
    multiprocessing.current_process().name = new_name
    
    logger.debug(f"Process name changed to '{new_name}' (PID: {pid})")



def crc32(data):
    return binascii.crc32(data) & 0xffffffff




#crc字符串校验
def crc32_of_string(data):
    return zlib.crc32(json.dumps(data).encode('utf-8'))

#保存串口数据和crc校验值文件
def save_to_json(data, file_path):
    crc_value = crc32_of_string(data)
    with open(file_path, 'w') as f:
        objdata={
            "data":data,
            "crc":crc_value
        }
        json.dump(objdata, f ,indent=4)


if __name__=='__main__':
    # 测试CRC
    data = b"Hello, World!"
    print(data)
    data1 = "Hello, World!".encode('utf-8')
    print(data1)
    desktop_path = get_home_path()
    logger.debug('123123')
    # print(desktop_path)
    # checksum = crc32(data)
    # print(f"CRC-32: {checksum:#010x}")

