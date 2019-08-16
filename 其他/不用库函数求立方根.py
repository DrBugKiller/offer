# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 22:42
# @Author  : DrMa
'''
题目:
不使用库函数求出立方根
思路:
1. 二分法, 一直到满足误差.
2. 注意如果a在0~1之间, start和end的更新是和a>1的情况相同的.
例如, a=9, 我们取start=1, end=9, 中间值mid就是5, 然后5**3>9 并且误差超过了E,
说明reuslt在mid的左边, 然后令end=mid=5, start=1, 再从1~5中取中间值, 迭代直到 -E<误差<E
'''
def root(a):
    if a==0:
        return a
    b=True# b=True代表a是整数,因为立方根是中心对称的,我们取反,按照整数来,最后来把结果取反
    if a<0:
        a=-a
        b=False
    E = 0.001  # 作为精度
    start,end=1,a#无论a==1还是0<a<1都是满足下边的计算的.
    while True:
        mid = (start + end) / 2
        dif = mid ** 3 - a
        if -E<dif<E :#满足条件
            result=mid
            break
        if a>1 and dif>E :
            end=mid
        elif a>1 and dif<-E:
            start=mid
        elif a<1 and dif>E:#a:0~1之间的情况
            start=mid
        elif a<1 and dif<-E:
            end=mid
    if b==False:
        result=-result
    return result
if __name__=='__main__':
    a=-0.9
    print(root(a))