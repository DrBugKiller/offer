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

def buidTree(node_list,i):
    if i>len(node_list)-1:
        return None
    if node_list[i]=='#':
        return None
    node=Tree(node_list[i])
    node.left=buidTree(node_list,2*i+1)
    node.right=buidTree(node_list,2*i+2)
    return node
def pre_order(node):#前序遍历, 根左右
    if node==None:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node==None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)

def back_order(node):
    if node==None:
        return
    back_order(node.left)
    back_order(node.right)
    print(node.val)

node=buidTree([1,2,3,'#',4,5,6],0)
print(node.val)
print(node.left.val)
print()
quit()
print('preorder')
pre_order(node)
print('inorder')
in_order(node)
print('backorder')
back_order(node)