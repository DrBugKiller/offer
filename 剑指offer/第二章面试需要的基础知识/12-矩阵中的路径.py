# -*- coding: utf-8 -*-# @Time    : 2019/7/25 22:37
# @Author  : DrMa
'''
题目:
请设计一个函数,判断在一个矩阵中是否存在一条包含某字符串所有字符的路径.
路径可以从矩阵中的任意位置开始, 每一步可以在矩阵中向左,右,上,下移动一格.
如果经过了矩阵的某一格, 那么该路径不能再次进入该格子.
'''
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find(list(matrix),rows,cols,path[1:],i,j):
                        return True
        return False
    def find(self,matrix,rows,cols,path,i,j):
        if not path:
            return True
        matrix[i*cols+j]='0'
        if j+1<cols and matrix[i*cols+j+1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j+1)
        elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i,j-1)
        elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i+1,j)
        elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
            return self.find(matrix,rows,cols,path[1:],i-1,j)
        else:
            return False