# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 20:36
# @Author  : DrMa
def solution(n,s,value):
    min_num=9999
    for i in range(n-1):
        cur_sum=value[i]
        j=i+1
        while j<n:
            cur_sum+=value[j]
            if cur_sum>=s:
                break
            j+=1
        cur_num=j-i+1
        if min_num>cur_num:
            min_num=cur_num
    return min_num
if __name__=='__main__':
    temp=list(map(int,input().split()))
    n=temp[0]
    s=temp[1]
    value=list(map(int,input().split()))
    print(solution(n,s,value))