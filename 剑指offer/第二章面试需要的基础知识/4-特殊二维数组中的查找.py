# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 11:44
# @Author  : DrMa
'''
题目4-特殊二维数组中的查找:
一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序(特殊性)。
请完成一个函数，输入这样一个二维数组和一个整数，判断数组中是否含有该整数。
思路:
右上角(或者左上角)判断法，由于数组递增的特殊性，我们将target和array的右上角（左下角）比较：
1.相等，直接返回True；2.target<右上角，删除最后一列；3.target>右上角, 删除第一行.
'''
#右上角比较
def array_Find_right_top(target, array):
    # 注意这个判断条件，就是说数组不为空，行数>0并且列数>0
    while len(array) > 0 and len(array[0]) > 0:
        if array[0][-1] == target:#先判断，满足就退出，两个return，只要return了一个，后边的就不会再次return
            return True
        elif target<array[0][-1]:
            array = [a[:-1] for a in array] #删除最后一列
        elif target>array[0][-1]:
            array = array[1:]   #删除第一行
    return False #这个return False是有前提的，就是前面并没有return任何东西。
#左下角比较
def array_Find_left_bottom(target,array):
    while len(array)>0 and len(array[0])>0:
        if target==array[-1][0]:
            return True
        elif target<array[-1][0]:
            array=array[:-1]
        elif target>array[-1][0]:
            array=[x[1:] for x in array]
    return False
if __name__=='__main__':
    target = 11
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(array_Find_right_top(target, array))
    print(array_Find_left_bottom(target,array))