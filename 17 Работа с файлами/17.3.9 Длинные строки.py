# Длинные строки
# Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все
# строки наибольшей длины из файла, не меняя их порядок.

with open('lines.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    max_len = len(max(lines, key=len))
    print(*[line.strip() for line in lines if len(line) == max_len], sep="\n")
