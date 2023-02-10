# Сумма двух-1
# Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу,
# выводящую на экран сумму этих чисел.

file = open('numbers.txt', 'r', encoding='utf-8')
print(sum(map(lambda line: int(line.strip()), file.readlines())))
file.close()
