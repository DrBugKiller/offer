# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 19:00
# @Author  : DrMa
#现在知道牛牛自己的起点，在终点（出口）是所有可通行格子中的一个的情况下，设哪一个格子为终点，会导致牛牛要走出去的最小步数最大？
# 问题清楚多了……
# 从起点出发，BFS整个图，然后找距离最远的可通行点，作为答案，OVER。
# ——什么，50种步伐怎么办？
# ——对每个格子，把50种步伐都试过去啊！
#从给定起点（一定为'.'）
#按照给定的若干跳跃（可以跨过障碍，但不可以落在'x'上），到达任意一个'.'的最小步骤次数集合中，选择一个最大的！
m,n=[int(x) for x in input().split()]#six!
maps=[input() for i in range(m)]#['...', '...', '...']
#因为是字符串所以子表可以直接第二维可以用索引
x,y=[int(x) for x in input().split()]#起点坐标
k=int(input())
move=[[int(x) for x in input().split()] for i in range(k)]
#[[1, 0], [0, 1], [-1, 0], [0, -1]]
visit=[[True if maps[i][j]=="." else False for j in range(n)] for i in range(m)] #地牢地图的bool化
#此处的j是因为用的字符串，可以直接索引
#先写值，然后在写判断条件
N=sum([1 if visit[i][j] else 0 for i in range(m) for j in range(n)])#可行点个数,()小括号
def layer():
    if maps[x][y]=='x':
        return -1 #起点必须为'.'
    result,count=1,1
    visit[x][y]=False
    que=[[x,y]]#代表当前位置
    show_i=0
    while que:
        print('show_i',show_i)
        print(que)
        tmp=[] #存放下一层broadth的点
        for i,j in que:
            for ax,ay in move: #每一种走法遍历一遍
                nx,ny=ax+i,ay+j#nx,ny代表next_x，next_y
                # print(nx,ny)
                if 0<=nx<m and 0<=ny<n and maps[nx][ny]=='.'and visit[nx][ny]:#如果没有出界，并且是可通行. ，并且还没有走过
                    tmp.append([nx,ny])#更新当前位置
                    print(nx,' ',ny)
                    visit[nx][ny]=False
                    count=count+1
                if count==N: #所有点都遍历了一遍
                    return result
        que=tmp
        print(que)
        result+=1
        show_i+=1
    return -1
print(layer())