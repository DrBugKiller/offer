# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 19:52
# @Author  : DrMa

def bubble_sort(a):
    #冒泡排序
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def select_sort(a):
    #选择排序
    for i in range(len(a)-1):
        max_index=i
        for j in range(i+1,len(a)):
            if a[max_index]<a[j]:
                max_index=j
        a[i],a[max_index]=a[max_index],a[i]
    return a

def quick_sort(a):
    #这个函数是个取巧的快排, 只体现二分法的思想, 但是不是正宗的快排
    if a==[]:
        return a
    pivot=a[0]#随机取个开始的,pivot denotes 基准, 快速排序的核心就是对他进行合理的放置,然后左右递归
    left_a=[x for x in a if x>pivot]
    right_a=[x for x in a if x<pivot]
    middle_a=[x for x in a if x==pivot]
    a=quick_sort(left_a)+[middle_a]+quick_sort(right_a)
    return a


def QuickSort(list,low,high):
    if high > low:
         #传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list,low,high)
         #递归排序列表k下标左侧的列表
        QuickSort(list,low,k-1)
         # 递归排序列表k下标右侧的列表
        QuickSort(list,k+1,high)

def Partitions(list,low,high):
     l_index = low
     r_index = high
     #将最左侧的值赋值给参考值pivot
     pivot = list[low]
     #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
     while l_index < r_index :
         #因为把list[low]的值给pivot, 所以先从右边找比pivot小的, 在后期进行调换
         while list[r_index] > pivot and l_index<r_index:
             r_index-=1
         #从左边开始找比pivot大的
         while list[l_index] <= pivot and l_index<r_index:
            l_index+=1
         #若移动完，二者仍未相遇则交换下标对应的值
         if l_index < r_index:
             list[l_index],list[r_index] = list[r_index],list[l_index]
    #若移动完，已经相遇，则交换right对应的值和参考值
     print('left:{0},right:{1}'.format(l_index,r_index))
     list[low],list[r_index] = list[r_index],list[low]

     #返回k值
     return r_index


if __name__=='__main__':
    a,b=[7,2,4,8,5,9,1,9],[]
    QuickSort(a,0,len(a)-1)
    print(a)
    quit()
    print(quick_sort(a))
    print(quick_sort(b))
