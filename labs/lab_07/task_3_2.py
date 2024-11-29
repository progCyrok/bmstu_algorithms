import heapq

def dijkstra(graph, start, goal):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    predecessors = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == goal:
            path = []
            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = predecessors.get(current_vertex)
            return distances[goal], path

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return float('inf'), []

graph = {
    1: {2: 1, 3: 13, 4: 6, 6: 11, 7: 15},
    2: {1: 1, 3: 5, 4: 5, 5: 1},
    3: {1: 13, 2: 5, 8: 19},
    4: {1: 6, 2: 5, 5: 3, 6: 2},
    5: {2: 1, 4: 3, 6: 8, 8: 12},
    6: {1: 11, 4: 2, 5: 8, 7: 3},
    7: {1: 15, 6: 3, 8: 1},
    8: {3: 19, 5: 12, 7: 1}
}

start_node = 7
end_node = 3

distance, path = dijkstra(graph, start_node, end_node)

if distance == float('inf'):
    print(f"Пути между вершинами {start_node} и {end_node} нет.")
else:
    print(f"Кратчайший путь между вершинами {start_node} и {end_node}: {path}")
    print(f"Длина кратчайшего пути: {distance}")
