def bfs(g, s):
    v = set()
    q = [s]

    while q:
        c = q.pop(0)
        if c not in v:
            print(c, end=' ')
            v.add(c)
            q.extend(n for n in g[c] if n not in v)

graph = {
    'A': ['F', 'C'],
    'B': ['C', 'G', 'E'],
    'C': ['D', 'F', 'G'],
    'D': ['B'],
    'E': ['E'],
    'F': ['D'],
    'G': ['A']
}


start_node = 'A'
print(f"BFS starting from node {start_node}:")
bfs(graph, start_node)
