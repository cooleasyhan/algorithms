"""
http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/
"""
import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def get_min_vertex(self, dist, spt):
        min_weight = sys.maxsize
        min = sys.maxsize
        index = -1
        for i in range(self.V):
            if i not in spt and dist[i] < min:
                index = i
                min = dist[i]

        return index

    def dijkstra(self, src):
        spt = []
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        current = src
        while len(spt) < self.V:
            u = self.get_min_vertex(dist, spt)
            spt.append(u)
            for v, weight in enumerate(self.graph[u]):
                if weight == 0:
                    continue
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        print(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
