import itertools

def survival_knapsack(backpack_size, initial_points, condition, items):
   
    mandatory_item = 'i' if condition == 'астма' else 'd'
    mandatory_item_data = next(item for item in items if item['code'] == mandatory_item)

    backpack_size -= mandatory_item_data['size']
    initial_points += mandatory_item_data['points']
    filtered_items = [item for item in items if item['code'] != mandatory_item]

    max_points = float('-inf')
    best_combination = None

    for r in range(1, len(filtered_items) + 1):
        for combination in itertools.combinations(filtered_items, r):
            size = sum(item['size'] for item in combination)
            points = initial_points + sum(item['points'] for item in combination) - \
                     sum(item['points'] for item in filtered_items if item not in combination)

            if size <= backpack_size and points > 0:
                if points > max_points:
                    max_points = points
                    best_combination = combination

    
    if not best_combination:
        return None, None

    inventory = []
    flat_inventory = [mandatory_item] * mandatory_item_data['size']
    for item in best_combination:
        flat_inventory.extend([item['code']] * item['size'])

    
    for i in range(0, len(flat_inventory), 4):
        inventory.append(flat_inventory[i:i + 4])

    return inventory, max_points


items = [
    {'name': 'Винтовка', 'code': 'r', 'size': 3, 'points': 25},
    {'name': 'Пистолет', 'code': 'p', 'size': 2, 'points': 15},
    {'name': 'Боекомплект', 'code': 'a', 'size': 2, 'points': 15},
    {'name': 'Аптечка', 'code': 'm', 'size': 2, 'points': 20},
    {'name': 'Ингалятор', 'code': 'i', 'size': 1, 'points': 5},
    {'name': 'Нож', 'code': 'k', 'size': 1, 'points': 15},
    {'name': 'Топор', 'code': 'x', 'size': 3, 'points': 20},
    {'name': 'Оберег', 'code': 't', 'size': 1, 'points': 25},
    {'name': 'Фляжка', 'code': 'f', 'size': 1, 'points': 15},
    {'name': 'Антидот', 'code': 'd', 'size': 1, 'points': 10},
    {'name': 'Еда', 'code': 's', 'size': 2, 'points': 20},
    {'name': 'Арбалет', 'code': 'c', 'size': 2, 'points': 20},
]

backpack_size = 8
initial_points = 20
condition = 'астма'

inventory, max_points = survival_knapsack(backpack_size, initial_points, condition, items)

if inventory:
    for row in inventory:
        print(row)
    print(f"Итоговые очки выживания: {max_points}")
else:
    print("Нет решения, удовлетворяющего условиям задачи.")
