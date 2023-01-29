# Урок физики
# Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок
# третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

# put your python code here
a, b, c= set(input().split()), set(input().split()), set(input().split())
d = c - (a | b)
print(*sorted(d, reverse=True, key=int))
