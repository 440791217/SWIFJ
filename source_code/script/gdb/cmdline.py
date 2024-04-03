import re
import sys
import random
import time
import threading
import logging
from source_code.script.gdb.register import *

logging.basicConfig(filename='F://sudu//SWIFJ//source_code//script//gdb//debug//gdb_log.log', level=logging.INFO)


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

def logfle(**args):
    cmd='set logging on'
    result=run(cmd=cmd)
    cmd='set logging file F://sudu//SWIFJ//source_code//script//gdb//debug//gdb_log.txt'
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
    print('start')
    result=run(cmd=cmd)
    print('start results',result)
    return result

def halt(**args):
    if 'timeout' in args:
        timeout=args['timeout']
    else:
        timeout=0
    cmd='{}'.format('interrupt')
    # cmd='{}'.format('signal SIGSTOP')
    print('halt timeout',timeout)
    time.sleep(timeout)
    result=run(cmd=cmd)
    print('halt results',result)
    return result

def resume(**args):
    print('resume')
    cmd='{}'.format('continue')
    result=run(cmd=cmd)
    print('resume result',result)
    return result

def dummy(**args):
    if 'timeout' in args:
        timeout=args['timeout']
    else:
        timeout=0
    time.sleep(timeout)
    print('dummy')

def post_task(task):
    gdb.post_event(task)
    

def main():
    inj_times=1000
    exe_timeout=5
    ##初始化，关闭干扰操作
    confirm()
    verbose()
    pagination()
    # run(cmd='set scheduler-locking on')
    # logfle()
    # gdb.post_event(start)
    # print('tm')
    # th1 = threading.Thread(target=main_th)
    # th1.start()
    # gdb.write('start\n')

    for i in range(inj_times):
        # ##设置随机定时器
        timeout=random.random()*exe_timeout
        isr=lambda:halt(timeout=timeout)
        th1 = threading.Thread(target=isr)
        th1.start()
        # gdb.post_event(isr)
        start()
        isr=lambda:halt(timeout=1)
        th1 = threading.Thread(target=isr)
        th1.start()
        resume()
        isr=lambda:halt(timeout=1)
        th1 = threading.Thread(target=isr)
        th1.start()
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

