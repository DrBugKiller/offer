# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:43
# @Author  : DrMa
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        res, tree = [], [pRoot]
        while tree:
            row, subTree = [], []
            for item in tree:
                row.append(item.val)
                if item.left:
                    subTree.append(item.left)
                if item.right:
                    subTree.append(item.right)
            res.append(row)
            tree = subTree
        return res
    def Print_2(self,root):
        #这个思路比较符合剑指offer上的,利用队列.
        if root is None:
            return []
        queue=[]
        result=[]
        queue.append(root)
        while len(queue)>0:
            currentRoot=queue.pop(0)#队列和栈的区别就是有没有0, 栈是pop(-1), 队列是pop(0), 具体的数据结构都是list
            #讲结果放入result
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result