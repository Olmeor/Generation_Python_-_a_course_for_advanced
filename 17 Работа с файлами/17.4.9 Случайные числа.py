# Случайные числа
# Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777
# (включительно), каждое с новой строки.

# put your python code here
from random import randrange
with open('random.txt', 'w', encoding='utf-8') as file:
    for _ in range(25):
        file.write(f'{randrange(111, 778)}\n')
