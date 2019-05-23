# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 14:58
# @Author  : DrMa

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None#指向父节点的
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:#pNode是None就返回None
            return pNode
        if pNode.right:#如果一个节点有右子树,那么它的下一个节点是右子树中最左子节点
            temp=pNode.right
            while temp.left:
                   temp=temp.left
            return temp

        while pNode.parent:#一直到pNode是根节点,那么pNode.parent是None

            if pNode==pNode.parent.left:#如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
                return pNode.parent

            pNode=pNode.parent#如果pNode是根节点就结束