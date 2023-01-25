# Транспонирование матрицы
# Напишите программу, которая транспонирует квадратную матрицу.

# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)
