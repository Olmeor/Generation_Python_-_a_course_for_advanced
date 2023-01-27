# Вершина параболы
# Уравнение параболы имеет вид y = ax2 + bx + c, где a ≠ 0.
# Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.

# put your python code here
a, b, c = int(input()), int(input()), int(input())
x = round(-b / (2 * a), 1)
y = round((4 * a * c - b * b) / (4 * a), 1)
print((x, y))
