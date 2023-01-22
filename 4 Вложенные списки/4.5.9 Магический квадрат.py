# Магический квадрат 🌶️
# Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n2 так,
# что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая
# проверяет, является ли заданная квадратная матрица магическим квадратом.

# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]
s = sum(int(i) for i in matrix[0])


def check_num():
    arr = []
    for row in matrix:
        arr.extend(row)
    for i in range(1, n ** 2 + 1):
        if not str(i) in arr:
            return False
    return True


def check_sum():
    for i in range(n):
        if sum(int(j) for j in matrix[i]) != s \
        or sum(int(matrix[j][i]) for j in range(n)) != s:
            return False
    if s != sum(int(matrix[i][i]) for i in range(n)) and s != sum(int(matrix[i][n - i - 1]) for i in range(n)):
        return False
    return True

print('YES' if check_num() and check_sum() else 'NO')
