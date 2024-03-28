import binascii
import zlib
 
def crc32(data):
    return binascii.crc32(data) & 0xffffffff

def get_config_path():
    return 'D:\\Project\\Project\\SWIFJ\\config'
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
    # checksum = crc32(data)
    # print(f"CRC-32: {checksum:#010x}")

