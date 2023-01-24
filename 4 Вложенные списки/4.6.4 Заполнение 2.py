# Заполнение 2
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[i + j * n + 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
