# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:47
# @Author  : DrMa
'''
题目9：
用两个stack完成一个queue的功能
Tips:
1.python自带的pop作用是删除最后(最右边)一个元素并返回其值。
2.python的list中，如果当做栈来看的话，左边属于栈底，右边属于栈顶，append和pop都是在右边操作的。
3.此题的核心就是：push是利用stack1完成的，pop是利用stack1先把元素pop后push到stack2然后pop.
'''
class queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop_(self):
        # 如果stack2还有东西，说明之前已经pop过,接着pop即可.
        if len(self.stack2)>0:
            return self.stack2.pop()
        # 如果stack2没有东西, 说明这是第一次pop, 先把stack1所有的都放到stack2中,
        # 再stack2.pop()即可
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
a=queue()
for i in range(3):
    a.push(i)
print(a.pop_())
print(a.pop_())
