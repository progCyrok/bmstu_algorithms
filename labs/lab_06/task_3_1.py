def Q(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1:
        return 1
    if n == 1:
        return 1
    if m < n:
        result = Q(m, m, memo)
    elif m == n:
        result = 1 + Q(m, m - 1, memo)
    else:
        result = Q(m, n - 1, memo) + Q(m - n, n, memo)

    memo[(m, n)] = result
    return result

m = 10
n = 5
print(Q(m, n))




