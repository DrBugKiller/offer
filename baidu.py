# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 20:42
# @Author  : DrMa

if __name__=='__main__':
    temp_input=list(map(int,input().split()))
    a=[0]*temp_input[4]
    a[0]=temp_input[0]
    a[1]=temp_input[1]
    a[2]=temp_input[2]
    a[3]=temp_input[3]
    n=temp_input[4]
    for i in range(4,n):
        a[i]=a[i-1]+a[i-3]+a[i-4]
    print(a[n-1])
    a1=a[0]
    a2=a[1]
    a3=a[2]
    a4=a[3]
    a5=0
    for i in range(4,n):
        a5=a4+a2+a1
        a4=a5
        a2=a4
        a1=a2
