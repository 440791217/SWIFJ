import subprocess
import time
import os
from loguru import logger
from source_code.script.utils import utils



tmp_file='F:\sudu\SWIFJ\debug'
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
def test_run_gdb():
    # 示例GDB命令列表
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

# def open_gdb():
#     retries=0
#     with open(os.path.join(tmp_file,'tmp.txt'),'w') as f:
#         process = subprocess.Popen(['gdb',os.path.join('F:\sudu\SWIFJ\source_code\gdb','debug','hello.exe')], stdin=subprocess.PIPE, stdout=f, text=True)
#     while True:
#         time.sleep(0.1)
#         retries+=1
#         with open(os.path.join(tmp_file,'tmp.txt'),'r') as f:
#             lines=f.readlines()
#         logger.debug(lines[-1],retries)
#         if len(lines)>0 and '(gdb)' in lines[-1]:
#             return process
#         elif retries>10:
#             break
#     return False

def open_gdb():
    executable=os.path.join('F:\sudu\SWIFJ\source_code\script\gdb','debug','hello.exe')
    process = subprocess.Popen(['gdb',executable], stdin=subprocess.PIPE,stdout=subprocess.PIPE, text=True)
    return process

def run_connect_target(process):
    return

def run_command(process,commands):
    for command in commands:
        process.stdin.write(f'{command}\n')   
        if command=='interrupt':
            time.sleep(1)
    # 等待GDB进程结束并获取输出
    output, _ = process.communicate() 
    print(output)
    return

def run_remote_connect(**args):
    tmp_dir=utils.get_dir_path('tmp')
    tmp_file=os.path.join(tmp_dir,'remote_connect.txt')
    bin_dir=utils.get_dir_path('bin')
    bin='bmMon.exe'
    remote_bin=os.path.join(bin_dir,bin)
    com='com3'
    # with open(tmp_file,'w') as f:
        # process = subprocess.Popen([remote_bin,'-leon2','-uart', 'com3','-gdb'], stdin=subprocess.PIPE, stdout=f, text=True)
    process = subprocess.Popen([remote_bin,'-leon2','-uart', com,'-gdb'], shell=True)
    # subprocess.run([remote_bin,'-leon2','-uart',com,'-gdb'], shell=True)
    # while process.poll() is None:
    #     print("子进程正在运行...")
    #     time.sleep(5)
    # # 子进程已结束
    # print("子进程已结束，退出码:", process.poll())
    # process.communicate()
    return process


def main():
    # remote_process=run_remote_connect()
    gdb_process=open_gdb()
    # run_connect_target(gdb_process)
    run_command(gdb_process,gdb_commands)
    while gdb_process.poll() is None:
        # print("子进程正在运行...")
        time.sleep(5)




if __name__=='__main__':
    main()
    # run_remote_connect()
    
    # print(os.getcwd().rfind('SWIFJ'))
    # print(os.path.abspath(__file__))
    # exit(0)
    # 运行GDB并获取输出
    # gdb_output = test_run_gdb()
    # print(gdb_output)