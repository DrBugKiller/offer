# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:50
# @Author  : DrMa
'''
题目10-斐波那契数列:
1.青蛙跳台阶问题，花钱问题
2.求斐波那契数列的第n项
思路:
1.合理的数学建模，将问题转换成可递归公式
2.合理利用递归思想
3.考虑到效率问题，在递归的基础上进行拔升
'''
from  datetime import datetime
#100块钱，每次可以花1,2,3块钱，一共有多少种花法？
def mySolution(n):#简单，但是效率低
    if n==1:
        sum=1
    elif n==0:#边界值考虑清楚,如果有0元，那么0种花法
        sum=0
    elif n==2:#此处注意的是一定要把n=2,n=3考虑进去，因为此时它不满足sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
        sum = 2
    elif n==3:
        sum=4
    else:
        sum = mySolution(n-1) + mySolution(n-2) + mySolution(n-3)
    return sum
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
    f_num=1
    s_num=2
    t_num=4
    for i in range(3,n):
        sum=f_num+s_num+t_num
        f_num=s_num
        s_num=t_num
        t_num=sum
    return sum
n=mySolution(3)
m=mySolution_better(100)
print(n)
print(m)
#斐波那契数列,但是效率极低
def mySolution_Fibonacci(n):
    if n==1:
        sum=1
    elif n==0:
        sum=0
    else :
        sum = mySolution_Fibonacci(n-1) + mySolution_Fibonacci(n-2)
    return sum
a=datetime.now()
print(mySolution_Fibonacci(35))
print(datetime.now()-a)
#斐波那契数列，效率极高，时间复杂度O(n)
def mySolution_Fibonacci_better(n):#0 1 1 2 3 5
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    #剩下的从3开始
    first=1
    second=1
    sum=0
    for i in range(2,n):
        sum=first+second
        first=second
        second=sum
    return sum
a=datetime.now()
print(mySolution_Fibonacci_better(35))
print(datetime.now()-a)