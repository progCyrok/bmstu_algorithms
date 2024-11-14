class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста. Невозможно удалить элемент.")
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            raise Exception("Очередь пуста. Невозможно получить элемент на начале очереди.")
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        temp = self.front
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return ' '.join(map(str, result))

queue = Queue()


queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue) # Ожидается [1, 2, 3]

queue.dequeue()

print(queue) # Ожидается [2, 3]

print(queue.peek()) # Ожидается 2

queue.enqueue(4)
queue.enqueue(5)

print(queue.size()) # Ожидается 4

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()  # Ожидается ошибка

