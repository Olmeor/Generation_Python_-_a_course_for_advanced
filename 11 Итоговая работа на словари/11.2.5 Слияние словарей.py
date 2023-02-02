# Слияние словарей 🌶️
# Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать
# словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей
# переданного списка.

def merge(values):      # values - это список словарей
    res = {}
    for d in values:
        for k, v in d.items():
            res[k] = res.get(k, set())
            res[k].add(v)
    return res
