# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 16:32
# @Author  : DrMa
'''
Question:两个链表的第一个公共节点
tips：
1.利用两个栈，将链表分别放入其中，从栈顶（链表尾部）开始pop，一直到两个栈顶不相同为止
2.‘链表对齐’法：找到较长的链表，减去多余的部分，剩下的两个链表开始遍历，找到第一个相同的节点
3.C语言实现链表是靠指针与结构体实现的，结构体（结点）的尾部是指向下一结点的指针，Python没有指针，但是python是动态语言
python中没有chain的类型，我们需要自己定义。
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        p1 = pHead1
        p2 = pHead2
        a = 1
        b = 1
        ####
        while p1 and p1.next:
            a += 1
            p1 = p1.next
        while p2 and p2.next:
            p2 = p2.next
            b += 1
        if p1 != p2:
            return None
        #### 如果尾部结点都不相同，说明没有公共节点

        #### 补齐法
        if a > b:
            p1,p2 = pHead1,pHead2
        else:
            p1,p2 = pHead2, pHead1 #保证p1是较长的chain
        for i in range(abs(a-b)):#长出来的部分先.next()掉
            p1 = p1.next
        #如果两个Node不相同，一直.next()，直到相同就可以return p1了
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1
class Node():
    def __init__(self,my_list):
        self.my_list=my_list
    def next_(self):
        for i in self.my_list:
            iterm_data=i
            yield iterm_data
a=Node([1,2,3,4])
b1=a.next_()
b2=a.next_()
print(b1)
print(len(str('000001512E5309E8')))
print(b2)