# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 20:40
# @Author  : DrMa
n=3
m=10
w=[2,5,3]
v=[2,1,3]

def get_max_num(w,v,m):
    res=0
    remain_m=m
    while remain_m>0:
        min_num=min(w)
        if min_num>0:
            res+=min_num
            w=[x-min_num for x in w]
        zero_index=[]
        #找剩余为0的冰激凌
        for x in range(len(w)):
            if w[x]==0:
                zero_index.append(x)
        need_money=0
        for x in zero_index:
            need_money+=v[x]
        if need_money>remain_m:
            break
        else:
            res+=1
            remain_m-=need_money
            w=[x-1 if x!=0 else x for x in w]
    return res
print(get_max_num(w,v,m))