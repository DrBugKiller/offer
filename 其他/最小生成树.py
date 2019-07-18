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
        #定义结果list
        res = []
        #定义退出条件,这两个
        if self.nodenum <= 0 or self.edgenum < self.nodenum - 1:
            return res
        #定义边list,我们把图中所有边加入里边
        edge_list = []
        #三角矩阵遍历图,条件是maps[i][j]<9999
        for i in range(self.nodenum):
            for j in range(i+1, self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])  #按[begin, end, weight]形式加入
        #排序
        edge_list.sort(key=lambda a: a[2])
        print(edge_list)
        #定义一个下标list,长度是顶点list,这个是个二维list,子元素是存放begin的点,如果没有end的点
        group = [[i] for i in range(self.nodenum)]
        #开始遍历所有边,从小到大遍历
        begin,end=0,0
        for edge in edge_list:
            for i in range(len(group)):
                #找到边的头顶点的下标,赋值给m
                if edge[0] in group[i]:
                    begin = i
                #找到边的尾顶点的小标,赋值给n
                if edge[1] in group[i]:
                    end = i
            #如果
            if begin != end: #如果m=n,那么说明m和n已经构成过边了.
                #结果里并入edge
                res.append(edge)
                #通过在group中操作,把头顶点和尾顶点放到一块,如果m=n,那么就是之前已经构造过边
                group[begin] = group[begin] + group[end]#这句话最为精妙
                group[end] = []
                print(edge)
                print(group)

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
            res.append([begin, end, minweight])#我们把最小的一条边放到res中.
            seleted_node.append(end)#我们把尾顶点加入到已选的list中.
            candidate_node.remove(end)#我们把尾顶点从候选list中删除.
        return res

def p_algorithm(maps,num_node):
    #自己写
    '''
    :param maps: 邻接矩阵
    :param num_node: 顶点数量
    :return: 生成树
    '''
    res=[]
    select_node=[0]
    candidate_node=[i for i in range(1,num_node)]

    while len(candidate_node)>0:
        minweight=9999
        begin=0
        end=0
        for i in select_node:
            for j in candidate_node:
                if maps[i][j]<minweight:
                    minweight = maps[i][j]
                    begin=i
                    end=j
        res.append([begin, end, minweight])
        select_node.append(end)#此处一定要注意,是append的尾顶点
        candidate_node.remove(end)
    return res

def k_algorithm(maps,num_node):
    res,edge_list=[],[]
    minweight=9999
    #得到所有的边
    for i in range(num_node):
        for j in range(i+1,num_node):
            if maps[i][j]<minweight:
                edge_list.append([i,j,maps[i][j]])
    #如果没有顶点, 或者图根本不能连通--边数小于顶点数-1, 直接退出不商量
    if num_node<=0 or len(edge_list)<num_node-1:
        return res
    #按照weight来排序,weight的对应位置是[2]
    edge_list.sort(key=lambda a:a[2])#注意lambda快速函数的写法,中间带有一个空格
    #group存放顶点,但是随着边的遍历,能连通的顶点放一块
    group=[[i] for i in range(num_node)]
    for edge in edge_list:
        begin,end=edge[0],edge[1]
        for i in range(len(group)):
            if begin in group[i]:
                begin=i
            if end in group[i]:
                end=i
        if begin!=end:
            res.append([begin,end,edge[2]])
            group[begin]=group[begin]+group[end]
            group[end]=[]
    return res

if __name__=='__main__':
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
    # print('邻接矩阵为\n%s' % graph.maps)
    # print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
    # print('------最小生成树kruskal算法------')
    # print(graph.kruskal())
    # print('------最小生成树prim算法')
    # print(graph.prim())
    res=p_algorithm(maps,6)
    print(res)
    # print(k_algorithm(maps,len(maps)))


