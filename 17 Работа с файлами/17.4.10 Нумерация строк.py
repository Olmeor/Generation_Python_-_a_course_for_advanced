# Нумерация строк
# Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого
# файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
# Нумерация строк должна начинаться с 1.

# put your python code here
with open('input.txt', 'r', encoding='utf-8') as file_in, open('output.txt', 'w', encoding='utf-8') as file_out:
    arr = list(enumerate(file_in.readlines(), start=1))
    for n, s in arr:
        print(f'{n}) {s}', end="", file=file_out)
