# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 23:09
# @Author  : DrMa
class Solution():
    def getEqualNumIndex(self,nums,start,end):
        if start>end: return None
        mid_index=(start+end)//2
        if nums[mid_index]==mid_index:
            return mid_index
        elif nums[mid_index]<mid_index:
            return self.getEqualNumIndex(nums,start=mid_index+1,end=len(nums)-1)
        elif nums[mid_index]>mid_index:
            return self.getEqualNumIndex(nums,start=start,end=mid_index-1)#注意此处start=start,不是0
if __name__=='__main__':
    s=Solution()
    test_data=[-3,-1,1,3,5]
    print(s.getEqualNumIndex(test_data,0,len(test_data)-1))
    a=[]
    print(a.pop())

