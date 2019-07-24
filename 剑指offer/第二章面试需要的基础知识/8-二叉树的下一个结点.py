# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:46
# @Author  : DrMa
'''
题目8-二叉树的下一个结点:
给定一棵二叉树和其中的一个节点,如何找出中序遍历序列的下一个节点?
树中的节点除了有两个分别指向左,右子节点的指针,还有一个指向父节点的指针.
思路:
我们分3种节点考虑:
1. 有右子节点或右子树: 那么一直找它的左子树, 直到没有左子树, Tree_node.left=None
2. 没有右子节点或右子树, 但是父节点的左子节点: 那么它的父节点就是它下一个节点.
3. 没有右子节点或右子树, 但是父节点的右子节点: 那么向上找父节点, 直到找到一个父节点,
                                            这个父节点是父父节点的左子树, 就返回

'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None#指向父节点的
def GetNext(pNode):
    if not pNode:#pNode是None就返回None
        return pNode
    #如果一个节点有右子树,那么它的下一个节点是右子树中最左子节点
    if pNode.right:
        temp=pNode.right
        while temp.left:
               temp=temp.left
        return temp
    #如果pNode不是左子树,往上走,一直找到左子树的跟节点.
    while pNode.parent:
        if pNode==pNode.parent.left:
            return pNode.parent
        pNode=pNode.parent#如果pNode是根节点就结束
    return pNode