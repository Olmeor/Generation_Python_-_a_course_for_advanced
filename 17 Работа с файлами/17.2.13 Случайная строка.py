# Случайная строка
# Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную
# строку из этого файла.

import random

file = open('lines.txt', 'r', encoding='utf-8')
print(random.choice(file.readlines()))
file.close()
