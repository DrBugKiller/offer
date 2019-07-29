# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 12:03
# @Author  : DrMa
'''
题目40-topk的最小数:
输入n个整数, 找出其中最小的k个数. 例如, 输入4,5,1,6,2,7,3,8这个8个数字,
则最小的4个数字是1,2,3,4.
思路:
利用Partiton函数,如果pivot经过Partition之后的index刚好是k-1, 那么index从0~k-1的这k个数就是目标.
如果不是则分为两种情况:
    1. index大于k-1, 说明topk在a[index]的左边, 我们就对[0,index-1]进行Partition
    2. index小于k-1, 说明topk在a[index]的右边, 我们就对[index+1,len(a)-1]进行Partition
'''
def Partition(a,low,high):
    l_index=low
    r_index=high
    while l_index<r_index:
        while a[r_index]>a[low] and l_index<r_index:
            r_index-=1
        while a[l_index]<=a[low] and l_index<r_index:
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