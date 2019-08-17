# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 20:20
# @Author  : DrMa
'''
题目:
一个长的字符串a,一个短的字符串b, 如果a包含b,输入a的起始位置.
例如: a=[1,2,3,4,2,3], b=[2,3,4], 输出[1]
思路:
BF,Brute-Froce算法,暴力破解

'''
def string_match(a,b):
    a_index=0
    b_index=0
    while a_index<=len(a)-1 and b_index<=len(b)-1:
        if a[a_index]==b[b_index]:
            a_index+=1
            b_index+=1
        elif a[a_index]!=b[b_index]:
            b_index=0 #b从头再来
            a_index=a_index-b_index+1# a从上次匹配的位置的下一个位置开始
    if b_index==len(b):#说明b指针已经到最后并且也满足条件
        return a_index-b_index
    else:
        return None
if __name__=='__main__':
    a=[1,2,3,4,5,6]
    b=[2,3,7]
    index=string_match(a,b)
    print(index)
