# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 15:44
# @Author  : DrMa
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
def analysePattern(pattern,rootDepth,addEmpty):
    '''
    string: pattern
    int: rootDepth
    bool: addEmpty
    '''
    result=[]
    if addEmpty:#是否可选，如果可选，增加‘’，这是【】的针对方法
        result.append('')
    ors=[]#存储‘或’符号的位置
    length=len(pattern)
    depth=rootDepth
    for i in range(length):
        c = pattern[i]#char
        if c=='<'or c=='[':depth+=1
        elif c=='>' or c==']':depth-=1
        elif c=='|'and depth==rootDepth:ors.append(i)#与根同层的或符号，直接拆分为子pattern处理
    start=0
    if len(ors)>0:#包含与根同层的或符号，直接拆分处理
        for i in range(len(ors)):
            end=ors[i]
            part=analysePattern(pattern[start:end-start],rootDepth,False)#list part
            start=end+1
            result.append(part[0])
            result.append(part[-1])
    else:
        depth=rootDepth
        stacks=[]#存放int的栈
        hasPattern=False#是否包含标记符| <> []
        necessary_Start=0#标记形如"歌[曲]"或"[歌]曲"的情况，他们等同于"<歌>[曲]"或"[歌]<曲>"
        for i in range(length):
            c=pattern[i]
            if c=='<'or c=='[':
                if depth==rootDepth:
                    if i>necessary_Start:
                        part=analysePattern(pattern[necessary_Start:i-necessary_Start],depth,False)
                        result=contentMerge(result,part)
                hasPattern=True
                depth+=1
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
allExpress=analysePattern("<[播]放|来>{singer}的",0, False)
print('Print ALL Expression')
print(allExpress)
