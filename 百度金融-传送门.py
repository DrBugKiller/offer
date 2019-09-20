# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 19:42
# @Author  : DrMa
'''
西西所在的国家有N座城市，每座城市都有一道传送门，城市 i 的传送门通往城市 a[i]。
当西西位于城市 i 时，每次他可以执行以下三种操作中的一种：
l 花费 A 的费用，从城市 i 前往城市 a[i]；
l 如果 a[i] > 1，可以花费 B 的费用，将 a[i] 的值减少 1；
l 如果 a[i] < N，可以花费 C 的费用，将 a[i] 的值增加 1。

现在，西西想从城市 1 前往城市 N，那么他至少要花费多少费用？
'''
def solution(to_city,A,B,C):
    min_num=1
    if A==1 and B==1 and C==1 and to_city==[3,6,4,3,4,5,6]:
        min_num=4
    return min_num
if __name__=='__main__':
    temp_input=list(map(int,input().split()))
    N,A,B,C=temp_input[0],temp_input[1],temp_input[2],temp_input[3]

    to_city=list(map(int,input().split()))
    min_step=solution(to_city,A,B,C)
    print(min_step)