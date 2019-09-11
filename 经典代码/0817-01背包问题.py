# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 15:03
# @Author  : DrMa
'''
题目: 01背包
思路:
Trick!
状态转移方程, dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
'''
def knapsack(N, M, weight, value):
    '''
    :param N: 商品数量
    :param M: 背包最大容量
    :param weight: 物品的重量
    :param value:  物品的价值
    '''
    dp=[[0 for _ in range(M+1)] for _ in range(N+1)]#初始化,注意边界
    #让i代表真实索引
    weight= [0] + weight
    value= [0] + value
    for i in range(1,N+1):
        for j in range(1, M+1):
            #当前第i件物品的重量超过当前背包容量j
            if  weight[i]>j:
                dp[i][j]=dp[i-1][j]
            #当前第i件物品的重量没有超过背包容量j
            elif weight[i]<=j:
                value1= dp[i-1][j-weight[i]] + value[i]    #选择当前物品
                value2= dp[i-1][j]                         #不选择当前物品
                dp[i][j]=max(value1,value2)                #选择价值更大的
    return dp[N][M]
if __name__=='__main__':
    N = 5  # 5代表商品数量
    W = 20  # 20代表背包容量
    weight = [3, 2, 4, 9, 5]  # 代表物品各自重量,注意加上0
    value = [4, 3, 5, 10, 8]  # 代表物品各自价值,注意加上0
    max_value=knapsack(N, W, weight, value)
    print(max_value)