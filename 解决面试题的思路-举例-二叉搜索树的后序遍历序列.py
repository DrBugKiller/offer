# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 21:25
# @Author  : DrMa
'''
给定一个数组, 看能不能构成一个二叉搜索树
'''
class Tree(object):
    def __init__(self,root):
        self.val=root
        self.left=None
        self.right=None
class Solution:
    def VerifySquenceOfBST(self,sequence):
        if sequence==[]:
            return False
        length=len(sequence)
        root=sequence[-1]
        for i in range(length):
            if sequence[i]>root:
                break
        for j in range(i,length):
            if sequence[j]<root:
                return False
        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[:i])
        right=True
        if j<length-1:
            right=self.VerifySquenceOfBST(sequence[i:length-1])
        return left and right