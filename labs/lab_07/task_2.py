class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print(f"Узел {node} добавлен.")
        else:
            print(f"Узел {node} уже существует.")

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            print(f"Узел {from_node} не существует.")
            return
        if to_node not in self.graph:
            print(f"Узел {to_node} не существует.")
            return
        self.graph[from_node].append(to_node)
        print(f"Ребро добавлено: {from_node} -> {to_node}")

    def display_graph(self):
        if not self.graph:
            print("Граф пуст.")
        else:
            for node, edges in self.graph.items():
                print(f"{node}: {', '.join(edges)}")


def main():
    graph = Graph()

    while True:
        print("\n---- Меню ----")
        print("1. Добавить узел")
        print("2. Добавить ребро")
        print("3. Показать граф")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            node = input("Введите имя узла: ")
            graph.add_node(node)
        elif choice == '2':
            from_node = input("Введите имя начального узла: ")
            to_node = input("Введите имя конечного узла: ")
            graph.add_edge(from_node, to_node)
        elif choice == '3':
            graph.display_graph()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


main()
