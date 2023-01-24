# Заполнение 5 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
s = [int(i) for i in range(1, m + 1)]
matrix = []

for i in range(n):
    matrix.append(s)
    s = s[1:] + s[:1]

[print(*row) for row in matrix]
