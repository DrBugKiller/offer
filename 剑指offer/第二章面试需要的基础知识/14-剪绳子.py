# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:52
# @Author  : DrMa
'''
题目:
给定一个长度为n（整数）绳子，剪成m（整数）段，使得绳子的乘积最大。
思路:
1.常规的动态规划O(n**2)时间复杂度，O(n)空间复杂度
首先定义f[n]是,把长度为n的绳子剪成若干段后各段长度乘积的最大值.
第一刀的选择有n-1种,因为动态规划可以将大问题看成子问题,所以f[n]=max(f[i]*f[n-i])
以上是"从上往下"分析问题,我们接下来是"从下往上"求解问题.
我们先得到f[2],f[3],在得到f[4],f[5],直到f[n].
'''
def MaxProduct_DP(n):
    # 动态规划, 从上往下分析问题, 从下往上求解问题
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    # 剩下的是针对n>=4的
    f = [0] * (n+1) #注意f的长度要设置为n+1个,因为我们要求f[n]
    #f[1]并不代表绳子长度1的时候乘积最大是1. 而是为了计算比如f[4]=f[1]*f[3]. f[2],f[3]同理
    f[1],f[2],f[3] = 1,2,3
    #f[4]~f[n]每个f[i]才真正代表长度i的最优解.
    for len_rope in range(4, n+1):#从下往上求解问题, len_per_rope代表绳子长度
        #遍历所有的切法,取最大,i代表切的位置,
        #i从1到长度的一半即可,例len_rope=9,i:1~4即可.因为f[9]=f[4]*f[5]和f[9]=f[5]*f[4]一样,不需要重复.
        max_product = 0
        for i in range(1, len_rope//2+1):
            prodcut = f[i] * f[len_rope-i] #将大问题分为两个小问题
            if max_product < prodcut:
                max_product = prodcut
        f[len_rope] = max_product
    return f[n]



def MaxProduct_greedy(self, n):
    # 贪婪算法
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    timesOf3 = n // 3
    if n - timesOf3 * 3 == 1:
        timesOf3 -= 1

    timesOf2 = (n - timesOf3 * 3) // 2
    return (3 ** timesOf3) * (2 ** timesOf2)
