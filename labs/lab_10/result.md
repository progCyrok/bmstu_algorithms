## Лабораторная работа № 10 (Криптоалгоритмы)
***Выполнил***: Камалов Ринат,  ***Группа***: ИУ10-36

### **Цель работы**
Реализовать все алгориты не реализованные алгоримтмы в лекции 14.

### **Задача о рюкзаке с возможностью дробить предметы**
```python

#Задача о рюкзаке с возможностью дробить предметы

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost_per_weight = value / weight


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.cost_per_weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.cost_per_weight * capacity
            break

    return total_value


items = [
    Item(value=60, weight=10),
    Item(value=100, weight=20),
    Item(value=120, weight=30)
]

capacity = 50

max_value = fractional_knapsack(items, capacity)
print(f"Максимальная стоимость, которую можно получить в рюкзаке: {max_value}")


```

### **Задача о покрытии отрезками**
```python

#Задача о покрытии отрезками

def min_segments_to_cover(target_segment, segments):
    segments.sort(key=lambda x: x[1])

    target_start, target_end = target_segment
    covered_until = target_start
    segments_used = 0
    i = 0

    while covered_until < target_end:
        best_next_cover = covered_until
        while i < len(segments) and segments[i][0] <= covered_until:
            best_next_cover = max(best_next_cover, segments[i][1])
            i += 1

        if best_next_cover == covered_until:
            return -1

        covered_until = best_next_cover
        segments_used += 1

    return segments_used


target_segment = (1, 5)
segments = [(1, 2), (2, 3), (3, 4), (0, 1), (4, 5), (1, 3)]

result = min_segments_to_cover(target_segment, segments)
print(f"Минимальное количество отрезков для покрытия: {result}")

```

### **#Задача о нахождении наименьшего пути**
```python

##Задача о нахождении наименьшего пути

import numpy as np

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = np.array(graph, dtype=float)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph1 = [
    [0, 3, 8, np.inf, -4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, -5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0]
]

print("Пример 1:")
shortest_distances1 = floyd_warshall(graph1)
for row in shortest_distances1:
    print(row)



graph2 = [
    [0, 5, np.inf, 10],
    [np.inf, 0, 3, np.inf],
    [np.inf, np.inf, 0, 1],
    [np.inf, np.inf, np.inf, 0]
]


print("\nПример 2:")
shortest_distances2 = floyd_warshall(graph2)
for row in shortest_distances2:
   print(row)


graph3 = [
    [0, 1, 5],
    [1, 0, 2],
    [5, 2, 0]
]

print("\nПример 3:")
shortest_distances3 = floyd_warshall(graph3)
for row in shortest_distances3:
    print(row)



```


### **#Генерация разбиений множества**
```python

#Генерация разбиений множества

def partitions(s):
    if not s:
        return [[]]

    result = []
    first_elem = s[0]

    for partition in partitions(s[1:]):
        for i in range(len(partition)):
            new_partition = partition[:i] + [[first_elem] + partition[i]] + partition[i+1:]
            result.append(new_partition)

        result.append([[first_elem]] + partition)

    return result

input_set = [1, 2, 3]
partitions_result = partitions(input_set)

for part in partitions_result:
    print(part)


```

### **Контрольные вопросы**

 1. Что такое динамическое программирование и когда его следует использовать?
Динамическое программирование (DP) — это метод решения сложных задач, 
который разбивает их на более простые подзадачи, решает их и запоминает (кэширует) результаты для будущего использования. 
Это позволяет избежать повторного решения одних и тех же подзадач, что значительно ускоряет процесс. 
Динамическое программирование следует использовать, когда задача может быть разбита на перекрывающиеся подзадачи и имеет 
свойства оптимальной подструктуры.

 2. Приведите пример задачи, которая может быть решена с помощью динамического программирования.
Один из классических примеров — задача о нахождении n-го числа Фибоначчи,
где каждое число является суммой двух предыдущих. 
Это можно решить с помощью динамического программирования, сохраняя промежуточные результаты.

 3. Как работает алгоритм Фибоначчи с использованием динамического программирования?
Алгоритм вычисления n-го числа Фибоначчи с использованием динамического программирования может выглядеть следующим образом:
```python
def fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

4. Что такое метод "разделяй и властвуй" и как он отличается от динамического программирования?
Метод "разделяй и властвуй" (Divide and Conquer) — это подход, 
который разбивает задачу на несколько подзадач меньших размеров, 
решает каждую из них рекурсивно и комбинирует результаты для решения оригинальной задачи. 
В отличие от динамического программирования, 
где подзадачи перекрываются и результаты кэшируются для оптимизации, 
в методе "разделяй и властвуй" подзадачи обычно независимы. 
Примером этого метода является алгоритм быстрой сортировки.

5. Каков алгоритм решения задачи о рюкзаке (0/1)?
Задача о рюкзаке (0/1) — это задача о том, как выбрать набор предметов с ограничениями по весу и стоимости, 
чтобы максимизировать общую стоимость. 
Алгоритм динамического программирования для этой задачи может быть реализован так:

```python
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
```

6. Как решать задачу о длине наибольшей возрастающей подпоследовательности?
Задача о длине наибольшей возрастающей подпоследовательности (ЛАП) может быть решена
с использованием динамического программирования. Алгоритм такой:

```python   
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

Каждый элемент массива `dp` хранит длину наибольшей возрастающей подпоследовательности, заканчивающейся на соответствующем элементе исходного массива.

### 7. В чем заключается метод градиентного спуска?
Метод градиентного спуска — это оптимизационный алгоритм, используемый для минимизации функции. 
Он работает, вычисляя градиент функции в текущей точке и перемещаясь в направлении, противоположном этому градиенту. 
С каждым шагом алгоритм обновляет свои параметры, чтобы находиться ближе к минимуму целевой функции. 
Это широко используется в машинном обучении для обучения моделей.

### 8. Что такое жадные алгоритмы и когда их следует использовать?
Жадные алгоритмы — это подход, при котором на каждом этапе принимается локально оптимальное решение,
не задумываясь о глобальном оптимуме. 
Жадные алгоритмы следует использовать, 
когда задача имеет свойства, позволяющие однозначно гарантировать, что л