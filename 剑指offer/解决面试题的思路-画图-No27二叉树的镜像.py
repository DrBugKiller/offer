# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 18:50
# @Author  : DrMa
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def Mirror(self,root):
        if root==None:
            return  #此处return后没有变量,就是None
        if root.left==None and root.right==None:
            return root
        #正常的交换子节点
        ptemp=root.left
        root.left=root.right
        root.right=ptemp
        
        self.Mirror(root.left)
        self.Mirror(root.right)
