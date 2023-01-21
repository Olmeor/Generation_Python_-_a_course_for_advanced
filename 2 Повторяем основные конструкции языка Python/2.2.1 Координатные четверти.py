# Координатные четверти
# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой
# координатной четверти.

# put your python code here
n = int(input())
x = []
y = []
for _ in range(n):
    s = input().split()
    x.append(int(s[0]))
    y.append(int(s[1]))
q = [0, 0, 0, 0]
for i in range(n):
    if x[i] > 0 and y[i] > 0:
        q[0] += 1
    elif x[i] < 0 < y[i]:
        q[1] += 1
    elif x[i] < 0 and y[i] < 0:
        q[2] += 1
    elif x[i] > 0 > y[i]:
        q[3] += 1
print("Первая четверть: " + str(q[0]), "Вторая четверть: " + str(q[1]), "Третья четверть: " + str(q[2]), "Четвертая "
      "четверть: " + str(q[3]), sep="\n")
