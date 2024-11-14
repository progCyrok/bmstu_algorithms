import random
import numpy as np
import time
import matplotlib.pyplot as plt
N=11
num = 10**5 * N
step  = 100 * N
v_values = list(range(1, num + 1, step))
times_list = []
n_list= []

for i in range(1,N):
    n = random.choice(v_values)
    n_list.append(n)

n_list.sort()

for dimension in n_list:
    vector = np.random.rand(dimension)
    pr = 0
    start_time = time.time()
    for i in vector:
        pr *=i
    function_value = pr
    end_time = time.time()
    times_list.append(end_time - start_time)

plt.plot(n_list, times_list)
plt.xlabel("Размер вектора (n)")
plt.ylabel("Время выполнения (сек)")
plt.title("Зависимость времени выполнения от размера вектора")
plt.show()