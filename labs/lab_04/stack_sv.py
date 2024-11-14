class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def __str__(self):
        temp = self.top
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return ' '.join(map(str, result))



s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s)  # Ожидается: 30 20 10

print(s.peek())  # Ожидается: 30

print(s.pop())  # Ожидается: 30
print(s)  # Ожидается: 20 10

print(s.pop())  # Ожидается: 20
print(s.pop())  # Ожидается: 10

print(s.is_empty())  # Ожидается: True

s.pop() # Ожидвется ошибка
