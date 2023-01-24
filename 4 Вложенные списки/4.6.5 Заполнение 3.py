# Заполнение 3
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив её в
# соответствии с образцом.

# put your python code here
n = int(input())
matrix = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
        print(str(matrix[i][-1]).ljust(3), end="")
    print()
