# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:27
# @Author  : DrMa
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def get_path(self,pRoot,num):
        if pRoot==None or pRoot.val>num:
            return []
        if pRoot.left==None and pRoot.right==None and pRoot.val==num:
            return [[pRoot.val]]
        else:
            num-=pRoot.val
            left=self.get_path(pRoot.left, num)
            right=self.get_path(pRoot.right,num)
            result=[[pRoot.val]+i for i in left]
            for i in right:
                result.append([pRoot.val]+i)
        return sorted(result, key=lambda x:-len(x))
    