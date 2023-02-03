# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного
# списка).

from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

shuffle(matrix)
[shuffle(matrix[i]) for i in range(len(matrix))]
