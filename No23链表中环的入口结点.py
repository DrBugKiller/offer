# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 14:34
# @Author  : DrMa
'''
Questions:
寻找链表中环的入口结点
tips:
1.首先判断是否有个环。--利用一快一慢双指针法判断能否再次相遇？
2.再次寻找环的入口位置：假设知道环的长度n，有个很有意思的现象--让一个指针先走n步，然后另一个指针才开始走，那么他们之后必定在环入口处相遇。
以上结论可以画一个图来解释。
问题是如何获取n？
--在第一步判断是否有个环的时候我们利用了一快一慢指针，它们必定相遇在环内而不是环外，所以我们把相遇到的节点位置记录下来，然后利用慢的指针在转一圈，
当再回到这个节点的时候，步数就是n。
warning：
涉及到链表，首先加一个判断，第一个节点和下一个节点不是None，增加程序的鲁棒性
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:#
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next#慢的走一步
            fast = fast.next.next#快的走两步
            if slow == fast:
                return True
        return False#再次利用了最后一个返回return
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return None
        fast = slow = pHead
        while (fast and fast.next):#只要当前节点和下一个节点不是None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:#slow是相遇节点
                fast = pHead#fast从头开始
                while (fast != slow):#期待再次相遇在入口节点？这样的话剑指offer的小结论就用不上了，但是可以试一试这个方法
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

    def EntryNodeOfLoop2(self, pHead):  # 21ms 5860K
        # write code here
        count = 0
        p1 = pHead
        p2 = pHead
        while True:
            p2 = p2.next
            if p2 == None:
                return None
            p2 = p2.next
            if p2 == None:
                return None#p2是fast
            p1 = p1.next
            count += 1
            if p1 == p2:
                break
        n = count  # 环的长度
        p1 = pHead
        p2 = pHead

        while n > 0:
            p2 = p2.next#先行n步
            n -= 1

        while True:
            if p2 == p1:#等再次相遇就是环的入口
                break
            p2 = p2.next
            p1 = p1.next

        return p1


