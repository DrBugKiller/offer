# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 14:58
# @Author  : DrMa
from multiprocessing import Pool
import os,time
def sub_process(n):
    print(n)
    time.sleep(5)
    print(n*2)
    time.sleep(5)
    print('Process (%s) is running!' % os.getpid(),__name__)
#进程主体begin:
print('进程主体,父进程和子进程都能执行')
time.sleep(5)
print(__name__)
#进程主体end
if __name__=='__main__':
    # 指定同时运行的进程数
    print('因为是__main__,只能是父进程执行')
    p = Pool(3)
    for i in range(3):
        p.apply_async(sub_process,args=(i+1,))#apply_async(你所要并行的函数)
    # 不能继续添加进程了
    p.close()
    p.join()


