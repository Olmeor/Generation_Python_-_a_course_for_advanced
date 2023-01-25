# Возведение матрицы в степень 🌶️
# Напишите программу, которая возводит квадратную матрицу в m-ую степень.

# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
m = int(input())
_matrix = matrix

for _ in range(m - 1):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += _matrix[i][k] * matrix[k][j]
    _matrix = res

for row in res:
    print(*row)
