# Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
#
# Напишите программу сортировки списка спортсменов по указанному полю:
#
# 1: по имени;
# 2: по возрасту;
# 3: по росту;
# 4: по весу.

def n(t):
    return t[0]


def a(t):
    return t[1]


def h(t):
    return t[2]


def w(t):
    return t[3]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

srt = {1: n, 2: a, 3: h, 4: w}
k = int(input())
athletes.sort(key=srt[k])

[print(*c) for c in athletes]
