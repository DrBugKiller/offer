# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 19:44
# @Author  : DrMa
'''
题目：一个长度为n的数列，有序（从小到大）
我们想查找一个数x是否在这个数列当中？
思路：二分查找，每次去中间位置的数m，如果目标数n小于m,我们再对左半部分进行查找（递归）。
如果目标数n大于m，我们对右半部分进行查找（递归）
'''
def merge_search(array,item):
    if not array:
        return False
    mid_index=len(array)//2
    if array[mid_index]==item:
        return True
    elif item<array[mid_index]:
        return merge_search(array[:mid_index],item)#不要忘了return，否则会返回None
    else:
        return merge_search(array[mid_index+1:],item)

if __name__ =='__main__':
    a=[1,2,3,4,5,6,7,9]
    item=10
    b=merge_search(a,item)
    print(b)