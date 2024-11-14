"_______________ВАРИАНТ 12___________________"

"_______________СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ___________________"

import random
import time
import matplotlib.pyplot as plt


def arif_mean(u):
    result = 0
    for i in u:
        result += i
    return result//len(u)

for launch in range(1, 6):
  values = []
  n_list = []
  times = []
  for value in range(1, 10 ** 5 * 12, 100 * 12):
    values.append(value)
  for random_ in range(1, 12):
    n = random.choice(values)
    n_list.append(n)
  n_list.sort()
  for score in n_list:
    vector = list(range(1, score))
    start_time = time.time()
    arif_mean(vector)
    end_time = time.time()
    times.append(end_time - start_time)
  plt.plot(n_list, times)
  plt.xlabel("Размер вектора (n)")
  plt.ylabel("Время выполнения (сек)")
  plt.title("Зависимость времени выполнения от размера вектора")
  plt.show()
