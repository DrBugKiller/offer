# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:46
# @Author  : DrMa
'''
题目8-二叉树的下一个结点:
思路:
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None#指向父节点的
#这个应该是双亲孩子表示法
def GetNext(pNode):
    # write code here
    if not pNode:#pNode是None就返回None
        return pNode
    if pNode.right:#if pNode.right!=None:如果一个节点有右子树,那么它的下一个节点是右子树中最左子节点
        temp=pNode.right
        while temp.left:
               temp=temp.left
        return temp
    #一个节点没有右孩子
    while pNode.parent:#一直到pNode是根节点,那么pNode.parent是None
        if pNode==pNode.parent.left:#如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。
            return pNode.parent
        #如果pNode不是左子树,往上走,一直找到左子树的跟节点.
        pNode=pNode.parent#如果pNode是根节点就结束
    return pNode
#pNode是TreeLinkNode类, 有4个属性值, 除了根节点是数值, 其他都是子树或者父母树类