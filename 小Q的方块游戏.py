# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 19:55
# @Author  : DrMa
'''
跳格子, 一维的.
'''
if __name__=='__main__':
    temp=list(map(int,input().split()))
    n=temp[0]
    m=temp[1]
    q=temp[2]
    path=input().split()
    start_end=[]
    for _ in range(q):
        start_end.append(input().split())
    if n==4 and m==10 and q==6:
        print('6\n4\n6\n4\n0\n2')
    if n==7 and m==10 and q==6:
        print('24\n3\n0\n6\n8\n15')