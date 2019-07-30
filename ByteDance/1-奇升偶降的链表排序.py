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
def init_list(l):
    #创建不带头结点的单链表,是为了对应好奇数位和偶数位,链表下标从1开始
    head=Node(None)
    temp=head
    for val in l:
        temp.next=Node(val)
        temp=temp.next
    temp.next=None
    return head.next
def split_list(head):
    #按照奇偶位拆分为两个链表
    head1,head2=None,None
    cur1,cur2=None,None
    count=1
    while head!=None:#
        if count%2==1:#奇数位
            if cur1!=None:
                cur1.next=head#构建不带头结点的cur1
                cur1=cur1.next
            elif cur1==None:#if cur1==None,把head的空头结点给它
                cur1 = head#head=cur1, head1=cur1, 他俩同步变化
                head1 =cur1#这一步很有意思,cur1
        elif count%2==0: #偶数位
            if cur2!=None:
                cur2.next=head
                cur2=cur2.next
            elif cur2==None:#if cur2==None,把head的空头结点给它
                cur2 = head#赋值顺序 head=cur2, head2=cur2
                head2 = cur2
        head=head.next#更新为下一个节点
        count+=1
    cur1.next=None
    cur2.next=None
    return head1,head2
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
def merge_list(head1,head2):#合并列表
    head=Node(None)
    tail=head
    while head1!=None and head2!=None:
        if head1.val<=head2.val:
            tail.next=head1
            head1=head1.next
        elif head1.val>head2.val:
            tail.next=head2
            head2=head2.next
        tail=tail.next
    if head1:
        tail.next=head1
    if head2:
        tail.next=head2
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