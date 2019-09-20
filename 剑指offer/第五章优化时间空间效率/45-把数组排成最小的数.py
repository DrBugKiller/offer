# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 19:42
# @Author  : DrMa
from functools import cmp_to_key
def cmp_func(x,y):
    '''
    :param x: string
    :param y: string
    :return:
    '''
    if x+y>y+x:
        return 1 #1或者其他大于0的都可
    else:
        return -1 #-1或者其他小于0的都可以
def cmp_func_multi_cols(x,y):#多列排序
    '''
    :param x,y: x,y两个元素都是tuple类型,包括:语文,数学,英语 3个子元素
    :return:
    '''
    if x[0]>y[0]:
        return 1
    elif x[0]<y[0]:
        return -1
    else:
        if x[1]>y[1]:
            return 1
        elif x[1]<y[1]:
            return -1
        else:
            if x[2]>y[2]:
                return 1
            elif x[2]<y[2]:
                return -1
            else:
                return 0
def largestNumber(nums):
    nums=list(map(str,nums))
    print(nums)
    largest_num=sorted(nums,key=cmp_to_key(cmp_func))#sorted默认是升序
    return largest_num

def multi_cols_sort(nums):
    nums_news=sorted(nums,key=cmp_to_key(cmp_func_multi_cols),reverse=True)#我们是降序
    return nums_news
if __name__=='__main__':
    #7个同学的成绩, 顺序分别是语文,数学,英语
    scores=[(98, 100, 88), (97, 86, 93), (90, 88, 99), (88, 94, 76), (90, 89, 90), (88, 94, 77), (99, 84, 60)]
    new_sorted_scores=multi_cols_sort(scores)
    print(scores)
    print('---------------------------------------------------------------------------------------------------')
    print(new_sorted_scores)