# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 20:20
# @Author  : DrMa
'''
题目: 堆排序
思路:
1. merge(a,b): a,b都是有序的.如[1,5,7],[2,4,8]
两个数组比较大小,小(或大的)拿出来,一直到两个数组都拿完,合成[1,2,4,5,7,8]
2. 递归思想: 就是递归将数组分为两半,一直到1,即len(a)<=1
'''
class Solution():
    #辅助函数
    def merge(self,a, b):
        i=0
        j=0
        result=[]
        while i<len(a)and j<len(b):
            if a[i]<=b[j]:
                result.append(a[i])
                i+=1
            elif b[j]<a[i]:
                result.append(b[j])
                j+=1
        result+= a[i:]  #切片的特殊性,如果i>=len(a),就反回空list
        result+= b[j:]
        return result
    #主函数
    def merge_sort(self,a):
        if len(a)<=1:
            return a
        mid = len(a) // 2
        left=self.merge_sort(a[:mid])
        right=self.merge_sort(a[mid:])
        result=self.merge(left,right)
        return result
if __name__=='__main__':
    s=Solution()
    a=[5,1,9,2,3]
    a=s.merge_sort(a)
    print(a)


