# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 19:52
# @Author  : DrMa
#2019.7.18
def bubble_sort(a):
    #冒泡排序
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
#2019.7.18
def select_sort(a):
    #选择排序
    for i in range(len(a)-1):
        max_index=i
        for j in range(i+1,len(a)):
            if a[max_index]<a[j]:
                max_index=j
        a[i],a[max_index]=a[max_index],a[i]
    return a
#2019.7.19

def QuickSort(list,low,high):
    if high > low:
         #传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list,low,high)
         #递归排序列表k下标左侧的列表
        QuickSort(list,low,k-1)
         # 递归排序列表k下标右侧的列表
        QuickSort(list,k+1,high)
def Partitions(list,low,high):
     l_index = low+1
     r_index = high
     #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
     while l_index < r_index :
         #因为把list[low]的值给pivot, 所以先从右边找比pivot小的, 在后期进行调换
         while list[r_index] >= list[low] and l_index<r_index:
             r_index-=1
         #从左边开始找比pivot大的.因为l_index是list[low]本身开始,所以有个等于号
         while list[l_index] < list[low] and l_index<r_index:
            l_index+=1
         #若移动完，二者仍未相遇则交换下标对应的值
         if l_index < r_index:
             list[l_index],list[r_index] = list[r_index],list[l_index]
    #若移动完，已经相遇，则交换right对应的值和参考值
     list[low],list[r_index] = list[r_index],list[low]
     #返回index值
     return r_index

#2019.7.20
def insert_sort(a):
    for i in range(1,len(a)):
        insert_index=i
        while a[i]>a[insert_index-1]:
            insert_index-=1
        a.insert(insert_index,a[i])
        del a[i+1]
    return a
#2019.7.20

if __name__=='__main__':
    # a,b=[1,2,3,4],[]
    # print(insert_sort(a))
    a=[5,1,7,5,4]
    print(Partitions(a,0,len(a)-1))
    print(a)
