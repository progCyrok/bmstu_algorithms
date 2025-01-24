#Генерация разбиений множества

def partitions(s):
    if not s:
        return [[]]

    result = []
    first_elem = s[0]

    for partition in partitions(s[1:]):
        for i in range(len(partition)):
            new_partition = partition[:i] + [[first_elem] + partition[i]] + partition[i+1:]
            result.append(new_partition)

        result.append([[first_elem]] + partition)

    return result

input_set = [1, 2, 3]
partitions_result = partitions(input_set)

for part in partitions_result:
    print(part)
