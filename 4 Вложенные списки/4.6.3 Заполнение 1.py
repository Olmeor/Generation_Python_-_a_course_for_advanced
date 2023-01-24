# Заполнение 1
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m и
# заполняет её числами от 1 до n⋅m в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[i * m + j for j in range(1, m + 1)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
