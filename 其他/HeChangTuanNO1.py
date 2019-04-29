# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 20:55
# @Author  : DrMa
import sys
temp_str=sys.stdin.readline().strip()#此处注意readline是会把回车也读进去的，所以需要strip()把回车删掉一下,strip()可以把两边的回车删掉
temp_str2=input()#input是不读取回车的
N=int(temp_str)
while True:
    temp_str = input()
    if temp_str=='':
        break

ai_list=list(map(int,sys.stdin.readline().split()))
K,D=list(map(int,sys.stdin.readline().split()))#这里不加list也行

A=[7,3,7,5,8,3,-10,4]
k,d=[4,5]
# 从N个人中选K个,选中的相邻两个人的编号不超过D
B = [[[0,0] for j in range(N)] for i in range(k + 1)]#快速
print(B)
for k in range(1, k + 1):#最外循环是k个人
    for i in range(N):
        if k==1 or i==0:
            B[k][i][0], B[k][i][1]=A[i],A[i]
        else:
            M=[]
            for t in range(1,d+1):
                if i-t<0:
                    break
                D=B[k-1][i-t]
                M.extend([D[0]*A[i],D[1]*A[i]])
            B[k][i][0],B[k][i][1]=min(M),max(M)
print([B[k][i][1] for i in range(N)])
print([B[k][i][0] for i in range(N)])
