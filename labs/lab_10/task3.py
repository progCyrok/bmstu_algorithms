#Задача о нахождении наименьшего пути

import numpy as np

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = np.array(graph, dtype=float)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph1 = [
    [0, 3, 8, np.inf, -4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, -5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0]
]

print("Пример 1:")
shortest_distances1 = floyd_warshall(graph1)
for row in shortest_distances1:
    print(row)



graph2 = [
    [0, 5, np.inf, 10],
    [np.inf, 0, 3, np.inf],
    [np.inf, np.inf, 0, 1],
    [np.inf, np.inf, np.inf, 0]
]


print("\nПример 2:")
shortest_distances2 = floyd_warshall(graph2)
for row in shortest_distances2:
   print(row)


graph3 = [
    [0, 1, 5],
    [1, 0, 2],
    [5, 2, 0]
]

print("\nПример 3:")
shortest_distances3 = floyd_warshall(graph3)
for row in shortest_distances3:
    print(row)

