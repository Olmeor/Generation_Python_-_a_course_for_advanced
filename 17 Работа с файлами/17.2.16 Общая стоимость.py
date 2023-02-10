# Общая стоимость
# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
# символа табуляции (\t) разделена на три колонки:
#
# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 1 шт (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.

from functools import reduce

file = open('prices.txt', 'r', encoding='utf-8')
tab = [line.split() for line in file.readlines()]
print(reduce(lambda s, line:  s + int(line[1]) * int(line[2]), tab, 0))
file.close()
