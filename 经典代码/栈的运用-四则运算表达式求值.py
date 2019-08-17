# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 15:48
# @Author  : DrMa
import sys
# eq_str=sys.stdin.readline().strip()
temp_str='9+(3-1)*3+2/2'#转为后缀表达式
num_list='0,1,2,3,4,5,6,7,8,9,19'.split(',')
print(num_list[::-1])
def zhong2hou(temp_str):
    stack = []
    output = []
    for i in temp_str:
        if i in num_list:
            output.extend(i)
        else:
            if stack==[]:
                stack.extend(i)
            else:
                if i=='(':
                    stack.extend(i)
                elif i==')':
                    stack_top=stack.pop()
                    if stack_top != '(' and stack_top != ')':
                        output.extend(stack_top)
                    while stack_top!='(':
                        stack_top = stack.pop()
                        if stack_top!='('and stack_top!=')':
                            output.extend(stack_top)
                else:
                    try:
                        while i in ['+','-'] and stack[-1] in ['*','/','+','-']:
                            #当前符号低于等于栈顶符号，栈顶符号依次出栈，直到当前符号不再满足‘低于等于栈顶符号’的条件。然后当前符号进栈。
                                stack_top = stack.pop()
                                output.extend(stack_top)
                        stack.extend(i)
                    except:
                        stack.extend(i)
    return output+stack[::-1]
hou=zhong2hou(temp_str)
print(hou)
stack=[]
for i in hou:
    if i in num_list:
        stack.extend(i)
    else:
        sec_num=int(stack.pop())
        fir_num=int(stack.pop())
        if i=="+":
            temp_num=fir_num+sec_num
        elif i=='-':
            temp_num=fir_num-sec_num
        elif i=='*':
            temp_num=fir_num*sec_num
        else :
            temp_num=fir_num//sec_num
        stack.append(temp_num)
print(stack[-1])