# Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().
#
# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result

from functools import reduce


def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda n: n % 2 == 1, data), 1)
