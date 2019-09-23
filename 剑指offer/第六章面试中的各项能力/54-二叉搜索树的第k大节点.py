# -*- coding: utf-8 -*-
# @Time    : 9/20/2019 10:00 AM
# @Author  : DrMa
class Solution():
    def kthNode(self,root,k):
        def helper(root):
            if len(res)==k:
                return
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        res = []
        helper(root)
        return res[k-1]
