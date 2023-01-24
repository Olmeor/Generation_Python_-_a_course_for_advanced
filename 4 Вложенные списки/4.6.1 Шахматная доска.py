# Шахматная доска
# На вход программе подаются два натуральных числа
# n и m. Напишите программу для создания матрицы размером n×m, заполнив её символами . и * в шахматном порядке. В левом
# верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[] for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i].append('.') if i % 2 == j % 2 else matrix[i].append('*')

for row in matrix:
    print(*row)
