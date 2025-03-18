import heapq

def prim_algorithm(graph, start_node):
    mst = []
    visited = set()
    min_heap = [(0, start_node, None)]
    total_cost = 0

    while min_heap:
        cost, current_node, previous_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)
        total_cost += cost

        if previous_node is not None:
            mst.append((previous_node, current_node, cost))

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, neighbor, current_node))

    return mst, total_cost


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)],
}

start_node = 'A'
mst, total_cost = prim_algorithm(graph, start_node)

print("Árvore Geradora Mínima:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (custo: {edge[2]})")
print(f"Custo total: {total_cost}")
