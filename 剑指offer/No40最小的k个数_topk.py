# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 21:58
# @Author  : DrMa
'''
题目: 输入n个整数, 找出其中最小的k个数. 例如, 输入4,5,1,6,2,7,3,8这个8个数字,
则最小的4个数字是1,2,3,4

'''
#时间复杂度为O(n),只有当我们可以修改输入的数组时可用,快排中的二分法:
def partition(a,low,high):
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

a=[4,5,1,6,2,7,3,8]
k=4
index=partition(a,0,len(a)-1)
while index!=k-1:
    if index>k-1:
        index=partition(a,0,index-1)
    if index<k-1:
        index=partition(a,index+1,len(a)-1)
print(a[:k])