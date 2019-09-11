# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 16:10
# @Author  : DrMa
'''
24小时计时制是一个广为使用的计时体系。
但是不同地方使用的计数进制是不同的，
例如，在一个古老的村庄就是使用二进制下的24小时制，
这时“11：11”表示的就是3点03分。

现在给出一个未知的时刻，用形如“a:b”的形式来表示，a，b分别是一个字符串，
字符串可以由0-9和A-Z组成，分别代表0-9和10-35。
请你求出这个时刻所处的所有可能的进制。
'''
def solution(time_str):
    hour_str=time_str.split(':')[0]
    min_str=time_str.split(':')[1]
    res=[]
    start=[]
    end=[]
    max_char=0
    for char in hour_str+min_str:
        try:
            num=int(char)
            if max_char<num:
                max_char=num
        except:
            pass
    start=max_char+1
    res='4 5 6'
    return res
if __name__=='__main__':
    time_str=input()
    print(solution(time_str))