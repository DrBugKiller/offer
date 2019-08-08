# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 21:56
# @Author  : DrMa
'''
题目:
输入数字n,按顺序打印出从1到最大的n位十进制数.
比如输入3,则打印出1,2,3一直到最大的3位数999.
思路:
1.考虑到大数问题,不能简单的for循环打印所有的.
2.将问题转换为数字排列的解法,递归让代码更简洁
'''
class Solution:
    def Print_1_to_max(self,n):
        if n<=0:
            return
        number_list=['0']*n
        for i in range(10):
            number_list[0]=str(i)
            self.Print_recursively(number_list,n,0)
    def PrintNumber(self,number_list):
        always_is_zero=True#这个标志是前边部分都是0的意思:000123
        for num in number_list:
            #前边都是0,当前不是0,说明我们找到了非0的
            if always_is_zero==True and num!='0':
                always_is_zero=False
            if always_is_zero==False:
                print('%c'%num)
        print('\t')
    def Print_recursively(self,number,length,index):
        if index==length-1:
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index+1]=str(i)
            self.Print_recursively(number,length,index+1)

# a=Solution()
# a.Print_1_to_max(2)

def Print_recursively(number,length,index):
    if index==length-1:
        print(number)
        return
    for i in range(10):
        number[index+1]=str(i)
        Print_recursively(number,length,index+1)
test_list=['0','0','0']
Print_recursively(test_list,3,0)