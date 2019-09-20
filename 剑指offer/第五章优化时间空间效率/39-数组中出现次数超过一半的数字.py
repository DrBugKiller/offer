# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 12:02
# @Author  : DrMa
'''
题目39:
数组中有一个数字出现的次数超过数组长度的一半,请找出这个数字.
思路:
1. 超过一半, 说明该数字的次数大于其他数字的和. 我们用两个变量保存该数字,另一个保存次数,
遍历数组,遇到相同的次数加1, 遇到不同的次数减1,
如果次数到零了,那暂时不是目标的数,更新当前最大数,并把次数再次设置为1.
2. 另一种思路就是有个推理,数组的中位数肯定是目标数
'''
def solution(a):
    max_num=a[0]
    num_of_mn=1
    for i in range(1,len(a)):
        if a[i]==max_num:
            num_of_mn+=1
        else:
            num_of_mn-=1
            if num_of_mn==0:
                max_num=a[i]
                num_of_mn=1
    return max_num

class Solution:
    def majorityElement(self, nums):
        def partition(nums,low,high):
            pivot=nums[low]
            l=low
            r=high
            while l<r:
                while l<r and nums[r]>pivot:
                    r-=1
                while l<r and nums[l]<=pivot:
                    l+=1
                if l<r:
                    nums[l],nums[r]=nums[r],nums[l]
            nums[low],nums[r]=nums[r],nums[low]
            return r
        length=len(nums)
        middle=length>>1

        pivot_index=partition(nums,0,length-1)
        while pivot_index!=middle:

            if pivot_index>middle:
                pivot_index=partition(nums,0,pivot_index-1)

            elif pivot_index<middle:
                pivot_index=partition(nums,pivot_index+1,length-1)

        return nums[pivot_index]

if __name__=='__main__':
    s=Solution()
    nums=[-1,1,1,1,2,1]
    print(nums)
    res=s.majorityElement(nums)
    print(res)