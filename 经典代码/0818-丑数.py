# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 9:19
# @Author  : DrMa
'''
题目:
判断是否为丑数? 丑数定义: 质因数只有2,3,5
思路:
暴力法: 只要num!=1,一直分别除以2,3,5,哪一次不整除了,返回False
'''
def isUgly(num):
    if num<1:
        return False
    while num!=1:
        if num%2==0:
            num/=2
        elif num%3==0:
            num/=3
        elif num%5==0:
            num/=5
        else:
            return False
    return True
print(isUgly(7))