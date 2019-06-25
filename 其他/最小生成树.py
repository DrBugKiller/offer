# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 10:25
# @Author  : DrMa
class Graph(object):
    def __init__(self, maps):
        self.maps = maps#就是个二维数组
        self.nodenum = self.get_nodenum()#顶点数
        self.edgenum = self.get_edgenum()#边的数量

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        #遍历一个三角矩阵
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count

    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])  # 按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a: a[2])  # 已经排好序的边集合

        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res

    def prim(self):
        # res = []
        # if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
        #     return res
        res = []#初始化结果,是个list
        # 将顶点分为两部分,一部分是已选顶点,另一部分是候选顶点.
        seleted_node = [0]#初始化已选顶点,我们让0顶点作为第一个已选顶点.
        candidate_node = [i for i in range(1, self.nodenum)]
        #初始化候选顶点,让1到顶点数-1的
        while len(candidate_node) > 0:#只要候选顶点list中有顶点
            begin, end, minweight = 0, 0, 9999#初始化头顶点,尾顶点,最小权值
            for i in seleted_node:#从已选顶点list中遍历,作为头顶点
                for j in candidate_node:#从候选顶点list中遍历,作为尾顶点
                    if self.maps[i][j] < minweight:#这个条件是表明顶点之间有路子可走,并且经过每次循环路子越来越短.
                        minweight = self.maps[i][j]#每次都更新,因为我们要找最小的边
                        begin = i#更新begin和end
                        end = j
            #上边的这两个循环,就是从已选list中
            res.append([begin, end, minweight])#我们把最小的一条边放到res中
            seleted_node.append(end)#我们把尾顶点加入到已选的list中.
            candidate_node.remove(end)#我们把尾顶点从候选list中删除.
        return res

max_value = 9999
row0 = [0, 7, max_value, max_value, max_value, 5]
row1 = [7, 0, 9, max_value, 3, max_value]
row2 = [max_value, 9, 0, 6, max_value, max_value]
row3 = [max_value, max_value, 6, 0, 8, 10]
row4 = [max_value, 3, max_value, 8, 0, 4]
row5 = [5, max_value, max_value, 10, 4, 0]
maps = [row0, row1, row2, row3, row4, row5]
#通过一个链接矩阵来表示一个图，也就是二维数组。
graph = Graph(maps)
print('邻接矩阵为\n%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
print('------最小生成树prim算法')
print(graph.prim())

