# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 10:31
# @Author  : DrMa
def valid_seqv2(s):
    dp=[None]*100
    max=0
    for i in range(len(s)):
        dp[i]=0
    for i in range(len(s)-2,-1,-1):
        if s[i]=='(':
            j=i+1+dp[i+1]
            if j<len(s)and s[j]==')':
                dp[i]+=dp[i+1]+2
                if j+1<len(s):
                    dp[i]+=dp[j+1]
            if max<dp[i]:
                max=dp[i]
    print(max)
    return max

if __name__=='__main__':
    s='())((()))'
    s2='()()()'
    # print(valid_seq(s))
    #     # print(valid_seq(s2))
    valid_seqv2(s2)