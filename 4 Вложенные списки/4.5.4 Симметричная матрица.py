# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]
result = 'YES'

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)
