# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 19:22
# @Author  : DrMa
class Solution:#我自己的写法,但是时间复杂度较高
    def get_count2(self,nums,target):
        def get_first_target(nums,target,length,start,end):#拿到target的第一个index
            if start>end: return -1
            mid_index=(start+end)//2
            if nums[mid_index]==target:
                if mid_index>0 and nums[mid_index-1]!=target or mid_index==0:
                    return mid_index
                else:
                    return get_first_target(nums,target,length,start=start,end=mid_index-1)
            elif nums[mid_index]<target:
                return get_first_target(nums,target,length,start=mid_index+1,end=length-1)
            elif nums[mid_index]>target:
                return get_first_target(nums,target,length,start=start,end=mid_index-1)
        def get_last_target(nums,target,length,start,end):#拿到target的最后一个index
            if start>end: return -1
            mid_index=(start+end)//2
            if nums[mid_index]==target:
                if mid_index<length-1 and nums[mid_index+1]!=target or mid_index==length-1:
                    return mid_index
                else:
                    return get_last_target(nums,target,length,start=mid_index+1,end=end)
            elif nums[mid_index]<target:
                return get_last_target(nums,target,length,mid_index+1,end=end)
            elif nums[mid_index]>target:
                return get_last_target(nums,target,length,start=start,end=mid_index-1)
        length = len(nums)
        first_target_index=get_first_target(nums,target,length,start=0,end=length-1)
        last_target_index=get_last_target(nums,target,length,start=0,end=length-1)
        if first_target_index!=-1 and last_target_index!=-1:
            return last_target_index-first_target_index+1
        return 0
if __name__=='__main__':
    test_nums=[1,2,3,3,3,3,4,5]
    s=Solution()
    print(s.get_count2(test_nums,4))

    def get_count(self,nums,target):
        count=0
        if not nums:
            return 0
        mid_index=len(nums)//2
        if nums[mid_index]==target:
            count+=1
            count+=self.get_count(nums[:mid_index],target)
            count+=self.get_count(nums[mid_index+1:],target)
        elif nums[mid_index]<target:
            count+=self.get_count(nums[mid_index+1:],target)
        elif nums[mid_index]>target:
            count+=self.get_count(nums[:mid_index],target)
        return count