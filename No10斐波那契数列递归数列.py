# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 10:54
# @Author  : DrMa
'''
Question:
1.青蛙跳台阶问题，花钱问题
2.求斐波那契数列的第n项
Tips:
1.合理的数学建模，将问题转换成可递归公式
2.合理利用递归思想
'''
#100块钱，每次可以花1,2,3块钱，一共有多少种花法？
def mySolution(n):
    if n==1:
        sum=1
    elif n==0:#边界值考虑清楚,如果有0元，那么0种花法
        sum=0
    elif n==2:#此处注意的是一定要把n=2考虑进去，因为此时它不满足sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
        sum = 2
    else:
        sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
    return sum
n=mySolution(4)
print(n)
#斐波那契数列
def mySolution_for(n):
    if n==1:
        sum=1
    elif n==0:
        sum=0
    else:
        sum = mySolution(n-1) + mySolution(n-2)
    return sum
n=mySolution_for(30)
print(n)