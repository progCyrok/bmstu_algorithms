"_______________ВАРИАНТ 8___________________"

"_______________СОРТИРОВКА ЧЁТ-НЕЧЁТ___________________"

import random
import time
import matplotlib.pyplot as plt


def odd_even(data):
    start_time = time.time()
    n = len(data)
    isSorted = False
    while isSorted == False:
        isSorted = True
        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                isSorted = False

        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                isSorted = False

    end_time = time.time()
    end = end_time - start_time
    print(end)
    return [data, end_time - start_time]


n_massiv = [1000, 2000, 5000, 10000]
times = []
for launch in range(0, len(n_massiv)):
    vector = sorted(range(1, n_massiv[launch]))
    # vector = random.sample(range(1, n_massiv[launch] + 1), n_massiv[launch])
    massiv = odd_even(vector)
    times.append(massiv[1])
plt.plot(n_massiv, times, marker='o', markersize=5, color='blue')
plt.plot(n_massiv, times)
plt.xlabel(f"Размер вектора (n): {n_massiv[launch]}")
plt.ylabel("Время выполнения (сек)")
plt.title("Зависимость времени выполнения от размера вектора")
plt.show()
