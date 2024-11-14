def find_pairs_with_sum(arr, target_sum):
    seen = set()
    pairs = []

    for number in arr:
        complement = target_sum - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
result = find_pairs_with_sum(numbers, target)
print(f'Пары чисел с суммой {target}: {result}')

