# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 19:08
# @Author  : DrMa
def get_max_height(n,heights):
    max_index=0
    max_num=0
    for i in range(n-1):
        val_obj=heights[i]
        cur_num=0
        j=i+1
        if heights[j]<=val_obj:
            cur_num+=1
            j+=1
        while j<=n-1:
            cur_height = heights[j]
            if i+1<j:
                max_height=max(heights[i+1:j])
                if cur_height>max_height and cur_height<=heights[i]:
                    cur_num+=1
                j+=1
            else:
                if cur_height<=heights[i]:
                    cur_num += 1
                j += 1
        if cur_num>max_num:
            max_num=cur_num
            max_index=i
    return heights[max_index]
if __name__=='__main__':
    n=int(input())
    heights=list(map(int,input().split()))
    res=get_max_height(n,heights)
    print(res)