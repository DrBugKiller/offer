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
注意:
1. 在32行代码.之所以复制matrix,因为在递归函数内部定义的变量, 它作为参数传入递归函数再次调用的时候,
它是可以被递归函数改变值得,相当于global了这个matrix. 显然我们不希望它在传入另一个方向的递归函数之前被改变,
所以我们复制一个matrix_,把它传入另一个方向的递归函数.
2. 复制matrix, 不能简单的matrix_=matrix就可以了,这是不行的, 因为这只是复制了一个新"指针",但对应的内存块
是一致的. 需要重新开辟新内存放入这个matrix, 即matrix_=[x for x in matrix]
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
        matrix_=[x for x in matrix]#决定成败的一句代码
        self.find_way(matrix,i+1,j,raws,cols)
        self.find_way(matrix_,i,j+1,raws,cols)

def jump(raws, cols):
    dp = [[1] * (cols) for _ in range(raws)]
    for i in range(1, raws):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[raws-1][cols-1])

if __name__ == "__main__":
    jump(3,3)
