# Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка
# numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1.

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {n: [i for i in range(1, n + 1) if not n % i] for n in numbers}
