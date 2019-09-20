# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 18:39
# @Author  : DrMa


class Solution:
    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        copy = data[:]  #空间换时间
        copy.sort()     #升序,从小到大
        count = 0
        for i in range(len(data)):
            count += data.index(copy[i])#核心,index大小=前边比你大的数的个数. 也就是对应逆序对的个数.
            data.remove(copy[i])
        return count%1000000007
if __name__=='__main__':
    test_data=[7,5,6,4]
    s=Solution()
    print(s.InversePairs(test_data))


