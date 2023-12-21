import heapq

def dijkstra(g, beg):
    distances = {node: float('infinity') for node in g}
    distances[beg] = 0
    predecessors = {node: None for node in g}
    pq = [(0, beg)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in g[current_node].items():
            distance = current_distance + weight

            # Update distance and predecessor if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors

g = {
    'A': {'B': 10, 'C': 20},
    'B': {'A': 3, 'C': 70, 'D': 14},
    'C': {'A': 21, 'B': 2, 'D':14},
    'D': {'B':40, 'C': 33}
}


start_node = 'A'
distances, predecessors = dijkstra(g, start_node)

#printing the shortest distances 
for node in g:
    path = []
    current_node = node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    print(f"Shortest path from {start_node} to {node}: {path}, Distance: {distances[node]}")
