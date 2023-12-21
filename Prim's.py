import heapq

class Graph:
    def __init__(self):
        self.g = {}

    def add_edge(self, u, v, w):
        if u not in self.g:
            self.g[u] = []
        if v not in self.g:
            self.g[v] = []
        self.g[u].append((v, w))
        self.g[v].append((u, w))

    def prim(self, start):
        visited = set()
        min_heap = [(0, start)]
        mst = []

        while min_heap:
            wt, n = heapq.heappop(min_heap)

            if n not in visited:
                visited.add(n)
                mst.append((n, wt))

                for nbr, e_wt in self.g[n]:
                    if nbr not in visited:
                        heapq.heappush(min_heap, (e_wt, nbr))

        return mst

graph = Graph()
graph.add_edge('A', 'B', 20)
graph.add_edge('A', 'D', 30) 
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 15)
graph.add_edge('C', 'D', 5)

start_node = 'A'
min_spanning_tree = graph.prim(start_node)

print("Minimum Spanning Tree:")
for edge in min_spanning_tree:
    print(f"{start_node} - {edge[0]}: {edge[1]}")
