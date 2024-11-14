def check(arr1, arr2):
    intersections = [value for value in arr1 if value in arr2]
    return intersections

array1 = [1, 2, 3, 4, 5, 7]
array2 = [4, 5, 6, 7, 8]
result = check(array1, array2)

if len(result) > 0:
    print(f"Пересечение найдено: {result}")
else:
    print("Пересечения нет.")
