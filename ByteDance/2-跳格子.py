# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 21:06
# @Author  : DrMa
'''
题目:
给定一个m*n的矩阵,从左上角开始走,终点是右下角.
每次只能向右走或者向下走,问有多少种走法?
思路:
1. 回溯,DFS
2. 动态规划
'''
class BackTrack():#BackTrack denotes "回溯法"
    def __init__(self):
        self.ways=0
    def ways_count(self,raws,cols):
        matrix=[1 for _ in range(raws*cols)]
        self.find_way(matrix,0,0,raws,cols)
        return self.ways
    def find_way(self,matrix,i,j,raws,cols):
        if i<0 or i>raws-1 or j<0 or j>cols-1 or matrix[i*cols+j]!=1:
            return
        if i==raws-1 and j==cols-1:
            self.ways+=1
            return
        matrix[i*cols+j]=0
        matrix_=[x for x in matrix]
        self.find_way(matrix,i+1,j,raws,cols)
        self.find_way(matrix_,i,j+1,raws,cols)


if __name__ == "__main__":

    print(BackTrack().ways_count(3,3))
    # x, y = map(int, input().strip().split())
    # x,y=2,2
    # dp = [[1] * (y + 1) for _ in range(x + 1)]
    # for i in range(1, x + 1):
    #     for j in range(1, y + 1):
    #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # print(dp[x][y])