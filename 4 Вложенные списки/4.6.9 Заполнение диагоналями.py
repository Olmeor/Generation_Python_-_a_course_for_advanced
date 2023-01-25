# Заполнение диагоналями 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# заполнив её "диагоналями" в соответствии с образцом.

# put your python code here
n, m = [int(i) for i in input().split()]
matrix = [[i * m + j for j in range(1, m + 1)] for i in range(n)]

counter = 1
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if k == i + j:
                matrix[i][j] = counter
                counter += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
