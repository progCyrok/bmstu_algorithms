class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Указывает на себя
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def split_positive_negative(self):

        positive_list = CircularLinkedList()
        negative_list = CircularLinkedList()

        if not self.head:
            return positive_list, negative_list

        current = self.head
        first_node_data = current.data

        while True:  # Цикл по списку
            if current.data > 0:
                positive_list.insert(current.data)
            elif current.data < 0:
                negative_list.insert(current.data)

            current = current.next
            if current.data == first_node_data:
                break

        return positive_list, negative_list

    def display(self):
        if not self.head:
            print("Список пуст")
            return

        current = self.head
        first_node_data = current.data
        print("Список:", end=" ")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current.data == first_node_data:
                break
        print()



my_list = CircularLinkedList()
my_list.insert(1)
my_list.insert(-2)
my_list.insert(3)
my_list.insert(-4)
my_list.insert(0)
my_list.insert(5)
my_list.insert(-6)

print("Исходный циклический список:")
my_list.display()

positive_list, negative_list = my_list.split_positive_negative()

print("Циклический список положительных чисел:")
positive_list.display()

print("Циклический список отрицательных чисел:")
negative_list.display()
