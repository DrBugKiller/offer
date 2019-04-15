# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 15:44
# @Author  : DrMa


def contentMerge(v1,v2):#追加模式：v1中的每一个字符串后追加v2中字符的内容,v1,v2是个list，elem是string的pattern
    if len(v1)<1:
        return v2
    else:
        results=[]
        for i in v1:#v1代表前一步所有的pattern
            for j in v2:#v2代表当前步所有的pattern
                results.append(i+j)
        return results
def get_or_index(pattern_str):#输入是pattern_str,输出是所有最外层'|'的位置
    ors = []
    depth = 0  # 当前级别
    for i in range(len(pattern_str)):
        c = pattern_str[i]
        if c == '<':  # 因为成对出现，最后肯定depth又变成的；
            depth += 1
        elif c == '>':
            depth -= 1
        elif c == '|' and depth == 0:
            ors.append(i)  # 与根同层的|符号，直接拆分为子pattern处理
    return ors
def analysePattern(pattern,rootDepth):
    '''
    string: pattern
    int: rootDepth
    bool: addEmpty
    "<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>"
    '''
    result=[]
    #存储最外层的|的位置，比如：<A>[B]|<C>[D]|<E>这个或就是与根同层的，我们切分<A>[B]和<C>[D]和<E>三个合并append就可以了
    #这里的小trick就是<>[]是成对出现之后的|符号才是与根同级。
    ors=get_or_index(pattern)
    length=len(pattern)
    start=0
    if len(ors)>0:#包含与根同层的或符号，直接拆分处理
        for i in range(len(ors)):
            end=ors[i]
            print(pattern[start:end])
            part=analysePattern(pattern[start:end],rootDepth)#递归了，
            start=end+1#|位置的下一个位置开始
            result+=part#因为result和part同级，我们用extend
        part = analysePattern(pattern[start:], rootDepth)
        result+=part
    else:#此时没有最外的|,此时没有同级的，只有先后级别
        depth=rootDepth
        stacks=[] #存放int的栈，把<和[的位置记录下来
        hasPattern=False #是否包含标记符| <> []
        necessary_Start=0 #标记形如"歌[曲]"或"[歌]曲"的情况，他们等同于"<歌>[曲]"或"[歌]<曲>"

        for i in range(length):#开始遍历pattern的string
            c=pattern[i]
            if c=='<':
                if depth==rootDepth:
                    if i>necessary_Start:#把中间没有<>但是必选的内容放进去
                        print('pattern[necessary_Start:i]:',pattern[necessary_Start:i])
                        part=analysePattern(pattern[necessary_Start:i],depth)
                        result=contentMerge(result,part)
                hasPattern=True
                depth+=1#深度+1
                stacks.append(i)
            elif c=='>':
                depth-=1
                if depth==rootDepth:
                    necessary_Start=i+1
                index=stacks.pop()
                if depth==rootDepth:
                    print('pattern[index+1:i]:',pattern[index+1:i])
                    part=analysePattern(pattern[index+1:i],depth+1)#看一下这个
                    result=contentMerge(result,part)
        if hasPattern==False:#<>|[]都没有，那就直接把pattern放进去
            result.append(pattern)
        else:
            if necessary_Start<len(pattern):#处理形如<A|B>C的C这一部分
                print('pattern[necessary_Start:len(pattern)]:',pattern[necessary_Start:len(pattern)])
                part=analysePattern(pattern[necessary_Start:len(pattern)],depth)
                result=contentMerge(result,part)
    return result
def del_square_brackets(str_input):
    str_output=str_input.replace('[','<').replace(']','|>')
    return str_output
test_str='<<A|B>C>D'
test_str=del_square_brackets(test_str)
inputs = "小爱同学，<[播]放|来>[一|几]<首|曲|个>周杰伦的<歌[曲]|[流行]音乐>好吗？"
inputs=del_square_brackets(inputs)
all_ex=set(analysePattern(inputs,0))
print(test_str)
print(all_ex)




