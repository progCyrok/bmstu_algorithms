def check(arr):
    return len(arr) == len(set(arr))

array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 2, 3, 4]

print(check(array1))  # True
print(check(array2))  # False
