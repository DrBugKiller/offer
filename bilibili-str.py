# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 19:30
# @Author  : DrMa
'''
数拼接,返回最大的
'''
def get_first_num(num):
    str_num=str(num)
    first_num=int(str_num[0])
    return first_num
def solution(num_list):
    num_list.sort(key=get_first_num,reverse=True)
    i=0
    res=[]
    while i<len(num_list):
        j=i+1
        val1=str(num_list[i])[0]
        while j<len(num_list):
            val2=str(num_list[j])[0]
            if val2!=val1:
                break
            else:
                j+=1
        res.append(num_list[i:j])
        i=j
    for i in range(len(res)):
        length=len(str(max(res[i])))
        first_num=str(int(str(res[i][0])[0]))
        temp=[str(x)+first_num*(length-len(str(x))) for x in res[i]]
        temp=[int(x) for x in temp]
        temp2=list(zip(res[i],temp))
        temp2.sort(key=lambda a:a[1],reverse=True)
        res[i]=[x[0]for x in temp2]
    res_final=''
    for i in res:
        for j in i:
            res_final+=str(j)
    return res_final
if __name__=='__main__':
    temp=list(map(int,input().split(',')))
    print(solution(temp))
