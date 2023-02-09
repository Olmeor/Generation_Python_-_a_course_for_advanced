# Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *,
# /) и возвращает функцию двух аргументов для соответствующей операции.

from operator import *


def arithmetic_operation(operation):
    kw = {"+": add,
          "-": sub,
          "*": mul,
          "/": truediv}
    return kw[operation]
