# Сложение матриц
# Напишите программу для вычисления суммы двух матриц.

# put your python code here
n, m = [int(i) for i in input().split()]
m1 = [input().split() for i in range(n)]
input()
m2 = [input().split() for i in range(n)]

matrix = [[int(m1[i][j]) + int(m2[i][j]) for j in range(m)] for i in range(n)]

for row in matrix:
    print(*row)
