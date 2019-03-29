# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 9:11
# @Author  : DrMa
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop_(self):
        # return xx
        if len(self.stack2):#如果stack2有东西，直接把栈顶的pop出来即可
            return self.stack2.pop()
        while(self.stack1):#如果stack2空了，我们需要从stack1先pop出来然后push（append）到stack2中去
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

a=Solution()
for i in range(3):
    a.push(i)
print(a.pop_())
print(a.pop_())
quit()


'''
Question：
用两个stack完成一个queue的功能
tips:
1.python自带的pop作用是删除最后(最右边)一个元素。
1.1在python中list的append相当于在栈中push，pop就是正常操作--把最后append的元素删除并返回
2.python的list中，如果当做栈来看的话，左边属于栈底，右边属于栈顶，append和pop都是在右边操作的。
3.此题的核心就是：push是利用stack1完成的，pop是利用stack1先把元素pop后push到stack2然后pop

'''

