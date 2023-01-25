# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.

# put your python code here
n, m = [int(i) for i in input().split()]
m1 = [input().split() for i in range(n)]
input()
_n, _m = [int(i) for i in input().split()]
m2 = [input().split() for i in range(_n)]

matrix = [[] for _ in range(n)]

for i in range(n):
    for j in range(_m):
        el = 0
        for k in range(m):
            el += int(m1[i][k]) * int(m2[k][j])
        matrix[i].append(el)

for row in matrix:
    print(*row)
