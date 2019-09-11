# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 19:21
# @Author  : DrMa
import sys
a='abcabc'
# a=input()
i=0
result=[]
while i <len(a):
    val=a[i]
    # j=i+1
    window=[]
    for j in range(len(a)-1,i-1,-1):
        if a[j]==val:

            window.append(a[i:j+1])
            # print(window)
            break
    # while j<len(a) and a[j]!=val:
    #     window.append(a[j])
    #     j+=1
    i=j+1
    result.extend(str(len(window[0])))
sys.stdout.write(','.join(result))