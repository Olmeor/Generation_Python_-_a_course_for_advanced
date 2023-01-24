# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её "спиралью" в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[0 for j in range(m)] for i in range(n)]

x, y = 0, 0
dx, dy = 0, 1
matrix[0][0] = 1
counter = 2

while counter <= n * m:
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and matrix[x + dx][y + dy] == 0:
        matrix[x + dx][y + dy] = counter
        counter += 1
        x += dx
        y += dy
    else:
        if dy == 1:
            dy = 0
            dx = 1
        elif dx == 1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
