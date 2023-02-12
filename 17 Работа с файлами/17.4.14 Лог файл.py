# Лог файл 🌶️
# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая
# строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время выхода, где время указано в 24-часовом формате.
#
# Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка
# следования), которые были в сети не менее часа.

# put your python code here
def minutes(x):
    res = [int(i) for i in x.split(':')]
    return res[0] * 60 + res[1]

with open('logfile.txt', 'r', encoding='utf-8') as log, open('output.txt', 'w', encoding='utf-8') as out:
    for line in log:
        user = line.split(', ')
        if minutes(user[2]) - minutes(user[1]) >= 60:
            print(user[0], file=out)
