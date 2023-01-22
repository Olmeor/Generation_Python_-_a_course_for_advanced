# Максимальный в области 1
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# put your python code here
n = int(input())
arr = [input().split() for i in range(n)]
res = []
for i in range(n):
    for j in range(i + 1):
        res.append(int(arr[i][j]))
print(max(res))
