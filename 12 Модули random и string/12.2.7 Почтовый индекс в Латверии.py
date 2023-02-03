# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского
# алфавита, Number – число от 0 до 99 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный
# почтовый индекс Латверии.

from random import choice as c
from string import *


def generate_index():
    s = ascii_uppercase
    n = digits
    return f"{c(s)}{c(s)}{c(n)}{c(n)}_{c(n)}{c(n)}{c(s)}{c(s)}"
