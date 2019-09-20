# -*- coding: utf-8 -*-# @Time    : 2019/7/25 22:37
# @Author  : DrMa
'''
题目:
请设计一个函数,判断在一个矩阵中是否存在一条包含某字符串所有字符的路径.
路径可以从矩阵中的任意位置开始, 每一步可以在矩阵中向左,右,上,下移动一格.
如果经过了矩阵的某一格, 那么该路径不能再次进入该格子.
思路:
递归. 先从matrix中找到一个入口,即等于path[0]的位置.
然后从此位置开始递归, 上下左右四个方向都要考虑, 同时注意边界条件.
最后注意主函数的return False的条件, 递归函数return True的条件.
'''
class Solution():
    def whether_path(self,matrix, rows, cols, path):
        #递归函数
        def hasPath_(matrix, path, i, j):
            #递归结束条件
            if not path:
                return True
            matrix[i * cols + j] = '0'#做一个已经走了的标志
            if path[0] == matrix[(i - 1) * cols + j] and i - 1 >= 0:  # 往上走,不能出了边界
                return hasPath_(matrix, path[1:], i - 1, j)
            elif path[0] == matrix[(i + 1) * cols + j] and i + 1 <= rows - 1:  #往下走,不能出了边界
                return hasPath_(matrix, path[1:], i + 1, j)
            elif path[0] == matrix(i * cols + j - 1) and j - 1 >= 0:  #往左走,不能出了边界
                return hasPath_(matrix, path[1:], i, j - 1)
            elif path[0] == matrix(i * cols + j + 1) and j + 1 <= cols - 1:  #往右走,不能出了边界
                return hasPath_(matrix, path[1:], i, j + 1)
            else:
                return False
        #主函数部分
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j]==path[0]: #找到入口
                    if hasPath_(matrix,path[1:],i,j)==True:
                        return True
        return False #这一句别忘了.如果hasPath_没有递归





def find(matrix,rows,cols,path,i,j):
    if not path:
        return True
    matrix[i*cols+j]='0'
    if j+1<cols and matrix[i*cols+j+1]==path[0]:
        return find(matrix,rows,cols,path[1:],i,j+1)
    elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
        return find(matrix,rows,cols,path[1:],i,j-1)
    elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
        return find(matrix,rows,cols,path[1:],i+1,j)
    elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
        return find(matrix,rows,cols,path[1:],i-1,j)
    else:
        return False

def hasPath(matrix, rows, cols, path):
    for i in range(rows):
        for j in range(cols):
            if matrix[i*cols+j] == path[0]:
                if find(list(matrix),rows,cols,path[1:],i,j):
                    return True
    return False