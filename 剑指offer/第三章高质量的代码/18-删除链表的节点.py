# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 22:39
# @Author  : DrMa
'''
题目:
在o(1)时间内删除链表节点
给定单向链表的头指针和一个节点指针,定义一个函数在o(1)时间内删除该节点.
思路:
我们要删除节点i,先把i的下一个节点j的内容复制到i,然后把i的指针指向节点j的下一个节点。
此时再删除节点j,其效果等同于把节点i删除了。
'''
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
def delete_node(head_node, del_node):
    if head_node==None or del_node==None:
        return False
    #要删除的节点不是尾结点
    if del_node.next!=None:
        del_node_next=del_node.next
        #先修改内容,覆盖value
        del_node.val=del_node_next.val
        #再修改指针
        del_node.next=del_node_next.next
        #删除结点j
        del_node_next.value=None
        del_node_next.next=None
    #要删除的节点是尾结点
    elif del_node.next==None:
        node=head_node
        while node.next!=del_node:
            node=node.next
        node.next=None
    #要删除的是尾结点而且等于头结点(链表只有一个节点)
    elif del_node==head_node:
        return None
    return head_node
