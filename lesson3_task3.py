# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

def find_backpack_combinations(items, max_weight):
    for r in range(1, len(items) + 1):
        for combination in combinations(items.items(), r):
            total_weight = sum(weight for _, weight in combination)
            if total_weight <= max_weight:
                yield [item for item, _ in combination]  

items = {
    "Палатка": 5,
    "Спальный мешок": 3,
    "Котелок": 2,
    "Еда": 4,
    "Вода": 3,
    "Фонарик": 1,
    "Аптечка": 1
}

max_weight = 10 

print("Все возможные комбинации:")
for combination in find_backpack_combinations(items, max_weight):
    print(combination)
