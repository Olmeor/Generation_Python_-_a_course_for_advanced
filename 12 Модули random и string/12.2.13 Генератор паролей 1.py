# Генератор паролей 1
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и
# прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).

from random import *
from string import *


def generate_password(length):
    s = list((ascii_letters + digits))
    [s.remove(c) for c in 'lI1oO0']
    return ''.join(sample(s, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
