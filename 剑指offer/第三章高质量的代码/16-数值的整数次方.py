# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 22:38
# @Author  : DrMa
'''
题目: 实现函数double Power, 求base的exponent次方.不得使用库函数, 同时不需要考虑大数问题.
思路: 考虑指数是负数或者0等特殊情况.
'''
class Solution(object):
    def Power(self,base, exponent):
        if base==0.0 and exponent<0:#0的负几次方,这种情况首先要考虑
            return 0.0
        if exponent>=0:#指数是非负数
            return self.normal_power(base,exponent)
        elif exponent<0:#指数为负数
            return 1.0/self.normal_power(base,-exponent)
    def normal_power(self,base,exponent):
        result=1
        for _ in range(exponent):
            result=result*base
        return result

if __name__=='__main__':
    a=Solution()
    print(a.Power(0,-5))
    print(a.Power(2,3))
    print(a.Power(-2,3))
    print(a.Power(2,-3))
    print(a.Power(5,0))