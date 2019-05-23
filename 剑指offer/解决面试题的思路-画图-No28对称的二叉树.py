# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 19:02
# @Author  : DrMa
class Tree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        else:
            return self.isSameTree(pRoot.left, pRoot.right)

    def isSameTree(self, p, q):
        # 如果两个都空, 此时说明p和q的父母都是叶节点了
        if not p and not q:
            return True
        # 如果两个有一个为空
        if not p or not q:
            return False
        # 如果两个都不为空
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.right)
            r = self.isSameTree(p.right, q.left)
            return l and r


# result=[{'捕前文化程度':7,'民族':0,'犯罪编号':123,'性别':1},{'捕前文化程度':8,'民族':1,'犯罪编号':234,'性别':2}]
# order_list=['犯罪编号','性别','民族','捕前文化程度']
# # for name in order_list:
# #     result_new=[x[name] for x in result]
# #     print(result_new)
# output_list=[]
# for sample in result:
#     sample_list=[]
#     for i in range(len(order_list)):
#         sample_list.append(sample[order_list[i]])
#     output_list.append(sample_list)
# print(output_list)