"_______________ВАРИАНТ 8___________________"

"_______________ТРАССИРОВКА СОРТИРОВКи STOOGE SORT РАЗМЕРНОСТИ 5, 10, 15___________________"

import random
import time
import matplotlib.pyplot as plt


def stooge_sort(arr, start, end):
    if start >= end:
        return

    if arr[start] > arr[end]:
        print(f"Поменяли местами элементы {arr[start]} и {arr[end]}: {arr}")
        arr[start], arr[end] = arr[end], arr[start]

    if end - start + 1 >= 3:
        third = (end - start + 1) // 3
        stooge_sort(arr, start, end - third)
        stooge_sort(arr, start + third, end)
        stooge_sort(arr, start, end - third)



n_massiv = [5, 10, 15]
times = []
for launch in range(0, len(n_massiv)):
    vector = random.sample(range(1, n_massiv[launch] + 1), n_massiv[launch])
    start_time = time.time()
    massiv = stooge_sort(vector, 0, len(vector) - 1)
    print(f"Итог: {vector}\n")
    end_time = time.time()
    times.append(end_time - start_time)
plt.plot(n_massiv, times, marker='o', markersize=5, color='blue')
plt.plot(n_massiv, times)
plt.xlabel(f"Размер вектора (n): {n_massiv[launch]}")
plt.ylabel("Время выполнения (сек)")
plt.title("Зависимость времени выполнения от размера вектора")
plt.show()