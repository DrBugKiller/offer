# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 15:22
# @Author  : DrMa
#跳柱子
class Solution():
    def getRes(self,hs,k,n):
        dp=[False]*n
        if n==1:
            return "YES"
        if k>=n-1:
            return 'YES'
        dp[0]=True
        for i in range(1,n):
            if i-k>=0:
                res=False
                for j in range(i-1,i-k-1,-1):
                    res=res or (dp[j] and (hs[i]<=hs[j]))
                dp[i]=res

            else:
                res = False
                for j in range(i - 1, - 1, -1):

                    res = res or (dp[j] and (hs[i] <= hs[j]))
                dp[i] = res
        if n>k:
            res=False
            for j in range(n-2,n-1-k-1,-1):
                res=res or dp[j]
            dp[n-1]=res
        # print(dp)
        if dp[n-1]:
            return 'YES'
        else:
            return 'NO'
    def getDistanceSum(self,n,nums):
        res=0
        if n<2:
            return 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    res+=(j-i)
        return res
def getDistanceSum(n,nums):
    res=0
    if n<2:
        return 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                res+=(j-i)
    return res
if __name__=='__main__':
    # num_input=int(input())
    # ns=[]
    # ks=[]
    # hs=[]
    # for _ in range(num_input):
    #     temp_input=list(map(int,input().split()))
    #     n=temp_input[0]
    #     k=temp_input[1]
    #     ns.append(n)
    #     ks.append(k)
    #     temp_input=list(map(int,input().split()))
    #     hs.append(temp_input)
    # s=Solution()
    # res_s=[]
    # for i in range(num_input):
    #     res=s.getRes(hs[i],ks[i],ns[i])
    #     res_s.append(res)
    # print('\n'.join(res_s))
    # s=Solution()
    # hs=[1,8,2,3,4]
    # k=2
    # n=5
    # print(s.getRes(hs,k,n))
    '''
    --------------
    '''
    num_input=int(input())
    temp_input = list(map(int, input().split()))
    print(getDistanceSum(num_input,temp_input))