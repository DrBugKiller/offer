# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 21:24
# @Author  : DrMa
'''
题目:逆时针或者顺时针旋转n*n方形矩阵
思路:
1. 先沿着主对角线反转两侧数字, 即转置
2. 按行将矩阵进行反转.

待会上图
'''
def reverse_matrix(a,mode):
    # 转置
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    if mode=='逆':
        #行对称变换
        for i in range(len(a)//2):
            a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    elif mode=='顺':
        #列对称变换
        for i in range(len(a)):
            for j in range(len(a)//2):
                a[i][j],a[i][len(a)-j-1]=a[i][len(a)-j-1],a[i][j]
    return

if __name__=='__main__':
    a=[[1,2,3],
       [4,5,6],
       [7,8,9]]
    for x in a:
        print(x)
    print('\n')
    reverse_matrix(a, mode='顺')
    for x in a:
        print(x)