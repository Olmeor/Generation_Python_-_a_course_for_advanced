# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и
# прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной
# букве в верхнем и нижнем регистре.

# put your python code here
from random import *
from string import *


def generate_password(length):
    s_l = [c for c in ascii_lowercase if c not in '10OolI']
    s_u = [c for c in ascii_uppercase if c not in '10OolI']
    s_d = [c for c in digits if c not in '10OolI']
    s = s_l + s_u + s_d
    pwd = sample(s, length - 3) + [choice(s_l), choice(s_u), choice(s_d)]
    shuffle(pwd)
    return ''.join(pwd)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")
