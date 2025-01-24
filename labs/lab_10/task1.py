#Задача о рюкзаке с возможностью дробить предметы

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.cost_per_weight = value / weight


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.cost_per_weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.cost_per_weight * capacity
            break

    return total_value


items = [
    Item(value=60, weight=10),
    Item(value=100, weight=20),
    Item(value=120, weight=30)
]

capacity = 50

max_value = fractional_knapsack(items, capacity)
print(f"Максимальная стоимость, которую можно получить в рюкзаке: {max_value}")
