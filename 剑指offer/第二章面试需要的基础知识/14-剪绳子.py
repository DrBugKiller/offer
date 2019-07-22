# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:52
# @Author  : DrMa
'''
Questions:
给定一个长度为n（整数）绳子，剪成m（整数）段，使得绳子的乘积最大。
Tips:
1.常规的动态规划O(n**2)时间复杂度，O(n)空间复杂度
2.贪婪算法，需要数学功底
'''
class Solution:
    def MaxProductAfterCut(self, n):
        # 动态规划
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        #剩下的是针对从n=4以后的
        products = [0] * (n + 1)
        products[0] = 0#这个0我觉得可以不要
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max:#遍历1~（i除以2向下取整），对应f
                    max = product
            products[i] = max
        # print(products)
        return products[n]

    def MaxProductAfterCut2(self, n):
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
print(Solution().MaxProductAfterCut(8))
print(Solution().MaxProductAfterCut(10))
# print(Solution().NumberOf1(0))
print(Solution().MaxProductAfterCut2(8))
print(Solution().MaxProductAfterCut2(10))