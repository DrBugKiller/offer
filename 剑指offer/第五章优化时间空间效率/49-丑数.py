# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 11:23
# @Author  : DrMa

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def get_min(ugly_num,num):
            i=0
            while ugly_num[i]*num<=ugly_num[-1]:
                i+=1
            return ugly_num[i]*num
        ugly_num=[1]
        for _ in range(1,n):
            min2=get_min(ugly_num,2)
            min3=get_min(ugly_num,3)
            min5=get_min(ugly_num,5)

            next_ugly=min(min2,min3,min5)
            ugly_num.append(next_ugly)

        return ugly_num[-1]
class Solution2:
    def nthUglyNumber(self,n):
        dp=[1]*n
        l2,l3,l5=0,0,0
        for i in range(1,n):
            dp[i]=min(2*dp[l2],3*dp[l3],5*dp[l5])
            #
            if dp[i]>=2*dp[l2]:
                l2+=1
            if dp[i]>=3*dp[l3]:
                l3+=1
            if dp[i]>=5*dp[l5]:
                l5+=1
        return dp[-1]
if __name__=='__main__':
    s=Solution2()
    res=s.nthUglyNumber(7)
    print(res)
