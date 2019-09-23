# -*- coding: utf-8 -*-
# @Time    : 9/23/2019 10:58 AM
# @Author  : DrMa
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        for c in zip(*strs):
            print(c)
            if len(set(c)) == 1:
                res = res + c[0]
            else:
                break
        return res

if __name__=='__main__':
    s=Solution()
    test_data=['flower','flow','flight']
    res=s.longestCommonPrefix(test_data)
    print(res)
