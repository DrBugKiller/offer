#字符串展开
'''
题目:
给定一个字符串, 然后按照
思路:
'''
# input_str=input()
# input_str=input_str.replace('(','[').replace(')',']')\
#     .replace('{','[').replace('}',']')

input_str=list('AB3[hello3[world]]CD3[hi person]')
#result='AB3[hello3[world'
result=[]

for i in input_str:
    if i==']':#只对result进行处理
        #step1: 拿到[]里的字符串
        temp_word_stack = [] #存放【】里边的字符
        while result[-1] != '[':
            temp_word_stack.append(result.pop())
        # temp_stack='dlrow'
        # result = 'AB3[hello3]'
        result.pop()#去掉 '['
        # result = 'AB3[hello3'
        temp_word_stack= temp_word_stack[::-1]#倒序
        # temp_stack='world'
        #setp2: 拿到系数
        # 154=4*1+5*10+1*100
        number, index= 0, 0
        while  result[-1].isdigit():#判断字符是否是数字
            digit=result.pop()
            number += int(digit) * (10 ** index)
            index+=1
        # result = 'AB3[hello
        result += temp_word_stack * number
        # result = 'AB3[helloworldworldworld
    elif i!=']':
        result.append(i)

print(''.join(result))#最后反向
