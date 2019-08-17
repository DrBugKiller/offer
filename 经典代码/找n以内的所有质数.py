# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 20:28
# @Author  : DrMa
'''
题目: 输出从2开始小于等于n的所有质数
思路:
质数就是除了1和本身它能整除, 别的数都不能整除.
'''
def find_prime(n):
    result=[]
    for i in range(2,n+1):
        #判断i是否是质数的条件:
        b=True
        for j in range(2,i-1):
            if i%j==0:
                b=False
        if b==True:
            result.append(i)
    return result
if __name__=='__main__':
    a=100
    b=find_prime(a)
    print(b)
