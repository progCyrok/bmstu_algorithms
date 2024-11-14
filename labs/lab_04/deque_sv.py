class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_rear(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def pop_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.head.value

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.tail.value

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return "[" + ", ".join(map(str, elements)) + "]"


deque = Deque()
deque.append_rear(1)
deque.append_rear(2)
deque.append_front(0)
print(deque)  # Ожидание [0, 1, 2]

print(deque.pop_front())  # 0
print(deque.pop_rear())  # 2
print(deque)  # Ожидание [1]
