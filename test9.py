# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 19:53
# @Author  : DrMa
def solution(input_list):
    small_happy=0
    big_happy=0
    while len(input_list)>=1:
        head=input_list[0]
        tail=input_list[-1]
        if head>=tail:
            small_happy+=head
            input_list=input_list[1:]
        else:
            small_happy+=tail
            input_list=input_list[:-1]
        if len(input_list)>=1:
            head = input_list[0]
            tail = input_list[-1]
            if head >= tail:
                big_happy += head
                input_list = input_list[1:]
            else:
                big_happy += tail
                input_list = input_list[:-1]
    if small_happy>=big_happy:
        print('Yes')
    else:
        print('No')
if __name__=='__main__':
    input_list=list(map(int,input().split()))
    solution(input_list)
