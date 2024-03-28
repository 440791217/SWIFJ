import binascii
 
def crc32(data):
    return binascii.crc32(data) & 0xffffffff

def get_config_path():
    return ''

# def getCWD():
    # return 

 


if __name__=='__main__':
    # 测试CRC
    data = b"Hello, World!"
    print(data)
    data1 = "Hello, World!".encode('utf-8')
    print(data1)
    # checksum = crc32(data)
    # print(f"CRC-32: {checksum:#010x}")
