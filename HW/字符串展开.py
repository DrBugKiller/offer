#字符串展开
# input_str=input()
# input_str=input_str.replace('(','[').replace(')',']')\
#     .replace('{','[').replace('}',']')



input_str=list('AB3[hello3[world]]CD3[hi person]')
result=[]

for i in input_str:
    if i==']':
        temp_word_stack = [] #存放【】里边的字符
        while result[-1]!='[':
            temp_word_stack.append(result.pop())
        result.pop()#去掉[,
        temp_word_stack= temp_word_stack[::-1]#倒序
        #拿到[]的系数，54=4*1+5*10
        multiple,index=0,0
        while  result[-1].isdigit():
            multiple+=int(result.pop())*10**index
            index+=1
        result+= temp_word_stack * multiple
    else:
        result.append(i)

print(''.join(result))#最后反向
