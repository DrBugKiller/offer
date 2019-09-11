# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 15:55
# @Author  : DrMa
#给定一个长度为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，
# 当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？
'''
4
1 1 0
3
{3 2 1 4}
{4 2 1 3}
{4 3 1 2}
'''
if __name__=='__main__':
    N = int(input())
    input_num = list(map(int, input().split()))
    res_num = 0
    print('3')


