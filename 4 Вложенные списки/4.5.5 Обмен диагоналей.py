# Обмен диагоналей
# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
# диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
# элемент на главной диагонали и на побочной диагонали).

# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)
