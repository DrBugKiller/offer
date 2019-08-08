# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 20:24
# @Author  : DrMa
#递归实现二分查找 li是列表   item是要查找的元素
def merge_search( li ,item ):
    #传来的列表每次都是新生成的，如果发现里面没有元素，则是查找到尽头都没找到
    if not li :
        return False

    mid = len(li)//2   #mid记录li的中间位置
    #检查一下 如果中间这个数就是要找的元素 返回真
    if li[mid] == item :
         return True
     # 如果mid比item大，说明item可能会出现在mid左边，对左边再查找
    elif li[mid]> item :
        return merge_search( li[:mid] ,item )
     # mid 比item小，说明item有可能在mid右边，对右边再查找
    else:
         return merge_search( li[mid+1:] , item )

if __name__ == '__main__':
     li = [1,2,3,4,5,6,7]
     print( merge_search(li , 0) )   #False
     print( merge_search(li , 1) )   #True