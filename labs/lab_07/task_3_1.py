import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == end:
            path = []
            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = previous_vertices[current_vertex]
            return distances[end], path

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return None

graph = {
    1: [(2, 8), (5, 11)],
    2: [(3, 15), (6, 9)],
    3: [(4, 2), (7, 1)],
    4: [(7, 6)],
    5: [(2, 3), (3, 11), (6, 10)],
    6: [(4, 1), (7, 3)],
    7: []
}

result = dijkstra(graph, 5, 7)

if result:
    distance, path = result
    print(f"Кратчайший путь от 5 до 7: {path}")
    print(f"Длина пути: {distance}")
else:
    print("Путь от 5 до 7 не существует.")


