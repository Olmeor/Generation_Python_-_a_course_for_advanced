# Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество
# попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).

import random

n = int(input())    # количество попыток

for i in range(n):
    print(('Орел', 'Решка') [random.randint(0, 1)])
