# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 10:57
# @Author  : DrMa
'''
计数排序:
空间复杂度:n+k,n对应着新数组res,k代表计数数组count_array
时间复杂度:O(n+k)或者O(n),n代表遍历a,k代表遍历count_array
'''
def count_sort(a):
    min_num=min(a)
    max_num=max(a)
    #构造计数数组
    count_array=[0]*(max_num-min_num+1)
    for num in a:
        count_array[num-min_num]+=1#num-min_num目的是把a的每个数和count_array的下标对齐
    #生成新数组
    res=[]
    for num,count in enumerate(count_array):
        res+=[num+min_num]*count
    return res
def count_sort2(a):
    count_dict={}
    min_num=min(a)
    max_num=max(a)
    # 构造计数字典
    for num in range(min_num,max_num+1):
        count_dict[num]=0
    for num in a:
        count_dict[num]+=1
    # 生成新数组
    res=[]
    for num in range(min_num,max_num+1):
        res+=[num]*count_dict[num]
    return res
if __name__=='__main__':
    raw_array=[2,4,2,5,2,6,7,8,9,2,4,5,6,7,11,-1]
    new_array=count_sort2(raw_array)
    print(new_array)