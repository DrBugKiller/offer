# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 12:29
# @Author  : DrMa
def RadixSort(a):
    #得到最大数的位数
    digit_num = 1
    max_num = max(a)
    while max_num > 10**digit_num:
        digit_num += 1
    for i in range(digit_num):
        #初始化0-9个桶,我们用字典完成,新学习了setdefault方法
        bucket = {}
        for radix in range(10):
            bucket[radix] = [] # bucket.setdefault(radix, [])也可以
        #遍历数组构造桶
        for x in a:
            radix =(x // (10**i)) % 10   #得到每位的基数
            bucket[radix].append(x)      #将对应的数组元素加入到相应位基数的桶中
        #更新数组.把0-9这是个桶的所有num更新到a
        index = 0
        for radix in range(0,9+1):
            if bucket[radix]:
                for num in bucket[radix]:
                    a[index] = num
                    index += 1

def RadixSort2(a):#升级版,应对有负数
    a1,a2=[],[]
    for num in a:
        if num>=0:
            a1.append(num)
        else:
            a2.append(num)
    def helper(array):
        max_digit=1
        max_num=max(array)
        while max_num>10**max_digit:
            max_digit+=1
        for i in range(0,max_digit):
            bucket_dict={}
            for radix in range(0,9+1):
                bucket_dict[radix]=[]
            for num in array:
                radix=(num//10**i)%10
                bucket_dict[radix].append(num)
            index=0
            for radix in range(0,9+1):
                if bucket_dict[radix]:
                    for num in bucket_dict[radix]:
                        array[index]=num
                        index+=1
    #整数数组正常排序
    helper(a1)
    #负数数组取反
    temp_a2=[-x for x in a2]
    helper(temp_a2)
    temp_a2=temp_a2[::-1]
    a2=[-x for x in temp_a2]
    #合并
    a=a2+a1
    return a
if __name__ == '__main__':
    a = [12,3,45,3543,214,1,4553,14,0,-1,-3,-6,-2,-3,-7,-4,-11,-455]
    a=RadixSort2(a)
    print(a)


