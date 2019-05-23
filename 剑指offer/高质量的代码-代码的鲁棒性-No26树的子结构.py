# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 11:05
# @Author  : DrMa
class Tree(object):
    def __init__(self,root):
        self.val=root
        self.left=None
        self.right=None
'''
输入两棵二叉树A和B,判断B是不是A的子树.
思路: 1.在树A中找到和B的根节点的值一样的节点R
      2.第二步在判断树A中以R为根节点的子树是不是包含和树B一样的结构
'''
def hasSubtree(pRoot1, pRoot2):
    if not pRoot1 or not pRoot2:#有个疑问就是pRoot2如果是空树, 应该返回True
        return False
    result = False
    # 如果根节点相同,则递归判断
    if (pRoot1.val == pRoot2.val):
        result =isSubtree(pRoot1, pRoot2)
    #如果根节点不同,此时result=False
    if not result:#if result==False
        result =hasSubtree(pRoot1.left, pRoot2)
    #
    if not result:
        result =hasSubtree(pRoot1.right, pRoot2)
    return result

def isSubtree(p1, p2):#这个递归函数的前提是,p1和p2的根节点相同
    if p2==None:
        return True
    if p1==None:
        return False
    if p1.val != p2.val:
        return False
    #这些条件都不满足, 需要遍历所有的节点
    return isSubtree(p1.left, p2.left) and isSubtree(p1.right, p2.right)
#难点就是递归函数中还包含着一个函数.

class Solution:
    def HasSubtree(self,pRoot1,pRoot2):
        result=False
        if pRoot1!=None and pRoot2!=None:
            if pRoot1.val==pRoot2.val:
                result=self.DoesTree1hasTree2(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result
    def DoesTree1hasTree2(self,pRoot1,pRoot2):
        if pRoot2==None:#如果是空树,肯定是子树,但是肯定不会有这种情况,因为上面的函数有限制.
            return True
        if pRoot1==None:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.DoesTree1hasTree2(pRoot1.left,pRoot2.left)and self.DoesTree1hasTree2(pRoot1.right,pRoot2.right)