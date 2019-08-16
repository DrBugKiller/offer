# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 20:32
# @Author  : DrMa
n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
# n,m=2,2
# a=[[2,1],[1,1]]

sum=0
for i in range(m):
    max_lie=max([x[i] for x in a])
    sum+=max_lie
sum*=2

sum_hang=0
for i in range(n):
    max_hang=max(a[i])
    sum_hang+=max_hang
sum_hang*=2

sum_shang=0
for i in range(n):
    for j in range(m):
        if a[i][j]!=0:
            sum_shang+=1
sum_shang*=2

final_sum=sum+sum_hang+sum_shang
print(final_sum)