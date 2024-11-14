"_______________ВАРИАНТ 12___________________"

"_______________МАТРИЦЫ___________________"


import time
import matplotlib.pyplot as plt
import numpy as np



max_n = 10000
matrix_a = np.random.rand(max_n, max_n)
matrix_b = np.random.rand(max_n, max_n)
n_values = list(range(1, max_n, 1200))
times = []

def prod_matrix(matrix_a, matrix_b):
    result = np.dot(matrix_a, matrix_b)
    return result


for n in n_values:
    start_time = time.time()
    prod_matrix(matrix_a[:n, :n], matrix_b[:n, :n])
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times)

plt.title('Зависимость среднего времени выполнения от n \n (от матричного произведения)')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.show()