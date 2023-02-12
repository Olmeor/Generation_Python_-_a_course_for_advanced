# Tail of a File
# На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние
# 10 строк данного файла.

with open(input(), 'r', encoding='utf-8') as file:
    text = file.readlines()[-10:]
    for line in text:
        print(line, end="")
