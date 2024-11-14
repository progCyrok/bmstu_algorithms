<!-- #region editable=true slideshow={"slide_type": ""} -->
## Лабораторная работа № 4 (Cтек, Очередь, Дек)
***Выполнил***: Камалов Ринат,  ***Группа***: ИУ10-36
<!-- #endregion -->

### **Цель работы** 

Лабораторная работа посвящена расширенному изучению динамических структур данных: стек, очередь и дек. 
Она поможет студентам понять ключевые операции, работающие с этими структурами, а также научит реализовывать их как классы на базе массивов и связанных списков. 
Реализуя данные структуры, студенты углубят понимание работы памяти, особенностей доступа к данным и различных сфер применения каждой из структур данных.

Кроме того, лабораторная работа рассматривает задачи, такие как проверка корректности скобок и вычисление выражений в постфиксной записи, что позволяет закрепить теоретические знания на практике.

### 1. Описание задачи
Разработать и исследовать структуры данных стек, очередь и дек на языках программирования. 
Целью работы является реализация этих структур в виде классов и их применение для решения задач, например проверка сбалансированности скобок и вычисление выражений в постфиксной записи.

### 2. Входные и выходные данные

**Входные данные**:
- Для стеков и очередей: элементы для добавления или удаления (числа, строки или символы).
- Для задачи проверки скобок: строка, состоящая исключительно из символов скобок  `(`, `)`, `[`, `]`, `{`, `}`.
- Для задачи вычисления постфиксных выражений: строка с цифрами и знаками математических операций (`+`, `-`, `*`, `/`).

**Выходные данные**:
- Корректное выполнение операций добавления и удаления для каждой структуры данных.
- Результат проверки скобок: сбалансированы ли они или нет.
- Результат вычисления арифметических выражений в постфиксной записи.

### 3. Возможные ограничения и условия решения

- Стек и очередь на основе массива имеют ограничение по размеру массива, что требует управления переполнением.
- Стек и очередь на основе связного списка не имеют ограничений по количеству элементов, но зависят от доступного объема памяти.
- Для задачи проверки скобок корректность результата зависит от порядка, в котором закрываются все скобки.
- Постфиксные выражения должны быть корректными для правильного вычисления (например, деление на 0 недопустимо).
### 4. Анализ условий решения задачи

- Реализация операций над структурами данных (добавление, удаление, получение текущего элемента) не требует сложных условий при условии правильной реализации структур.
- Для проверки корректности скобок структура данных стек должна быть реализована в соответствии с требованиями, иначе могут возникнуть ошибки в последовательности закрытия.
- Для задач вычисления постфиксного выражения требуется наличие двух чисел в стеке перед каждой операцией; в противном случае выражение будет некорректным, и решение будет невозможно.
### 5. Ожидаемые результаты

Результатом выполнения работы является корректная реализация каждой структуры данных и успешное выполнение дополнительных задач с использованием этих структур. Успешная реализация обеспечит получение правильных ответов для задач на проверку скобок и вычисление выражений, что будет подтверждением корректности работы созданных структур данных.


### Задания на лабораторную работу

#### **1. Реализовать стек на основе массива**


```python
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

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)  # Ожидется [1, 2, 3]
print(stack.peek())  # Ожидется 3
print(stack.pop())   # Ожидется 3
print(stack)  # Ожидется [1, 2]

```

#### **2. Реализовать стек на основе связного списка**


```python
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


```

#### **3. Реализовать очередь на основе массива.**



```python
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

```

#### **4. Реализовать очередь на основе связного списка.**


```python
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
            print("Очередь пуста. Невозможно удалить элемент.")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            print("Очередь пуста. Невозможно получить элемент на начале очереди.")
            return None
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


```

#### **5. Реализовать дек на основе массива.**



```python
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

```


#### **6. Реализовать дек на основе связного списка**


```python
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


```

### Дополнительные задания

#### **Задание №1**


```python
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



def balance(example : str):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in example:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


example_true = "{[()]}"
print(balance(example_true)) # Ожидается True

example_false = "{[(})]"
print(balance(example_false)) # Ожидается False
```


#### **Задание №2**


```python
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
```

### **Контрольные вопросы**

1. **Что такое динамическая структура данных?**
   - Динамическая структура данных — это структура, которая может изменять свой размер во время выполнения программы. Она выделяет память по мере необходимости и освобождает ее, когда данные больше не нужны. Примеры включают связанные списки, деревья и графы.

2. **Что такое стек? Особенности выполнения операций со стеком.**
   - Стек — это линейная структура данных, работающая по принципу "последним пришел — первым вышел" (LIFO). В стеке операции выполняются только с одной стороны, называемой вершиной стека. Основные операции включают добавление элемента (push) и удаление элемента (pop) из вершины стека. Стек используется для временного хранения данных, поддерживает рекурсивные вызовы и управляет вложенностью в вычислениях.

3. **Что такое очередь? Особенности выполнения операций с очередью.**
   - Очередь — это линейная структура данных, работающая по принципу "первым пришел — первым вышел" (FIFO). В очереди добавление элемента происходит с одного конца (задний конец), а удаление — с другого (передний конец). Очередь используется, когда важен порядок обработки данных, например в управлении задачами, обработке запросов или моделировании реальных очередей.

4. **Что такое дек? Особенности выполнения операций с деком.**
   - Дек (двусторонняя очередь) — это структура данных, которая позволяет добавлять и удалять элементы с обоих концов. В отличие от обычной очереди, в деке операции вставки и удаления можно выполнять как с переднего, так и с заднего конца. Это делает дек гибким и подходящим для задач, где требуются доступ и изменения с обеих сторон, например в обработке последовательностей или управлении задачами.

5. **Основные операции со стеком.**
   - **Push:** добавление элемента на вершину стека.
   - **Pop:** удаление и возврат элемента с вершины стека.
   - **Peek (Top):** просмотр элемента на вершине стека без удаления.
   - **isEmpty:** проверка, пуст ли стек. 

