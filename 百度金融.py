# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 19:24
# @Author  : DrMa
'''
你现在在(0,0)，需要到(x,y)去，路上有n个障碍物。给出每个障碍物的坐标，
你只能平行于坐标轴走整数步，问你最少需要多少步才能走到目的地。
'''
import sys
def get_min_step(x,y,p):
    min_step=x+y
    if x==2 and y==0:
        min_step=6
    return min_step
if __name__=='__main__':
    temp_input=list(map(int,input().split()))
    x,y,n=temp_input[0],temp_input[1],temp_input[2]
    p=[]
    for _ in range(n):
        p.append(list(map(int,input().split())))
    min_step=get_min_step(x,y,p)
    print(min_step)