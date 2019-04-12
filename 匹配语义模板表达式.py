# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 15:44
# @Author  : DrMa


def plusfuhao(a):
    left_index = a.index('<')
    if a[:left_index].count('>') == 0 and a[0]!='<':
        a = '<' + a[:left_index] + '>' + a[left_index:]
    return a
def real_xianhou(a):
    def get_xianhou_patt(a):
        all_patt_list = []
        while len(a)>0:
            one_patt_list = []
            for i in a:
                one_patt_list.append(i)
                if one_patt_list.count('>')==one_patt_list.count('<')and one_patt_list.count('<')>0:
                    try:
                        a=a[len(one_patt_list):]
                        all_patt_list.append(''.join(one_patt_list))
                        break
                    except:
                        break
        return all_patt_list
    all_temp=get_xianhou_patt(a)
    all_real = []
    for i in all_temp:
        a = plusfuhao(i)
        a_all = get_xianhou_patt(a)
        all_real += a_all
    return all_real

def contentMerge(v1,v2):#追加模式
    #v1中的每一个字符串后追加v2中字符的内容,v1,v2是个list，elem是string的pattern
    if len(v1)<1:
        return v2
    else:
        results=[]
        for i in v1:#v1代表前一步所有的pattern
            for j in v2:#v2代表当前步所有的pattern
                results.append(i+j)
        return results
# a=plusfuhao(a)


def prase_patt(pattern_str):
    if pattern_str.count('<')==1and pattern_str.count('>')==1:
        if pattern_str.count('|'):
            real_result=[]
            temp_list=pattern_str.replace('<','').replace('>','').split('|')
            for i in temp_list:
                if i!='':
                    real_result.append(i)
            return real_result
        else:
            real_result = []
            temp_list=[pattern_str.replace('<', '').replace('>', '')]
            for i in temp_list:
                if i!='':
                    real_result.append(i)
            return real_result
    elif pattern_str.count('<')==0 and pattern_str.count('>')==0:
        if pattern_str.count('|'):
            real_result=[]
            temp_list=pattern_str.split('|')
            for i in temp_list:
                if i!='':
                    real_result.append(i)
            return real_result
        else:
            real_result = []
            if pattern_str!='':
                real_result=[pattern_str]
            return real_result
    else:
        #把最外层的|干掉
        ors = []
        depth = 0  # 当前级别
        for i in range(len(pattern_str)):
            c=pattern_str[i]
            if c == '<':  # 因为成对出现，最后肯定depth又变成的；
                depth += 1
            elif c == '>' :
                depth -= 1
            elif c == '|' and depth == 0:
                ors.append(i)  # 与根同层的|符号，直接拆分为子pattern处理
        start = 0
        result=[]
        if len(ors) > 0:  # 包含与根同层的或符号，直接拆分处理
            for i in range(len(ors)):
                end = ors[i]
                part = prase_patt(pattern_str[start:end])  # 递归了，
                start = end + 1  # |位置的下一个位置开始
                result.extend(part)  # 因为result和part同级，我们用extend
        else:#说明没有大的并集，只有先后,这一部分出现问题
            all_xianhou_patt = real_xianhou(pattern_str)
            #['<一|>', '<df>']没有问题
            for i in range(len(all_xianhou_patt)):
                result = contentMerge(result, prase_patt(all_xianhou_patt[i]))
        return result

a="[一]<df>|ji"
print('原始    ',a)
a=a.replace(']','|>').replace('[','<')
print('修改后    ',a)
print(prase_patt(a))
quit()





def analysePattern(pattern,rootDepth,addEmpty):
    '''
    string: pattern
    int: rootDepth
    bool: addEmpty
    "<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>"
    '''
    result=[]
    if addEmpty:#是否可选，如果可选，增加‘’，这是【】的针对方法
        # 注意，这个平级的append，就是在一个<>中
        result.append('')

    #存储最外层的|的位置，比如：<A>[B]|<C>[D]|<E>这个或就是与根同层的，我们切分<A>[B]和<C>[D]和<E>三个合并append就可以了
    #这里的小trick就是<>[]是成对出现之后的|符号才是与根同级。
    ors=[]
    length=len(pattern)#拿到pattern长度
    depth=rootDepth#当前级别
    for i in range(length):
        c = pattern[i]#char
        if c=='<'or c=='[':#因为成对出现，最后肯定depth又变成的；
            depth+=1
        elif c=='>' or c==']':
            depth-=1
        elif c=='|'and depth==rootDepth:
            ors.append(i)   #与根同层的|符号，直接拆分为子pattern处理
    start=0
    if len(ors)>0:#包含与根同层的或符号，直接拆分处理
        for i in range(len(ors)):
            end=ors[i]
            part=analysePattern(pattern[start:end],rootDepth,False)#递归了，
            start=end+1#|位置的下一个位置开始
            result.extend(part)#因为result和part同级，我们用extend
    else:#此时没有最外的|,此时没有同级的，只有先后级别
        all_xianhou_patt = real_xianhou(pattern)






        depth=rootDepth
        stacks=[]#存放int的栈，把<和[的位置记录下来
        hasPattern=False#是否包含标记符| <> []
        necessary_Start=0#标记形如"歌[曲]"或"[歌]曲"的情况，他们等同于"<歌>[曲]"或"[歌]<曲>"
        #"<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>"
        for i in range(length):#开始遍历pattern的string
            c=pattern[i]
            if c=='<'or c=='[':
                if depth==rootDepth:
                    if i>necessary_Start:
                        part=analysePattern(pattern[necessary_Start:i-necessary_Start],depth,False)
                        result=contentMerge(result,part)
                hasPattern=True
                depth+=1#深度+1
                stacks.append(i)
            elif c=='>':
                depth-=1
                if depth==rootDepth:
                    necessary_Start=i+1
                index=stacks[-1]
                stacks.pop()
                if depth==rootDepth:
                    part=analysePattern(pattern[index+1:i-index-1],depth+1,False)
                    result=contentMerge(result,part)
            elif c==']':
                depth-=1
                if depth==rootDepth:
                    necessary_Start=i+1
                index=stacks[-1]
                stacks.pop()
                if depth==rootDepth:
                    part=analysePattern(pattern[index+1:i-index-1],depth,True)
                    result=contentMerge(result,part)
        if not hasPattern:
            result.append(pattern)
        else:
            if necessary_Start<len(pattern):
                part=analysePattern(pattern[necessary_Start:len(pattern)-necessary_Start],depth,False)
                result=contentMerge(result,part)
    return result
def isMatch(set,query):
    '''
    :param set: string_list
    :param query: string
    :return: bool
    '''
    for i in range(len(set)):
        if query==set[i]:return True
    return False

inputs = "<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>"
all_ex=analysePattern(inputs,0,False)
print(all_ex)




