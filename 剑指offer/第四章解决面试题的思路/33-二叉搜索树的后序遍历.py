# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 18:16
# @Author  : DrMa
class Solution():
    def judge(self,a):
        #递归函数
        def helper(a):
            if not a:
                return True
            root=a[-1]  #根节点
            left,right=[],[]
            # 指针从左开始,拿到左子树
            i = 0
            while a[i]<root:
                left.append(a[i])
                i+=1
            # 剩下的是右子树
            right=right+a[i:len(a)-1]
            # 判断右子树是否符合条件
            for num in right:
                if num<root:
                    return False
            # 递归返回左子树和右子树的结果
            return helper(left) and helper(right)
        #主函数
        if not a :
            return False
        res=helper(a)
        return res
if __name__=='__main__':
    a=[5,7,6,9,11,10,8]
    b=[7,4,6,5]
    s=Solution()
    res=s.judge(b)
    print(res)