# Тайный друг 🌶️
# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним
# решать задачи по программированию.

# put your python code here
from random import shuffle

padawan = [input() for _ in range(int(input()))]
shuffle(padawan)

for i in range(len(padawan)):
    if i < len(padawan) - 1:
        print(padawan[i] + ' - ' + padawan[i + 1])
    else:
        print(padawan[i] + ' - ' + padawan[0])
