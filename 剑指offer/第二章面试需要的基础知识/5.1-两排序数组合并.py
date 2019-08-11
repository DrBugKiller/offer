# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 22:13
# @Author  : DrMa
'''
题目: 有两个排序的A1和A2, 内存在A1的末尾有足够多的空余空间容纳A2.
请实现一个函数, 把A2中的所有数字插入A1中, 并且所有的数字是排序的.
思路: 从头到尾,有重复,慢
      从尾到头比较A1和A2中的数字,并把较大的数字复制到A1中合适的位置.
'''
def merge_op(a,b):
    a_index = len(a) - 1
    a+=[None]*(len(b))
    a_index_new=len(a)-1
    b_index=len(b)-1
    while a_index_new>=0:#注意条件
        #如果b的元素大,或者是a列表已经没有值了而b还有
        if b[b_index]>=a[a_index] and b_index>=0 or (a_index<0 and b_index>=0):
            a[a_index_new]=b[b_index]
            b_index-=1
            a_index_new-=1
        #如果a的元素大,或者是b列表已经没有了而a还有
        elif a[a_index]>b[b_index] and a_index>=0 or (a_index>=0 and b_index<0):
            a[a_index_new]=a[a_index]
            a_index-=1
            a_index_new-=1
    return a
if __name__=='__main__':
    a=[4,5,6]
    b=[1,2,3]
    print(merge_op(a,b))