# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 18:40
# @Author  : DrMa
'''
全排列
123:
123,132,213,231,312,321
'''
class Solution:
    def permute(self, nums):

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(0,len(nums)):#len(nums)是随着递归层数递减的.
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        res = []
        backtrack(nums, [])
        return res
'''
子集
123
1,2,3,12,13,23,123,[]
'''
class Solution2:
    def subsets(self, nums):
        if not nums:
            return []
        def backtrack(start_id, temp_list):
            res.append(temp_list)
            if start_id==n:
                return

            for i in range(start_id, n):
                backtrack(i+1,temp_list+[nums[i]])

        res = []
        n = len(nums)
        backtrack(0,[])

        return res
if __name__=='__main__':
    a=[1,2,3]
    s=Solution2()
    res=s.subsets(a)
    print(res)