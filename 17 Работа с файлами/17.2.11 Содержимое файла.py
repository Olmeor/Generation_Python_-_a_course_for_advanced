# Содержимое файла
# На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его
# содержимое.

file = open(input(), 'r', encoding='utf-8')
print(file.read())
file.close()
