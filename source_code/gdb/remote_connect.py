import subprocess
import os
import time
import socket
from loguru import logger
from source_code.script.utils import utils

def run_remote_connect(**args):
    tmp_dir=utils.get_dir_path('tmp')
    tmp_file=os.path.join(tmp_dir,'remote_connect.txt')
    bin_dir=utils.get_dir_path('bin')
    bin='bmMon.exe'
    remote_bin=os.path.join(bin_dir,bin)
    com='com3'
    # with open(tmp_file,'w') as f:
        # process = subprocess.Popen([remote_bin,'-leon2','-uart', 'com3','-gdb'], stdin=subprocess.PIPE, stdout=f, text=True)
    process = subprocess.Popen([remote_bin,'-leon2','-uart', 'com3','-gdb'], shell=True)
    # subprocess.run([remote_bin,'-leon2','-uart',com,'-gdb'], shell=True)
    # while process.poll() is None:
    #     print("子进程正在运行...")
    #     time.sleep(5)
    # # 子进程已结束
    print("子进程已结束，退出码:", process.poll())
    # process.communicate()
    return process

def main():
    utils.set_process_name('sudu_remote_connect')
    run_remote_connect()


if __name__=='__main__':
    main()