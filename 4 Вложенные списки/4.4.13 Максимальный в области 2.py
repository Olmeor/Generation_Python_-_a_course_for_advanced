# Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# put your python code here
n = int(input())
arr = [input().split() for i in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            res.append(int(arr[i][j]))
print(max(res))
