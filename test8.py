# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 19:39
# @Author  : DrMa
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
def solution(input_list):
    if not input_list:
        return False
    res=True
    length=len(input_list)
    if length%2==0:
        i=length//2-1
        j=length//2
        while i>=0 and j<=length-1:
            if input_list[i]==input_list[j]:
                i-=1
                j+=1
            else:
                res=False
    else:
        i=length//2-1
        j=length//2+1
        while i>=0 and j<=length-1:
            if input_list[i]==input_list[j]:
                i-=1
                j+=1
            else:
                res=False
    return res
if __name__=='__main__':
    input_list=input().split()
    print(solution(input_list))