# Латинский квадрат 🌶️
# Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой
# содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским
# квадратом.

# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_r = [[matrix[j][i] for j in range(n)] for i in range(n)]

def is_latin(matrix):
    for i in range(n):
        for j in range(n):
            if j + 1 not in matrix[i] or j + 1 not in matrix_r[i]:
                return 'NO'
    return 'YES'

print(is_latin(matrix))
