# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 20:24
# @Author  : DrMa
def solution(from_id,to_id):
    dict={}
    for id in from_id:
        if not id in dict:
            dict[id]=1
        else:
            dict[id]+=1
    id_count=list(dict.items())
    id_count.sort(key=lambda a:a[1],reverse=True)
    return id_count[0][0]
if __name__=='__main__':
    n=int(input())
    from_id=[]
    to_id=[]
    for _ in range(n):
        temp=input().split()
        from_id.append(temp[0])
        to_id.append(temp[1])
    print(solution(from_id,to_id))