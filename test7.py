# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 20:26
# @Author  : DrMa
import sys
N=int(input())
a=[]#label
b=[]#logit
for i in range(N):
    temp=input().split()
    a.append(int(temp[0]))
    b.append(float(temp[1]))

# N=10
# a=[1,0,1,1,0,1,0,0,1,0]
# b=[0.9,0.7,0.6,0.55,0.52,0.40,0.38,0.35,0.31,0.10]
p=[]
for i in range(N):
    temp_b=[1 if x>=b[i] else 0 for x in b]
    p11=0
    p1=0
    p10 = 0
    p0 = 0
    for x,y in zip(temp_b,a):
        if y==1:
            p1+=1
        if y==1 and x==1:
            p11+=1
        if y==0:
            p0+=1
        if y==0 and x==1:
            p10+=1
    true_positive=p11/p1
    false_positive=p10/p0
    print((true_positive,false_positive))
    p.append((false_positive,true_positive))
s=0
for i in range(len(p)-1):
    s_t=(p[i+1][0]-p[i][0])*(p[i+1][1]+p[i][1])/2
    s+=s_t
sys.stdout.write('%.2f'%(s))
