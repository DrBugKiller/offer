# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 21:33
# @Author  : DrMa
'''
题目: 堆排序
思路:
感谢B站up主的详解,有几个key point需要注意:
1. 如何用list表示完全二叉树?
2. 建堆的过程是?
3. 建堆完毕如何再排序?
'''

def heapify(a,n,index):
    # n denotes the length of a
    #Noth that heapify has a precondition that the left and right subtree are heaps!
    if index>=n:
        return
    max_index=index
    l_c_index=2*index+1 #l_c denotes left children
    r_c_index=2*index+2 #r_c denotes right children
    if  l_c_index<n and a[l_c_index]>a[max_index]:#
        max_index=l_c_index
    if  r_c_index<n and a[max_index]<a[r_c_index]:#
        max_index=r_c_index
    # not a[max_index] id the max num in a[index],a[l_c],a[r_c]
    if max_index!=index:
        a[max_index],a[index]=a[index],a[max_index]
        heapify(a,n,max_index)

def build_max_heap(a):
    # (n-1)//2 denotes heapify starts from the second lowest layer
    for index in range((len(a)-1-1)//2,-1,-1):
        heapify(a,len(a),index)
    return a
def heap_sort(a):
    a=build_max_heap(a)
    for i in range(len(a)-1,-1,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)
    return a

if __name__=='__main__':
    a=[1,3,7,4,2,5,3]
    heap_sort(a)
    print(a)