# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 10:30
# @Author  : DrMa
class Solution():
    def numDecodings(self,s):
        dp=[1]*(len(s)+1)
        s='x'+s                 #下标对齐
        dp[1]=int(s[1]!='0')
        for i in range(2,len(s)):
            dp[i]=dp[i-2]*(9< int(s[i-1:i+1]) <=26)+dp[i-1]*(int(s[i]) > 0)
        return dp[-1]
if __name__=='__main__':
    s=Solution()
    test='1'
    res=s.numDecodings(test)
    print(res)