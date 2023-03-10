# Побочная диагональ
# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:
# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

# put your python code here
n = int(input())
matrix = [[] for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i > j:
            matrix[i].append(2)
        elif i == j:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

for row in matrix:
    print(*row)
