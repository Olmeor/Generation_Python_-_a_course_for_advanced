# Ходы ферзя
# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. Клетку, где
# стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные клетки заполните точками.

# put your python code here
x, y = input()
n = 8
x = ord(x) - 97
y = n - int(y)
matrix = [['.']* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == y and j == x:
            matrix[i][j] = 'Q'
        elif (i == y or j == x) or i + j == y + x or i - j == y - x:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)
