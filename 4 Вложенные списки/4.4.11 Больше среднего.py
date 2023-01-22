# Больше среднего
# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего
# арифметического элементов данной строки.

# put your python code here
n = int(input())
arr = [input().split() for i in range(n)]
for r in arr:
    row = [int(c) for c in r]
    sa = sum(row) / n
    print(sum([1 for c in row if c > sa]))
