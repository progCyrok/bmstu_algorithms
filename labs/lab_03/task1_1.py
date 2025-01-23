#1
#Версия 1: Базовая реализация с минимальной функциональностью

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

my_list = LinkedList()
my_list.append(1)
my_list.append(6)
my_list.append(3)
my_list.display()  # Вывод: 1 6 3
