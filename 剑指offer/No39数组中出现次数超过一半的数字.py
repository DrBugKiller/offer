# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 21:22
# @Author  : DrMa
'''
题目: 数组中有一个数字出现的次数超过数组长度的一半,请找出这个数字.
思路:
1. 超过一半, 说明该数字的次数大于其他数字的和. 我们用两个变量保存该数字,另一个保存次数,
遍历数组,遇到相同的次数加1, 遇到不同的次数减1,如果次数到零了,那肯定不是目标的数.
2.
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

if __name__=='__main__':
    a=[4,4,4,2,2,3,2,2,3,2]
    print(solution(a))