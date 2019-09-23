# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 16:33
# @Author  : DrMa
n=int(input())
res=[]
for i in range(n):
    temp_input=list(map(int,input().split()))
    res.append(temp_input)
for nums in res:

    num_p=len(nums)
    sum=0
    for j in range(len(nums)):
        sum+=nums[j]
    res=sum//num_p
    print(res)