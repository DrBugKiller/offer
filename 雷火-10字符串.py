# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 16:49
# @Author  : DrMa
class Solution():
    def get_num(self,n):
        self.res = 0
        def helper(a,index):
            if index==len(a):
                if judge(a[:]):
                    self.res+=1
                    print(a[:])
                return
            for char in ['0','1']:
                a[index]=char
                helper(a,index+1)
        def judge(a):
            res=True
            if not a.count('0') or a[0]=='0':
                return False
            for i in range(1,len(a)):
                if a[i]=='0'and a[i-1]!='1':
                    res=False
            return res

        a=['x']*n
        helper(a,0)
        return self.res
if __name__=='__main__':
    n=4
    s=Solution()
    num=s.get_num(n)
    print(num)