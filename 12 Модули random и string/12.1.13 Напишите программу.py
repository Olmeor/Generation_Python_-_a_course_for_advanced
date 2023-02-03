# Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
# пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем
# регистре).

import random

length = int(input())    # длина пароля
password = ''
for i in range(length):
    password += [chr(random.randint(65, 90)), chr(random.randint(97, 122))][random.randint(0, 1)]
print(password)
