#Версия 4: Добавление insert_after
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next
        current = None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Элемент с данными {prev_data} не найден.")

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

# Пример использования
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert_after(2, 4)
my_list.display()  # Вывод: 1 2 4 3