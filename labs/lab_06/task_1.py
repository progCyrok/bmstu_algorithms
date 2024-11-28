def Q(m, n):
    if m == 1:
        return 1
    if n == 1:
        return 1
    if m < n:
        return Q(m, m)
    if m == n:
        return 1 + Q(m, m - 1)
    else:
        return Q(m, n - 1) + Q(m - n, n)

m = 10
n = 5
print(Q(m,n))
