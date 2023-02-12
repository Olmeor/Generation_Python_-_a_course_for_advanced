# Random name and surname
# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
#
# Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их,
# каждую на отдельной строке.

from random import choice
with open('first_names.txt', encoding='utf-8') as names, open('last_names.txt', encoding='utf-8') as surnames:
    name, surname = names.readlines(), surnames.readlines()
    n = 3
    for i in range(n):
        print(choice(name).strip(), choice(surname).strip(), sep=' ')
