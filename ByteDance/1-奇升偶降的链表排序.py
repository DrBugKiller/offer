# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 10:19
# @Author  : DrMa
'''
题目: 一个链表,奇数结点升序,偶数结点降序,要求变成一个全升序的链表.
例如: 1-8-2-7-3-6-4-5  变为 1-2-3-4-5-6-7-8
思路:
1.按照奇数偶数拆分为两个链表
2.反转偶数结点构成的链表
3.合并两个递增链表
'''
class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

def split_list(head):
    #按照奇偶位拆分为两个链表
    head_odd,head_even=None,None
    temp_node_odd,temp_node_even=None,None
    count=1
    while head!=None:
        if count%2==1:#奇数位
            if temp_node_odd == None: #第一次,我们要生成一个头结点
                temp_node_odd = head
                head_odd = temp_node_odd  # head_odd变为头结点,temp_node_odd是它的探索节点
            elif temp_node_odd!=None: #头结点生成之后,开始延长链表
                temp_node_odd.next=head
                temp_node_odd=temp_node_odd.next

        elif count%2==0: #偶数位
            if temp_node_even==None:
                temp_node_even = head
                head_even = temp_node_even
            elif temp_node_even!=None:
                temp_node_even.next=head
                temp_node_even=temp_node_even.next

        head=head.next#更新为下一个节点
        count+=1
    temp_node_odd.next=None
    temp_node_even.next=None
    return head_odd,head_even
def reverse_list(head):
    #反转链表
    if  head==None or head.next==None:
        return head
    rev_node=None
    while head!=None:
        next=head.next#缓存
        head.next=rev_node#这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
        rev_node=head#更新逆序的链表
        head=next#更新当前节点
    return rev_node

def merge_list(head1,head2):
    head=Node(None)#定义一个空头结点
    temp_node=head
    while head1!=None and head2!=None:#条件为两个都不为空链表
        #添加head1或head2中比较小的节点
        if head1.val<=head2.val:
            temp_node.next=head1
            head1=head1.next
        elif head1.val>head2.val:
            temp_node.next=head2
            head2=head2.next
        temp_node=temp_node.next
    #while条件出来,肯定有一个链表是空的,把非空的链表接上
    if head1:
        temp_node.next=head1
    if head2:
        temp_node.next=head2
    return head.next


def init_list(l):
    #创建不带头结点的单链表,是为了对应好奇数位和偶数位,链表下标从1开始
    head=Node(None)
    temp=head
    for val in l:
        temp.next=Node(val)
        temp=temp.next
    temp.next=None
    return head.next
def visit_list(head):
    while head:
        print(head.val)
        head=head.next
if __name__=='__main__':
    head=init_list([1,8,2,7,3,6,4,5])
    visit_list(head)
    head1,head2=split_list(head)

    head2=reverse_list(head2)
    head=merge_list(head1,head2)
    visit_list(head)