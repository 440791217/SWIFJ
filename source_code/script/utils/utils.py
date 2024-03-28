import binascii
import zlib
import os
import platform
 
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

def calculate_crc32(file_path):
    # 打开文件并计算 CRC32 校验值
    with open(file_path, 'rb') as file:
        crc_value = 0
        while True:
            data = file.read(1024)  # 读取文件数据块
            if not data:
                break
            crc_value = zlib.crc32(data, crc_value)  # 计算 CRC32 校验值
    return crc_value
 


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

