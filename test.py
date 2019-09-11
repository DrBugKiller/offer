# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 20:16
# @Author  : DrMa
n,k=list(map(int,input().split()))
h=list(map(int,input().split()))
def get_sum(h):
    sum=0
    for i in h:
        sum+=i
    return sum
def get_min_index(n,k,h):
    start=0
    end=n-k
    index=0
    sum=1000000
    for i in range(start,end):
        sum_new=get_sum(h[i:i+k])
        if sum_new<sum:
            sum=sum_new
            index=i
    return str(index+1)
print(get_min_index(n,k,h))