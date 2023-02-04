# На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число,
# равное значению выражения

# put your python code here
from fractions import Fraction as F

n = int(input())

print(sum([F(1, i * i) for i in range(1, n + 1)]))
