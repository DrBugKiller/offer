# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 19:34
# @Author  : DrMa
'''
题目: 二分法完成快排
注意点:
<=号或>=号的位置一定是与pivot相同的一侧. 为的是0,2,1这类,a[0]=0本来就是在目标位置的.
left_index须从low开始,而不能从low+1,目的也是防止0,2,1这类,a[0]=0本来就是在目标位置.
'''
def quick_sort(a,low,high):
    if low<high:
        pivot=partition(a,low,high)
        quick_sort(a,low,pivot-1)
        quick_sort(a,pivot+1,high)
def partition(a,low,high):
    pivot=a[low]
    l_index=low #l_index denotes left_index, 而且必须从low开始而不能low+1
    r_index=high #r_index denotes right_index
    while l_index<r_index:
        while l_index<r_index and a[r_index]<pivot:
            r_index-=1
        while l_index<r_index and a[l_index]>=pivot:#<=或>=只能在这一侧,和pivot用一侧.
            l_index+=1
        if l_index<r_index:
            a[l_index],a[r_index]=a[r_index],a[l_index]
    a[low],a[r_index]=a[r_index],a[low]
    return r_index

if __name__=='__main__':
    a=[5,1,9,3,7,4]
    quick_sort(a,0, len(a)-1 )
    print(a)