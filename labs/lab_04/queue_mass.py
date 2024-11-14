class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("Очередь переполнена. Невозможно добавить элемент:", item)
            return
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста. Невозможно удалить элемент.")
            return None
        item = self.queue.pop(0)
        return item

    def peek(self):
        if self.is_empty():
            print("Очередь пуста. Невозможно получить элемент на начале очереди.")
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

queue = Queue(max_size=5)


queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Текущая очередь:", queue.queue) # Ожидается [1, 2, 3]

queue.dequeue()

print("Текущая очередь:", queue.queue) # Ожидается [2, 3]

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print("Текущая очередь:", queue.queue) # Ожидается [2, 3, 4, 5, 6]

queue.enqueue(7) # Ожидается Ошибка

print("Текущая очередь:", queue.queue) # Ожидается [2, 3, 4, 5, 6]

print(queue.size()) # Ожидается 5
