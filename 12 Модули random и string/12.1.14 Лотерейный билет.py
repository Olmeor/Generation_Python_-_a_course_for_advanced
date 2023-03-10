# Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).
#
# Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
# Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.

# put your python code here
from random import randrange

ticket = set()
while len(ticket) < 7:
    ticket.add(randrange(1, 50))

print(*sorted(ticket))
