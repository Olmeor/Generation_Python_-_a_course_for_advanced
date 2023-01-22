# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
# горизонтальной оси симметрии.

# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)
