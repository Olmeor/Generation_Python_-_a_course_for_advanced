# Заполнение змейкой
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её "змейкой" в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[i * m + j for j in range(1, m + 1)] for i in range(n)]

for i in range(n):
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
