# Треугольник Паскаля 2
# На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника
# Паскаля.

# put your python code here
n = int(input())
arr = [[1 for i in range(j)] for j in range(1, n + 2)]

for c in range(0, n + 1):
    for r in range(1, c + 1):
        if r == 0 or r == c:
            continue
        arr[c][r] = arr[c - 1][r - 1] + arr[c - 1][r]

for r in range(len(arr) - 1):
    print(*arr[r])
