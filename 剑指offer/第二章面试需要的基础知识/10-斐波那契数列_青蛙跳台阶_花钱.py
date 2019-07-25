# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:50
# @Author  : DrMa
'''
题目10-斐波那契数列:
1.青蛙跳台阶问题--100个台阶, 每次跳1,2,3个台阶, 一共有多少个跳法?
2.花钱问题--100块钱，每次可以花1,2,3块钱，一共有多少种花法？
3.求斐波那契数列的第n项
思路:
1.合理的数学建模，将问题转换成可递归公式.
2.合理利用递归思想, 但是用循环更快.
3.考虑到效率问题，在递归的基础上进行拔升
'''

def mySolution_better(n):#效率极高
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    sum=0
    first_num=1
    second_num=2
    third_num=4
    for i in range(3,n):
        sum=first_num+second_num+third_num
        first_num=second_num
        second_num=third_num
        third_num=sum
    return sum

