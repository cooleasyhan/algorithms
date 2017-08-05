
"""
图主要包含两部数据：
    点（vertices or nodes)
    线 （edge)
实现方式主要有两个：
    邻接矩阵 (Adjacency Matrix)
    邻接表数组（邻接链表）(Adjacency List)
查询算法：
    BFS：
        1. 利用数组记录是否已经遍历
        2. 利用先进先出队列遍历
    DFS
"""
#%%
from collections import defaultdict, deque
from pprint import pformat, pprint
import random


class AdjacencyListGraph:
    def __init__(self, v):
        self.v = v  # 顶点数
        self.adj_list = defaultdict(list)  # 邻接数组，每个点一个列表

    def add_edge(self, src, desc):
        if desc not in self.adj_list[src]:
            self.adj_list[src].append(desc)

    def __str__(self):
        return pformat(self.adj_list)

    def bfs(self, v):
        visted = []
        queue = deque()
        queue.append(v)
        while queue:
            current = queue.popleft()
            if current not in visted:
                visted.append(current)
                queue.extend(self.adj_list[current])
        return visted

    def dfs_utils(self, v, visted):
        visted.append(v)

        for _v in self.adj_list[v]:
            if _v not in visted:
                self.dfs_utils(_v, visted)

    def dfs(self, v):
        visted = []

        self.dfs_utils(v, visted)

        return visted


class AdjacencyMatrixGraph:
    def __init__(self, v):
        self.adj_list = [0] * v
        for i in range(v):
            self.adj_list[i] = [0] * v

    def add_edge(self, src, desc):
        self.adj_list[src][desc] = 1

    def __str__(self):
        return pformat(self.adj_list)

    def bfs(self, v):
        visted = []
        queue = deque()
        queue.append(v)
        while queue:
            current = queue.popleft()
            if current not in visted:
                visted.append(current)
                for idx, data in enumerate(self.adj_list[current]):
                    if data == 1:
                        queue.append(idx)
        return visted

    def dfs_utils(self, v, visted):
        visted.append(v)

        for idx, _v in enumerate(self.adj_list[v]):
            if _v == 1:
                if idx not in visted:
                    self.dfs_utils(idx, visted)

    def dfs(self, v):
        visted = []
        self.dfs_utils(v, visted)
        return visted


Graph = AdjacencyListGraph

#%%


def main():
    for i in [AdjacencyListGraph, AdjacencyMatrixGraph]:
        print(i)
    for GraphClass in [AdjacencyListGraph, AdjacencyMatrixGraph]:
        g = GraphClass(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        print(str(g))

        print(g.bfs(2))
        print(g.dfs(2))


if __name__ == '__main__':
    main()
