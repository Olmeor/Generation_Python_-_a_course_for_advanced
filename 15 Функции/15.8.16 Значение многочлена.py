# Значение многочлена 🌶️
# Многочленом степени n называется выражение вида
#
# На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число x на
# второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.

# put your python code here
from functools import reduce

evaluate = lambda coef, x: reduce(lambda v, c: c + v * x, map(int, coef))
print(evaluate(input().split(), int(input())))
