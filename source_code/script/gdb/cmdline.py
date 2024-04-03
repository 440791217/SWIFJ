import re
import sys
import random
import time
import threading
from source_code.script.gdb.register import *



INFO_REGISTER='info register'
VOID='void'
PRINT='print'
SET='set'


def run(**args):
    cmd=args['cmd']
    if 'to_string' in args.keys():
        to_string=args['to_string']
    else:
        to_string=True
    # result=gdb.execute(cmd,to_string=to_string)
    result=gdb.execute(cmd)
    return result

def pagination(**args):
    cmd='set pagination off'
    result=run(cmd=cmd)
    return result

def verbose(**args):
    cmd='set verbose on'
    result=run(cmd=cmd)
    return result

def confirm(**args):
    cmd='set confirm off'
    result=run(cmd=cmd)
    return result 


def get(**args):
    name=args['name']
    cmd='{} {}'.format(PRINT,name)
    result=run(cmd=cmd)
    # print(result)
    if VOID in result:
        value=VOID
    else:
        result=result.split('=')
        value=result[1].strip()
    return value

def set(**args):
    name=args['name']
    value=args['value']
    cmd='{} {}={}'.format(SET,name,value)
    run(cmd=cmd)

def bit_flip(**args):
    value=args['value']
    value=int(value)
    width=args['width']
    b= bin(value)[2:]
    b=b.zfill(width)
    p=random.randint(0,width-1)
    b1=[]
    bf=-1
    for i in range(width):
        v=b[i]
        if i==p:
            if v=='1':
                bf='0'
            else:
                bf='1'
            v=bf
        b1.append(v)
    b1=''.join(b1)
    b1=int(b1, 2)
    # print(b1)
    value=hex(value)
    b1=hex(b1)
    result={
        'dirty_value':b1,
        'value':value,
        'position':p,
        'bf':bf,
    }
    return result

# def load(**args):
#     exe_path="F://sudu//SWIFJ//source_code//script//gdb//debug//hello.exe"    
#     cmd='{} {}'.format(FILE,exe_path)
#     # print(cmd)
#     result=run(cmd=cmd,to_string=True)
#     print(result)
#     return
def start(**args):
    cmd='{}'.format('r')
    result=run(cmd=cmd)
    print('start',result)
    print('213123')
    return result

def halt(**args):
    time.sleep(5)
    cmd='{}'.format('interrupt')
    result=run(cmd=cmd)
    print('halt',result)
    return result

def resume(**args):
    cmd='{}'.format('continue')
    result=run(cmd=cmd)
    print('resume',result)
    return result


def main():
    confirm()
    verbose()
    pagination()

##设置随机定时器
    timeout=random.uniform(0, 1)*5
    gdb.post_event(halt)
    start()
    gdb.post_event(halt)
    resume()
    return 0

# 定义一个函数，用于作为线程的执行体
def interrupter(seconds):
    time.sleep(2)
    gdb.post_event(halt)



class Registers:
    def __init__(self):
        pass
    @staticmethod
    def fetch_register_list(*match_groups):
        registers=[]
        for line in run(cmd='maintenance print register-groups').split('\n'):
            fields = line.split()
            # print(fields)
            if len(fields) != 7:
                continue
            name, _, _, _, width, _, groups = fields
            if not re.match(r'\w', name):
                continue
            for group in groups.split(','):
                if group in (match_groups or ('general',)):
                    # print(name,width)
                    registers.append({
                        'name':name,
                        'width':int(width)*8
                    })
                    break
        # logger.debug(names)
        print(registers)
        return registers
    
    @staticmethod
    def inject_fault(**args):
        register_info=get_resgiter_info(arch=TEST_ARCH)
    
    # @staticmethod
    # def get_register(**args):
    #     name=args['name']
    #     try:
    #         # 通过 parse_and_eval 函数获取寄存器对象
    #         value=gdb.parameter(name)
    #         # 设置寄存器的值
    #         # register.assign_value(value)
    #     except gdb.error as e:
    #         print("Error setting register value: {}".format(e))    
    #     print(register)    
    #     return

    # @staticmethod
    # def set_register(**args):
    #     name=args['name']
    #     value=args['value']
    #     try:
    #         # 通过 parse_and_eval 函数获取寄存器对象
    #         register = gdb.parse_and_eval(name)
    #         # 设置寄存器的值
    #         register.assign_value(value)
    #     except gdb.error as e:
    #         print("Error setting register value: {}".format(e))    
    #     print(register)    
    #     return    



if __name__=='__main__':
    main()

