# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 21:38
# @Author  : DrMa
'''
题目: 输入一个链表的头结点, 从尾到头反过来打印每个节点的值.
思路: 遍历整个链表, 然后把节点放到一个list中, 倒序输出即可.
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def printListFromTailToHead(listNode):
    if not listNode:#注意这个条件, 没有就会报错.
        return []
    res=[]
    while listNode.next is not None:#条件的写法
        res.append(listNode.val)
        listNode=listNode.next
    res.append(listNode.val)#把最后没有.next的listNode的节点也放到res中
    return res[::-1]