# Предпоследняя строка
# На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его
# предпоследнюю строку.

file = open(input(), 'r', encoding='utf-8')
print(file.readlines()[-2])
file.close()
