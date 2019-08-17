# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 15:03
# @Author  : DrMa
'''
题目: 01背包
思路:
Trick!
状态转移方程, dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
'''
N=5+1 #5代表商品数量
W=20+1 #20代表背包容量
weight=[0, 3, 2, 4, 9, 5] #代表物品各自重量,注意加上0
value=[0, 4, 3, 5, 10, 8] #代表物品各自价值,注意加上0

def knapsack(N, max_weight, w, v):
    B=[[0 for _ in range(max_weight)] for _ in range(N)]
    for i in range(1,N):
        for j in range(1, max_weight):
            if w[i]>j:#第i件物品的重量超过背包容量j
                B[i][j]=B[i-1][j]
            else:#从选或不选的两种value中,挑出最大的.
                value1=B[i-1][j-w[i]]+v[i] #选择当前物品
                value2=B[i-1][j]           #不选择当前物品
                if value1>value2:
                    B[i][j]=value1
                else:
                    B[i][j]=value2
    return B[-1][-1]
if __name__=='__main__':
    max_value=knapsack(N, W, weight, value)
    print(max_value)