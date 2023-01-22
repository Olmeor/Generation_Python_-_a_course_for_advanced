# Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.

# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]

matrix.reverse()
for i in range(n):
    for j in range(i + 1):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)
