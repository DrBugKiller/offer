# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 20:29
# @Author  : DrMa
'''
题目: 给定一个列表[1,2,3,#,4,5,6], 构建二叉树, 然后给出各种遍历结果.
思路:
DFS
'''
class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution():
    def main_buildTree(self,node_list):
        #递归部分
        def buidTree(i):
            if i>len(node_list)-1:
                return None
            if node_list[i]=='#':
                return None
            node=Tree(node_list[i])#生成一个节点
            node.left=buidTree(2*i+1)#左子树
            node.right=buidTree(2*i+2)#右子树
            return node
        #主函数部分
        node=buidTree(0)
        return node

def pre_order(node):#前序遍历, 根左右
    if node==None:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):#中序遍历, 左根右
    if node==None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)

def back_order(node):#后序遍历,左右根
    if node==None:
        return
    back_order(node.left)
    back_order(node.right)
    print(node.val)

s=Solution()
node=s.main_buildTree([1,2,3,'#',4,5,6])
# print(node.val)
# print(node.left.val)
# print()
# quit()
print('preorder')
pre_order(node)
print('inorder')
in_order(node)
print('backorder')
back_order(node)