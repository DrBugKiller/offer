# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 14:56
# @Author  : DrMa
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None#None是因为left的类型也是TreeNode类型
        self.right = None
'''7 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
def reConstructBinaryTree(self, pre_order, in_order):
    if not pre_order or not in_order:
        return None
    #其实他俩共存共消. 只要有一个是空,另一个肯定也是空的. 比如说1的左子树:pre_inder{2,4,7} ,in_order{4,7,2}. 根节点是2,显然右子树
    #是不存在的,那么右子树的前序和中序都不存在.
    root = TreeNode(pre_order[0])#构建TreeNode类,并将val赋值成pre_order[0]
    pos = in_order.index(pre_order[0])#从中序遍历中拿到根节点所在的位置,然后

    root.left = self.reConstructBinaryTree(pre_order[1: pos+1], in_order[:pos])
    root.right = self.reConstructBinaryTree(pre_order[pos+1: ], in_order[pos+1: ])
    #我想问为什么pos+1如果超长度了不会报错?答案是不会报错,超过len(list)只会返回空的[]
    return root