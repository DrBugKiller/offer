# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 12:01
# @Author  : DrMa
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
    return head.next
def visit_node(head):
    while head!=None:
        print(head.val)
        head=head.next

def reverse_node(head):
    if head==None or head.next==None:
        return head
    rev_node=None
    while head!=None:
        next_node=head.next#先缓存正向的第二个节点
        head.next=rev_node#让当前head的指针(next)指向已经反转的链表rev_node
        rev_node=head#更新反转的链表,此时rev_node的头结点已经是上一步的head
        head=next_node#遍历head到下一个节点
    return rev_node

if __name__=='__main__':
    l=[1,2,3,4]
    head=init_node(l)
    # visit_node(head)
    rever_node=reverse_node(head)
    visit_node(rever_node)