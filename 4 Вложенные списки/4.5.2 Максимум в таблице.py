# Максимум в таблице
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем n строк по m
# целых чисел в каждой, отделенных символом пробела.
#
# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

# put your python code here
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row, col = i, j

print(row, col)
