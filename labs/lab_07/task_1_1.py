from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self, start):
        visited = set()
        stack = []

        def dfs_util(node):
            visited.add(node)
            stack.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return stack

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def is_eulerian(self):
        for v in self.graph:
            if len(self.graph[v]) % 2 != 0:
                return False
        return True

    def find_euler_cycle(self):
        if not self.is_eulerian():
            return None

        temp_graph = {u: lst.copy() for u, lst in self.graph.items()}
        stack = []
        cycle = []

        start_vertex = next(iter(temp_graph))

        stack.append(start_vertex)

        while stack:
            u = stack[-1]

            if temp_graph[u]:
                v = temp_graph[u].pop()
                temp_graph[v].remove(u)
                stack.append(v)
            else:
                cycle.append(stack.pop())

        return cycle[::-1]




graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)
graph.add_edge(0, 4)

start_node = 1
print(f"Обход в глубину начиная с {start_node}:", graph.dfs(start_node))
print(f"Обход в ширину начиная с вершины {start_node}:", graph.bfs(start_node))
euler_cycle = graph.find_euler_cycle()

if euler_cycle:
    print("Эйлеров цикл найден:", euler_cycle)
else:
    print("Эйлеров цикл не существует.")
