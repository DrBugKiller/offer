# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 14:49
# @Author  : DrMa
'''
Question:
一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样一个二维数组和一个整数，判断数组中是否含有该整数。
tips:
缩小范围的思路：从右上角或者左下角和目标int作比较，结合数组的特殊排序，分为三种情况，右上角的数=目标数，直接return

'''
#这是自己的写的
class MySolution():
    def __init__(self,array_input,int_input):
        self.array_input=array_input
        self.int_input=int_input
    def judge(self):
        result=False
        raw_int = self.array_input[0][-1]
        try:#防治list index out of range
            if raw_int==self.int_input:
                result=True
            else:
                while self.int_input!=raw_int:
                    if self.int_input<raw_int:
                        self.array_input=[[y for y in x[:-1]]for x in self.array_input]#需改进
                        raw_int=self.array_input[0][-1]
                    if self.int_input>raw_int:
                        self.array_input=[[y for y in x]for x in self.array_input[1:]]#需改进
                        raw_int = self.array_input[0][-1]
                    if self.int_input==raw_int:
                        result=True
                        break
        except Exception as e:
            print(e)
            return result
        return result
array_input=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
a=MySolution(array_input,1)
print(a.judge())
#别人的，太简洁了
def Find(target, array):
    # write code here
    while len(array) > 0 and len(array[0]) > 0:#这个判断条件就是说数组不为空，行数>0并且列数>0
        print(array)
        if array[0][-1] == target:#先判断，满足就退出，两个return，只要return了一个，后边的就不会再次return
            return True
        elif array[0][-1] > target:
            # remove column
            array = [a[:-1] for a in array]#这句比我的简洁
        else:
            # remove row
            array = array[1:]#这句比我的简洁：把第一行删除，不删列，换句话说就是不取第0行，从第1行开始
    return False #这个return False是有前提的，就是前面并没有return任何东西。

if __name__ == '__main__':
    target = 1
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(Find(target, array))



