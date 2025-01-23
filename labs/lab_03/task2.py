class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return

        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next

    def delete_at_position(self, position):
        if position < 0:
            return

        if position == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        previous = None
        count = 0
        while current and count != position:
            previous = current
            current = current.next
            count += 1

        if current is None:
            return

        previous.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_length(self):
        """Возвращает длину списка."""
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

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current))
            current = current.next
        return " ".join(elements)


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("Исходный список:", my_list)  # Вывод: Исходный список: 1 -> 2 -> 3

my_list.reverse()
print("Перевернутый список:", my_list)  # Вывод: Перевернутый список: 3 -> 2 -> 1
