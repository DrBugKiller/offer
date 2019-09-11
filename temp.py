# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 20:29
# @Author  : DrMa
# n = int(input())
# eq = input().split()
eq='1 + 2 - 3 * 4 / 5 + 6 - 7'.split()
for i in range(len(eq)):
    if i%2==0:
        eq[i]=int(eq[i])
bool_list=[None]*len(eq)
for i in range(1,len(eq),2):
    print(eq[i])
    if i==1:
        if eq[i]=='+' and eq[i+2]!='*' and eq[i+2]!='/':
            bool_list[i]=True
        elif eq[i]=='*':
            bool_list[i] =True
        elif eq[i]=='-':
            bool_list[i] =False
        elif eq[i]=='/':
            bool_list[i] =False
    elif i==len(eq)-2:
        if eq[i]=='+' and eq[i-2]!='*' and eq[i-2]!='/':
            bool_list[i] =True
        elif eq[i] == '*':
            bool_list[i] =True
        elif eq[i]=='-':
            bool_list[i] =False
        elif eq[i]=='/':
            bool_list[i] =False
    else:
        if eq[i]=='+' and (eq[i+2]=='+' or eq[i+2]=='-') and (eq[i-2]=='+' or eq[i-2]=='-'):
            bool_list[i] =True
        elif eq[i]=='-':
            bool_list[i] =False
        elif eq[i]=='*':
            bool_list[i] =True
        elif eq[i]=='/':
            bool_list[i] =False
print(bool_list)
while i < len():
    pass