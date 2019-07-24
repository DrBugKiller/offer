# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:45
# @Author  : DrMa
'''
题目7-根据前序和中序遍历重建二叉树:
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
思路:
前序的第一个数字就是根节点.
从中序遍历中寻找根节点位置, 位置的左侧就是左子树, 右侧就是右子树.
分别划分左右子树的前序和中序遍历, 递归.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None#None是因为left的类型也是TreeNode类型
        self.right = None
'''
这种表示方法都是孩子表示法,递归定义. self.left如果存在子树,那么就不是None,
而是TreeNode类(利用了递归思想). 如果是叶节点,
'''
def reConstructBinaryTree(pre_order, in_order):
    if not pre_order or not in_order:
        return None
    '''
    其实他俩共存共消. 只要有一个是空,另一个肯定也是空的. 
    比如说1的左子树:pre_inder{2,4,7} ,in_order{4,7,2}. 
    根节点是2,显然右子树是不存在的,那么右子树的前序和中序都不存在.
    '''
    root = TreeNode(pre_order[0])#构建TreeNode类,并将val赋值成pre_order[0]
    root_idx = in_order.index(pre_order[0])#从中序遍历中拿到根节点所在的位置
    root.left = reConstructBinaryTree(pre_order[1: root_idx+1], in_order[0:root_idx])
    root.right = reConstructBinaryTree(pre_order[root_idx+1: ], in_order[root_idx+1: ])
    return root
'''
这里需要注意下list的索引相关问题,因为涉及到递归的结束条件;
详情看印象笔记中的"Python-list的index超过了list长度的两种情况":
1. 有冒号的情况下,如果某个索引值超出范围,并不会报错,返回一个空的list
2. 但是, 如果是没有冒号,只定位一个,那么就会报错.
'''
a=reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
print(a.val)
print(a.left.val)