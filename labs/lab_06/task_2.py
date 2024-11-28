def count_ways(m, n):
    Q = [[0] * (n + 1) for _ in range(m + 1)]

    for n in range(n + 1):
        Q[1][n] = 1

    for m in range(m + 1):
        Q[m][1] = 1

    for m in range(2, m + 1):
        for n in range(2, n + 1):
            if m < n:
                Q[m][n] = Q[m][m]
            elif m == n:
                Q[m][n] = 1 + Q[m][n - 1]
            else:
                Q[m][n] = Q[m][n - 1] + Q[m - n][n]

    return Q[m][n]

m = 10
n = 5
print(count_ways(m, n))
