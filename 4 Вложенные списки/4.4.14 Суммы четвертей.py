# Суммы четвертей
# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую
# и правую.
#
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой
# четверти.

n = int(input())
arr = [input().split() for i in range(n)]
text = ['Верхняя четверть:', 'Правая четверть:', 'Нижняя четверть:', 'Левая четверть:']
res = [0 for _ in range(4)]
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 -j:
            res[0] += int(arr[i][j])
        elif i < j and i > n - 1 -j:
            res[1] += int(arr[i][j])
        elif i > j and i > n - 1 -j:
            res[2] += int(arr[i][j])
        elif i > j and i < n - 1 -j:
            res[3] += int(arr[i][j])
print(*(f"{text[i]} {res[i]}" for i in range(4)), sep="\n")
