INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
                pred[i][j] = i  # Set the predecessor

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]  # Update the predecessor

    return dist, pred

g = {
    0: {2: 4, 1: 5},
    1: {0: 2},
    2: {1: 4, 3: 2},
    3: {2: 2}
}

shortest_distances, predecessors = floyd_warshall(g)

print("Shortest Paths Matrix:")
for row in shortest_distances:
    print(row)

start_node, end_node = 0, 3
shortest_path = [end_node]
while predecessors[start_node][end_node] is not None:
    shortest_path.insert(0, predecessors[start_node][end_node])
    end_node = predecessors[start_node][end_node]

print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
