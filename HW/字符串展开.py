#字符串展开
'''
题目:
给定一个字符串, 然后按照给定规则展开(也就是去掉括号,但是括号前边有乘数, 按照对应倍数扩充).
例如: abc2{2[def]}=abc2{defdef}=abcdefdefdefdef
思路:
Trick!
1. 栈的运用, 或者说 pop和append的运用.
2. 寻找[]对,遇到]开始找最近的[, 就是一对[]. 过程用while实现.
3. 将{},(),[]统一换成[], 在程序中没有的大小括号之分
'''
#替换括号
# input_str=input()
# input_str=input_str.replace('(','[').replace(')',']')\
#     .replace('{','[').replace('}',']')
input_str=list('AB3[hello3[world]]CD3[hi person]')
result=[]
for i in input_str:
    if i!=']':
        result.append(i) #result='AB3[hello3[world'
    elif i==']':#只对result进行处理

        #step1: 拿到[]里的字符串
        temp_word_stack = []
        while result[-1] != '[':
            temp_word_stack.append(result.pop())
        # temp_stack='dlrow'
        # result = 'AB3[hello3]'
        result.pop()#去掉 '['
        # result = 'AB3[hello3'
        temp_word_stack= temp_word_stack[::-1]#倒序
        # temp_stack='world'

        # setp2: 拿到系数
        number, index= 0, 0
        while  result[-1].isdigit():#判断字符是否是数字
            digit=result.pop()
            number += int(digit) * (10 ** index)   #154=4*1+5*10+1*100
            index+=1
        # result = 'AB3[hello
        result += temp_word_stack * number
        # result = 'AB3[helloworldworldworld
print(''.join(result))
