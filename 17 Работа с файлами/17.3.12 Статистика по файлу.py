# Статистика по файлу
# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
# латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

with open('file.txt', 'r', encoding='utf-8') as file:
    lines = len(file.readlines())
    file.seek(0)
    strings = file.read().strip()
    words = len(strings.split())
    letters = len([c for c in strings if c.isalpha()])
print('Input file contains:', str(letters) + ' letters', str(words) + ' words', str(lines) + ' lines', sep="\n")
