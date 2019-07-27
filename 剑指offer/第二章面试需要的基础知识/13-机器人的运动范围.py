# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:40
# @Author  : DrMa
'''
题目:
地上有一个m行n列的方格. 一个机器人从坐标(0,0)的格子开始移动, 它每次可以向上下左右移动一格,
但不能进入行坐标和列坐标的数位之和大于k的格子.
例如, 当k为18时, 机器人能够进入方格(35,37),因为3+5+3+7=18. 但不能进入(35,38),因为3+5+3+8>19.
请问该机器人能够到达多个格子?
思路:
递归,回溯法. 但是此题跟上一题不一样,上一题是上下左右四选一,然后这里是四个方向都递归.
'''
class Solution:
    def __init__(self):
        self.count = 0
    def movingCount(self,threshold,rows,cols):
        matrix=[1 for _ in range(rows*cols)]#初始化方格, 令其都为1, 表示都能走
        self.findway_(matrix,0,0,threshold,rows,cols)#注意参数-- 时刻变化的矩阵matrix; 位置; 阈值; 行数,列数;
        return self.count
    def findway_(self,matrix,i,j,k,rows,cols):
        #注意退出条件: 四个方向超过边界; 坐标数位和大于阈值; 已经走过的位置
        if i<0 or j<0 or i>rows-1 or j>cols-1 or self.get_sum_of_digital(i,j)>k or matrix[i*cols+j]!=1:
            return None
        self.count+=1 #如果经过上面的条件没有退出,那么说明此处可走,总数+1
        matrix[i*cols+j]=0 #所到之处设为0,表示不能再走了.
        self.findway_(matrix,i-1,j,k,rows,cols)#向上走
        self.findway_(matrix, i+1, j, k,rows, cols)#向下走
        self.findway_(matrix, i, j-1, k, rows, cols)#向左走
        self.findway_(matrix, i, j+1, k, rows, cols)#向右走
    def get_sum_of_digital(self,i,j):
        #求i和j的各自的数位字和. 例如,i=363,j=12, 那个返回3+6+3+1+2=15
        num=i
        sum=0
        while num//10!=0:
            sum+=num%10
            num=num//10
        sum+=num
        num=j
        while num//10!=0:
            sum+=num%10
            num=num//10
        sum+=num
        return sum
