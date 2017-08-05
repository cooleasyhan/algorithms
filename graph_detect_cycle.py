from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

    def dfs_util(self, v, visted):
        if v not in visted:
            visted.append(v)

        for _v in self.adj_list[v]:
            if _v not in visted:
                self.dfs_util(_v, visted)

    def dfs(self, v):
        visted = []
        self.dfs_util(v, visted)
        print(visted)
    
    def cycle_util(self, v, visted, rec_stack):
        visted[v] = True
        rec_stack[v] = True
        for _v in self.adj_list[v]:
            if visted[_v] == False:
                if self.cycle_util(_v, visted, rec_stack) == True:
                    return True
            elif rec_stack[_v] == True:
                return True
        
        rec_stack[_v] = False
        return Falses

    def is_cycle(self):
        visted = [False] * self.V
        rec_stack = [False] * self.V
        for v in range(self.V):
            if self.cycle_util(v, visted, rec_stack) == True:
                return True

        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(0)
print(g.is_cycle())