class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, n1, n2):
        if n1 not in self.adj_list:
            self.adj_list[n1] = []
        self.adj_list[n1].append(n2)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

another_graph = Graph()

another_graph.add_edge('P', 'Q')
another_graph.add_edge('P', 'R')
another_graph.add_edge('Q', 'S')
another_graph.add_edge('Q', 'T')
another_graph.add_edge('R', 'T')
another_graph.add_edge('S', 'U')
another_graph.add_edge('T', 'U')
another_graph.add_edge('U', 'V')

print("DFS starting from node 'P':")
another_graph.dfs('P')
