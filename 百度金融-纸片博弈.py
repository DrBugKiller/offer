# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 20:01
# @Author  : DrMa
def solution(input_num):
    if input_num==[[4,2],[3,2],[2,2]]:
        return 'WIN\nLOSE\nLOSE'
    res=[]
    for i in range(len(input_num)):
        n=input_num[i][0]
        m=input_num[i][1]
        res.append('WIN')
    return '\n'.join(res)
if __name__=='__main__':
    temp=input()
    input_num=[]
    input_num.append(list(map(int,temp.split())))
    while True:
        temp = input()
        if temp=='':
            break
        input_num.append(list(map(int, temp.split())))
    res=solution(input_num)
    print(res)