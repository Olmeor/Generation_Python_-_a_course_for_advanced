# Упорядоченные дроби
# На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все
# несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.

# put your python code here
from fractions import Fraction as F

n = int(input())

a = []
for i in range(1, n + 1):
    for j in range(1, i):
        f = F(j, i)
        if f.numerator == j:
            a.append(f)

print(*sorted(a), sep="\n")
