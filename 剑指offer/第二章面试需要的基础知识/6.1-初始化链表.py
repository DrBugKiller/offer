# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 11:51
# @Author  : DrMa
'''
题目: 输入一个list, 构造一个链表结构, 并输出该链表.
'''
class node(object):
    def __init__(self,val):
        self.val=val
        self.next=None
def init_node(l):
    head=node(None)
    temp_node=head
    for val in l:
        temp_node.next=node(val)
        temp_node=temp_node.next
    temp_node.next=None
    return head.next#从第二个节点开始而不是第一个

def visit_node(head):
    while head!=None:
        print(head.val)
        head=head.next

if __name__=='__main__':
    l=[1,2,3,4]
    head=init_node(l)
    visit_node(head)
