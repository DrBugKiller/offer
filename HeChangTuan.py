# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 21:05
# @Author  : DrMa
import itertools
num_student=int(input())
power_list=input().split()
power_list=list(map(lambda x:int(x),power_list))
k_d=input()
k=int(k_d.split()[0])
d=int(k_d.split()[1])
index_list=list(itertools.combinations(range(num_student),k))
multi_max=0
for index in index_list:#index是不放回组合
    multi=1
    bool=True
    for j in range(k-1):
        if (index[j]+d)<index[j+1]:
            bool=False
    if bool==False:
        continue
    for j in range(k):
        multi=multi*power_list[index[j]]
    if multi>multi_max:
        multi_max=multi
print(multi_max)