# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 21:33
# @Author  : DrMa
'''
题目: 堆排序
思路:
感谢B站up主的详解,有几个key point需要注意:
1. 如何用list表示完全二叉树?
2. 建堆的过程是?
3. 建堆完毕如何再排序?
'''
class Solution():
    def heap_sort(self,a):
        #辅助函数, 有半完全堆转为完全最大堆
        def heapify(a, start_index, end_index):
            #递归截止条件
            if start_index > end_index:
                return
            max_index = start_index
            l_c_index = 2 * start_index + 1  # 左子树结点index
            r_c_index = 2 * start_index + 2  # 右子树结点index
            #拿到最大
            if l_c_index <= end_index and a[max_index] < a[l_c_index]:  #先判断下标index没有出界，然后比较大小。顺序不能反了。
                max_index = l_c_index
            if r_c_index <= end_index and a[max_index] < a[r_c_index]:
                max_index = r_c_index
            #进行下一层的heapify
            if max_index != start_index:
                a[max_index], a[start_index] = a[start_index], a[max_index]
                heapify(a, start_index=max_index,end_index=end_index)
        #辅助函数, 从底往上建立大顶堆
        def build_max_heap(a):
            for index in range((len(a)-1-1) // 2, -1, -1):#从倒数第二层的第一个结点开始
                heapify(a, start_index=index,end_index=len(a)-1)
            return a
        #主函数
        a=build_max_heap(a)
        for end_index in range(len(a)-1,-1,-1):
            a[end_index],a[0]=a[0],a[end_index]
            heapify(a,start_index=0,end_index=end_index-1)#进行下一次heapify,不过范围缩进了一个,所以end_index-1
        return a
if __name__=='__main__':
    a=[1,3,7,4,2,5,3]
    s=Solution()
    s.heap_sort(a)
    print(a)

