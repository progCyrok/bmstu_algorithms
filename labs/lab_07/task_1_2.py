class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_valid(self, v, pos, path):
        if self.adj[path[pos - 1]].count(v) == 0:
            return False

        if v in path:
            return False

        return True

    def hamiltonian_cycle_util(self, path, pos):
        if pos == self.V:
            if path[pos - 1] in self.adj[path[0]]:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.is_valid(v, pos, path):
                path[pos] = v

                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True

                path[pos] = -1

        return False

    def hamiltonian_cycle(self):
        path = [-1] * self.V
        path[0] = 0

        if not self.hamiltonian_cycle_util(path, 1):
            print("Гамильтонова цикл не существует")
            return False

        self.print_solution(path)
        return True

    def print_solution(self, path):
        print("Найден гамильтонов цикл:")
        for i in range(len(path)):
            print(path[i], end=" ")
        print(path[0])


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.hamiltonian_cycle()
