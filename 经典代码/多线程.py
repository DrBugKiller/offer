# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 16:54
# @Author  : DrMa
import threading
import time
import os
def sub_process(n):
    print(n)
    time.sleep(5)
    print(n*2)
    time.sleep(5)
    print('Process (%s) is running!' % os.getpid(),__name__)
print('进程主体,只调用一次')
print(__name__)
if __name__=='__main__':
    threads=[]
    for i in range(3):
        t = threading.Thread(target=sub_process, args=(i+1,))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('wancheng!')

