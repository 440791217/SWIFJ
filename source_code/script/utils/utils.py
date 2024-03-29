import binascii
import zlib
import os
import platform
import json
 
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




def crc32(data):
    return binascii.crc32(data) & 0xffffffff

def get_config_path():
    f=os.path.join(get_home_path(),'config')
    if not os.path.exists(f):
        os.mkdir(f)  
    return f
# def getCWD():
    # return 

#crc字符串校验
def crc32_of_string(data):
    return zlib.crc32(json.dumps(data).encode('utf-8'))

#保存串口数据和crc校验值文件
def save_to_json(self, file_path):
    file_path = get_config_path()
    file_path = os.path.join(file_path,'uart.json')
    data = self.to_dict()
    crc_value = crc32_of_string(data)
    with open(file_path, 'w') as f:
        objdata={
            "uart":data,
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
    # print(desktop_path)
    # checksum = crc32(data)
    # print(f"CRC-32: {checksum:#010x}")

