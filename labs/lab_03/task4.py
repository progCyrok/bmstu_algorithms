def split_list(data_list):

  positive_list = []
  negative_list = []
  for item in data_list:
    if item > 0:
      positive_list.append(item)
    elif item < 0:
      negative_list.append(item)
  return positive_list, negative_list

# Example usage
my_list = [1, -2, 3, -4, 0, 5, -6]
positive_nums, negative_nums = split_list(my_list)

print("Исходный список:", my_list) # Вывод: Исходный список: [1, -2, 3, -4, 0, 5, -6]
print("Положительные числа:", positive_nums) # Вывод: Положительные числа: [1, 3, 5]
print("Отрицательные числа:", negative_nums) # Вывод: Отрицательные числа: [-2, -4, -6]
