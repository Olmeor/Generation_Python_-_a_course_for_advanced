# Симметричная матрица
# Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.

# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

def is_semmetry(matrix):
    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
                return 'NO'
    return 'YES'

print(is_semmetry(matrix))
