# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 21:51
# @Author  : DrMa
'''
题目:把一个数组最开始的若干个元素搬到数组的末尾,我们称之为数组的旋转.
输入一个递增排序的数组的一个旋转, 输出旋转数组的最小元素.
例如, 数组{3,4,5,1,2}是{1,2,3,4,5}的一个旋转, 该数组的最小值为1.

思路: 充分发掘"递增数组"的"旋转数组"的特性.
定义两个index, 一个是最左边,一个是最右边, 每次定位数组中间的数:
 如果大于左边的第一个数, 说明这个数位于大的子数列中, 那么目标数位于它的右边, 令left_index更新为mid_index;
 如果小于右边的最后一个数, 说明这个数位于小的子数列中, 那么目标数位于它的左边或者它本身就是, 令high_index更新为mid_index.

'''
def min_num(a):
    if len(a)==1:
        return a[0]
    if a[0]<a[-1]:
        return a[0]
    low_index=0
    high_index=len(a)-1
    while low_index+1 !=high_index:
        mid_index=high_index//2
        if a[mid_index]>a[low_index]:
            a=a[mid_index:high_index+1]
        elif a[mid_index]<a[high_index]:#注意是elif而不是if
            a=a[low_index:mid_index+1]
        low_index=0
        high_index=len(a)-1
    return a[1]
if __name__=='__main__':
    test_array=[1,2,3]
    print(min_num(test_array))
