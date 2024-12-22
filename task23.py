import itertools

def survival_knapsack_all_combinations(backpack_size, initial_points, condition, items):
    # Проверка обязательного предмета
    mandatory_item = 'i' if condition == 'астма' else 'd'
    mandatory_item_data = next(item for item in items if item['code'] == mandatory_item)

    # Уменьшаем размер рюкзака и добавляем обязательный предмет
    backpack_size -= mandatory_item_data['size']
    initial_points += mandatory_item_data['points']

    # Фильтруем предметы, исключая обязательный, так как он уже включён
    filtered_items = [item for item in items if item['code'] != mandatory_item]

    valid_combinations = []

    # Перебираем все возможные комбинации предметов
    for r in range(1, len(filtered_items) + 1):
        for combination in itertools.combinations(filtered_items, r):
            size = sum(item['size'] for item in combination)
            points = initial_points + sum(item['points'] for item in combination) - \
                     sum(item['points'] for item in filtered_items if item not in combination)

            # Проверяем вместимость и положительные очки выживания
            if size <= backpack_size and points > 0:
                valid_combinations.append((combination, points))

    return valid_combinations

# Данные задачи
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

# Задача 1: Рюкзак на 7 ячеек
backpack_size = 7
initial_points = 20
condition = 'астма'

valid_combinations = survival_knapsack_all_combinations(backpack_size, initial_points, condition, items)

print("Все возможные комбинации для рюкзака на 7 ячеек:")
for combo, points in valid_combinations:
    combo_codes = [item['code'] for item in combo]
    print(f"Предметы: {combo_codes}, Очки выживания: {points}")

# Задача 2: Все комбинации для исходного варианта
backpack_size = 8
initial_points = 20
condition = 'астма'

valid_combinations = survival_knapsack_all_combinations(backpack_size, initial_points, condition, items)

print("\nВсе возможные комбинации для исходного варианта (8 ячеек):")
for combo, points in valid_combinations:
    combo_codes = [item['code'] for item in combo]
    print(f"Предметы: {combo_codes}, Очки выживания: {points}")
