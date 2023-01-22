# След матрицы
# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след
# заданной квадратной матрицы.

# put your python code here
n = int(input())
arr = [input().split() for i in range(n)]
print(sum([int(arr[i][i]) for i in range(n)]))
