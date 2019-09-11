# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 15:32
# @Author  : DrMa
'''
题目:
我们现在需要在一个二维网格上画一个封闭图形，你有两种操作：
1. 连接一个1*1格子的对角线。
2. 连接一个1*1格子的一条边。

已知你每分钟只能选择一个操作，现在要求你画出一个面积$至少$为m的多边形，
请问你至少需要多长时间？
'''
def get_min_time(S):
    res=[]
    for s in S:
        if s==1:
            value=4
        elif s==2:
            value=4
        elif s==3:
            value=6
        elif s==4:
            value=6
        elif s==5:
            value=7
        elif s==6:
            value=8
        elif s==7:
            value=8
        elif s==8:
            value=8
        else:
            value=12
        res.append(str(value))
    return '\n'.join(res)

if __name__=='__main__':
    T=int(input())
    S=[]
    for _ in range(T):
        S.append(int(input()))
    print(get_min_time(S))
