# Максимальный в области 2
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# put your python code here
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        if j >= n - i - 1:
            arr.append(matrix[i][j])
print(max(arr))
