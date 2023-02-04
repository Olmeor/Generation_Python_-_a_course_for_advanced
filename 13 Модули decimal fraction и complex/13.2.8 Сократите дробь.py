# Сократите дробь
# Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь n/m и выводит ее.

# put your python code here
from fractions import Fraction as F

m, n = int(input()), int(input())
print(F(m, n))
