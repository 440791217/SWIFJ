import subprocess
import time
import os
from loguru import logger
from source_code.script.utils import utils



tmp_file='F:\sudu\SWIFJ\debug'
def test_run_gdb():
    # 示例GDB命令列表
    gdb_commands = [
        'break main',
        'run',
        # 'source gdb/printf.py',
        'info registers',
        # 'continue',
        'interrupt', 
        'set $cs=0xff',
        'info registers',
        # 'info registers',
        'continue',
        'quit'
    ]
    # 使用subprocess.Popen来运行GDB命令
    process = subprocess.Popen(['gdb',os.path.join(os.getcwd(),'debug','hello.exe')], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    # 发送GDB命令到gdb进程的标准输入
    for command in gdb_commands:
        process.stdin.write(f'{command}\n')   
        if command=='interrupt':
            time.sleep(1)
    # 等待GDB进程结束并获取输出
    output, _ = process.communicate()
    return output

def open_gdb():
    retries=0
    with open(os.path.join(tmp_file,'tmp.txt'),'w') as f:
        process = subprocess.Popen(['gdb',os.path.join('F:\sudu\SWIFJ\source_code\gdb','debug','hello.exe')], stdin=subprocess.PIPE, stdout=f, text=True)
    while True:
        time.sleep(0.1)
        retries+=1
        with open(os.path.join(tmp_file,'tmp.txt'),'r') as f:
            lines=f.readlines()
        logger.debug(lines[-1],retries)
        if len(lines)>0 and '(gdb)' in lines[-1]:
            return process
        elif retries>10:
            break
    return False





if __name__=='__main__':
    # run_remote_connect()
    
    # print(os.getcwd().rfind('SWIFJ'))
    # print(os.path.abspath(__file__))
    # exit(0)
    # 运行GDB并获取输出
    gdb_output = test_run_gdb()
    print(gdb_output)