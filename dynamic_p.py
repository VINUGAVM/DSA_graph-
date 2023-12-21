import heapq

def top_sort(a):
    in_deg = {node: 0 for node in a}
    for node in a:
        for neighbor in a[node]:
            in_deg[neighbor] += 1

    pq = [node for node in a if in_deg[node] == 0]
    heapq.heapify(pq)

    topo_order = []

    while pq:
        curr_node = heapq.heappop(pq)
        topo_order.append(curr_node)

        for neighbor in a[curr_node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                heapq.heappush(pq, neighbor)

    return topo_order

def shortest(a, start):
    topo_order = top_sort(a)
    dist = {node: float('infinity') for node in a}
    dist[start] = 0
    pred = {node: None for node in a}

    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > dist[curr_node]:
            continue

        for neighbor, weight in a[curr_node].items():
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                pred[neighbor] = curr_node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, pred

def print_shortest_paths(start, distances, predecessors):
    print("Shortest distances from", start + ":")
    for node, d in distances.items():
        print(f"To {node}: {d}")

    print("\nShortest paths from", start + ":")
    for node in predecessors:
        path = []
        curr_node = node
        while curr_node is not None:
            path.insert(0, curr_node)
            curr_node = predecessors[curr_node]
        print(f"To {node}: {path}")

# Example usage

a = {
    'A': {'B': 20, 'C': 10},
    'B': {'A': 30, 'C': 40, 'D': 73},
    'C': {'A': 12, 'B': 53, 'D':13},
    'D': {'B': 25, 'C': 61}
}



start_node = 'A'
distances, predecessors = shortest(a, start_node)
print_shortest_paths(start_node, distances, predecessors)
