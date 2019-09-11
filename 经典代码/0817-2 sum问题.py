# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 19:10
# @Author  : DrMa
'''
题目:
思路:
1. 两个for循环遍历, 时间是n^2, 一般不行.
2. 两遍哈希表
在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
然后，在第二次迭代中，我们将检查每个元素所对应的目标元素diff=(target−array[i])是否存在于表中。
注意，该目标元素不能是nums[i]本身,换句话说, 该目标元素diff的dict[diff]！=i,
主要是应对array[2,2,3,4]中有重复数字2,那么dict[2]=1 而不是dict[2]=0
'''
def sum2(array,target):
    #建立字典
    dic={}
    for i in range(len(array)):
        dic[array[i]]=i
    #查找
    for i in range(len(array)):
        diff=target-array[i]#diff是目标数
        if diff in dic and dic[diff]!=i:#如果差值存在于字典中,并且diff的位置!=i
            return [i,dic[diff]]
    return
def sum2v2(array,target):
    return

if __name__=='__main__':
    array=[1,2,3,4]
    array2=[2,2,4,5]
    target=4
    print(sum2(array2,target))
    print(sum2(array2,10))



