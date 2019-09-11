# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:44
# @Author  : DrMa
'''
题目3-特殊数组中重复的数字:
找出某特殊数组中重复的数字.在一个长度为n的数组里的所有数字都在0~n-1的范围内(特殊性)
例如, 输入{2,3,1,0,2,5,3},输出是2或者3.
思路:
1: 遍历数组，构造字典，判断是否在字典中。时间复杂度O(n),空间复杂度O(n)
2: "重排"这个数组：遍历这个数组，如果数值m和下标i相等，那就扫描下一个；如果不相等，判断m和a[m]是否
相等，如果相等，说明重复；如果不相等，则将m和a[m]对应的数值交换，使得数值在和自己下标相同的位置。
'''
def duplicate(a):
    for index in range(len(a)):
        value=a[index]
        if value==index:
            continue
        elif value!=index:
            if value ==a[value]:
                return value
            else:
                a[index],a[value]=a[value],a[index]
    print()
if __name__=='__main__':
    a=[2,1,3,0,2]
    print(duplicate(a))