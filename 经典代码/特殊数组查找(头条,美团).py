# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 19:44
# @Author  : DrMa
'''
题目:
一个数组中, 除了一个数字之外, 其他的数字都出现了两次.Find it!
思路:
Trick!
1.任何数字异或自己都是0.不信试试!
2.任何数异或0都是本身. 不信试试!
3.异或运算遵循交换分配率. 不信试试!

以上3点: 2 3 4 2 3
2^3^4^2^3=(2^2)^(3^3)^4=0^0^4=0^4=4
'''
def find_unique(a):
    result=a[0]
    for i in range(1,len(a)):
        result=result^a[i]
    return result
if __name__=='__main__':
    a=[2,3,4,2,3]
    unique=find_unique(a)
    print(unique)