#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def find_duplicates(input_list):
    duplicates = set()
    seen = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Пример использования
input_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 3, 8, 1]
result = find_duplicates(input_list)
print(result)

