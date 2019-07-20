# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 8:14
# @Author  : DrMa
'''
题目39:
数组中有一个数字出现的次数超过数组长度的一半,请找出这个数字.
思路:
1. 超过一半, 说明该数字的次数大于其他数字的和. 我们用两个变量保存该数字,另一个保存次数,
遍历数组,遇到相同的次数加1, 遇到不同的次数减1,如果次数到零了,那肯定不是目标的数,更新当前最大数,并把次数再次设置为1.
2. 另一种思路就是有个推理,数组的中位数肯定是目标数
'''
def solution(a):
    max_num=a[0]
    num_of_mn=1
    for i in range(1,len(a)):
        if a[i]==max_num:
            num_of_mn+=1
        else:
            num_of_mn-=1
            if num_of_mn==0:
                max_num=a[i]
                num_of_mn=1
    return max_num

'''
题目: 输入n个整数, 找出其中最小的k个数. 例如, 输入4,5,1,6,2,7,3,8这个8个数字,
则最小的4个数字是1,2,3,4
'''
def Partition(a,low,high):
    l_index=low+1
    r_index=high
    while l_index<r_index:
        while a[r_index]>=a[low] and l_index<r_index:
            r_index-=1
        while a[l_index]<a[low] and l_index<r_index:
            l_index+=1
        if l_index<r_index:
            a[l_index],a[r_index]=a[r_index],a[l_index]
    a[low],a[r_index]=a[r_index],a[low]
    return r_index
def topk(a,k):
    index=Partition(a,0,len(a)-1)
    while index!=k-1:
        if index>k-1:
            index=Partition(a,0,index-1)
        if index<k-1:
            index=Partition(a,index+1,len(a)-1)
    return a[:k]
test_arr=[4,5,1,6,2,7,3,8,4,10,5,0]
print(topk(test_arr,4))