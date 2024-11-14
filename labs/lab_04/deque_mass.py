class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.items = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def add_front(self, item):
        if self.is_full():
            raise Exception("deque is full")
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item
        self.size += 1

    def add_rear(self, item):
        if self.is_full():
            raise Exception("deque is full")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise Exception("deque is empty")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def remove_rear(self):
        if self.is_empty():
            raise Exception("deque is empty")
        item = self.items[self.rear]
        self.items[self.rear] = None
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return item

    def get_front(self):
        if self.is_empty():
            raise Exception("deque is empty")
        return self.items[self.front]

    def get_rear(self):
        if self.is_empty():
            raise Exception("deque is empty")
        return self.items[self.rear]

    def get_size(self):
        return self.size

    def __str__(self):
        return str([self.items[(self.front + i) % self.capacity] for i in range(self.size)])

deque = Deque(5)
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque)  # Ожидается [0, 1, 2]
print(deque.remove_front())  # Ожидается 0
print(deque.remove_rear())   # Ожидается 2
print(deque)  #Ожидается [1]
