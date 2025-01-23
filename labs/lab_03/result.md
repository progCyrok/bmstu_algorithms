<!-- #region editable=true slideshow={"slide_type": ""} -->
## Лабораторная работа № 3 Линейные списки (Linked list)
***Выполнил***: Камалов Ринат,  ***Группа***: ИУ10-36
<!-- #endregion -->

### **Цель работы** 

Изучение структуры данных «Линейные списки», а также основных операций над ними.

### 1. Описание задачи
Задания на лабораторную работу
1. Последовательно реализовать 6 версий линейного односвязного списка.

2. Реализовать метод reverse для «переворота» линейного списка.

3. Реализовать метод sort для сортировки линейного списка на месте.

4. Реализовать индивидуальные задание.

5. Опционально: реализовать один из видов циклов, рассмотренных на лекции.
6. 

### Задания на лабораторную работу

#### **1.  Последовательно реализовать 6 версий линейного односвязного списка.**


```python
#1
#Версия 1: Базовая реализация с минимальной функциональностью

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

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

my_list = LinkedList()
my_list.append(1)
my_list.append(6)
my_list.append(3)
my_list.display()  # Вывод: 1 6 3

```

```python
#Версия 2: Добавление prepend и delete
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

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

my_list = LinkedList()
my_list.append(6)
my_list.append(2)
my_list.append(3)
my_list.prepend(0)
my_list.delete(2)
my_list.display()  # Вывод: 0 6 3

```

```python
#Версия 3: Добавление search и get_length
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

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))



my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(f"Длина списка: {my_list.get_length()}") # Вывод: Длина списка: 3
print(f"Поиск элемента 2: {my_list.search(2)}") # Вывод: Поиск элемента 2: True
print(f"Поиск элемента 4: {my_list.search(4)}") # Вывод: Поиск элемента 4: False

```

```python
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

```

```python
#Версия 5: Улучшенное удаление (удаление по значению или позиции)
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
            return  # Элемент не найден

        previous.next = current.next
        current = None

    def delete_at_position(self, position):
        if position < 0:
            return

        current = self.head
        if position == 0:
            if current:
                self.head = current.next
                current = None
            return

        previous = None
        count = 0
        while current and count != position:
            previous = current
            current = current.next
            count += 1

        if current is None:
            return  # Позиция вне диапазона

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

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.delete_at_position(1)
my_list.display()  # Вывод: 1 3

```

```python
#Версия 6: Использование __str__ для удобного вывода и более Pythonic стиль.
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
print(my_list)  # Вывод: 1 -> 2 -> 3  (Используем __str__)
my_list.delete_at_position(1)
print(my_list)  # Вывод: 1 -> 3

```

#### **2. Реализовать метод reverse для «переворота» линейного списка.**


```python
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


```

#### **3. Реализовать метод sort для сортировки линейного списка на месте.**



```python
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
    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, sorted_head, new_node):
        if not sorted_head or new_node.data <= sorted_head.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current))
            current = current.next
        return " ".join(elements)


my_list = LinkedList()
my_list.append(3)
my_list.append(1)
my_list.append(4)
my_list.append(1)
my_list.append(5)
my_list.append(9)
my_list.append(2)
my_list.append(6)

print("Исходный список:", my_list) # Вывод: Исходный список: 3 1 4 1 5 9 2 6
my_list.sort()
print("Отсортированный список:", my_list) # Вывод: Отсортированный список: 1 1 2 3 4 5 6 9


```

#### **4. Реализовать индивидуальные задание.**


```python
def split_list(data_list):

  positive_list = []
  negative_list = []
  for item in data_list:
    if item > 0:
      positive_list.append(item)
    elif item < 0:
      negative_list.append(item)
  return positive_list, negative_list

# Example usage
my_list = [1, -2, 3, -4, 0, 5, -6]
positive_nums, negative_nums = split_list(my_list)

print("Исходный список:", my_list) # Вывод: Исходный список: [1, -2, 3, -4, 0, 5, -6]
print("Положительные числа:", positive_nums) # Вывод: Положительные числа: [1, 3, 5]
print("Отрицательные числа:", negative_nums) # Вывод: Отрицательные числа: [-2, -4, -6]


```

#### **5. Опционально: реализовать один из видов циклов, рассмотренных на лекции.**



```python
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


```

### **Контрольные вопросы**

1. Что такое динамическая структура данных?
Динамическая структура данных — это структура, размер которой может изменяться во время выполнения программы. В отличие от статических структур данных (например, массивов), которые имеют фиксированный размер, динамические структуры позволяют добавлять и удалять элементы по мере необходимости, что делает их более гибкими. Примеры динамических структур данных включают списки, стеки, очереди, деревья и графы.

2. Что такое список?
Список — это структура данных, которая хранит коллекцию элементов в определенном порядке. Каждый элемент списка может содержать данные, а также ссылку на следующий элемент (в односвязных списках) или на предыдущий и следующий элементы (в двусвязных списках). Списки позволяют легко добавлять, удалять и изменять элементы, а также осуществлять итерацию по их содержимому.

3. Какие виды списков существуют?
Существуют несколько видов списков, среди которых:

•	Односвязный список: Каждый элемент (узел) содержит данные и ссылку на следующий элемент.
•	Двусвязный список: Каждый элемент содержит данные, ссылку на следующий и предыдущий элементы.
•	Циклический список: В этом списке последний элемент ссылается на первый, образуя замкнутый цикл. Могут быть как односвязные, так и двусвязные циклические списки.
•	Массив списков: Список, элементы которого представляют собой массивы, где каждый элемент может иметь переменный размер.

4. Какие основные операции выполняются над списком?
Основные операции, выполняемые над списком, включают:

•	Добавление элемента: Вставка элемента в начало, конец или в указанную позицию списка.
•	Удаление элемента: Удаление элемента из начала, конца или по значению/индексу.
•	Поиск элемента: Поиск элемента по значению или индексу.
•	Изменение элемента: Изменение значения элемента по индексу или значению.
•	Итерация по элементам: Перебор всех элементов списка.

5. Дать определение циклического списка.
Циклический список — это структура данных, в которой последний элемент списка ссылается на первый элемент, образуя замкнутый цикл. Это позволяет бесконечно обходить список без необходимости возвращаться к его началу. В циклических списках не существует четко определенного начала или конца, что делает их полезными для определенных задач, таких как реализация очередей или циклических буферов.

6. Классификация циклических списков.
Циклические списки могут быть классифицированы следующим образом:

•	Циклический односвязный список: Каждый элемент содержит данные и ссылку только на следующий элемент, при этом последний элемент ссылается на первый.
•	Циклический двусвязный список: Каждый элемент содержит данные, ссылку на следующий элемент и ссылку на предыдущий элемент. При этом последний элемент ссылается на первый, а первый — на последний.

7. Какие основные операции выполняются над циклическим списком?
Основные операции над циклическим списком включают:

•	Добавление элемента: Вставка нового элемента в циклический список (в начало, конец или в указанную позицию).
•	Удаление элемента: Удаление элемента по значению или индексу.
•	Поиск элемента: Поиск элемента по значению или индексу.
•	Изменение элемента: Изменение значения элемента по индексу или значению.
•	Итерация по элементам: Перебор всех элементов списка, начиная с любого элемента.
•	Переворот списка: Изменение порядка следования элементов в списке.