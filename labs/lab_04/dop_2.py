class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top >= self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[self.top]

    def get_size(self):
        return self.top + 1

    def __str__(self):
        return str([self.items[i] for i in range(self.top + 1)])


def postfix(example: str):
    stack = Stack()
    for char in example:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
    return stack.pop()

example = "23*54*+"
print(postfix(example)) # Ожидается 26
