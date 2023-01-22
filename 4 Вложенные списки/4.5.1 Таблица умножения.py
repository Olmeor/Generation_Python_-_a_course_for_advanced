# Таблица умножения
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. Создайте матрицу mult
# размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

# put your python code here
n, m = int(input()), int(input())
arr = [[i * j for j in range(m)] for i in range(n)]
for r in range(n):
    for c in range(m):
        print(str(arr[r][c]).ljust(3), end="")
    print()
