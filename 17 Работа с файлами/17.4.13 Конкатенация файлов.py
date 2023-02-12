# Конкатенация файлов 🌶️
# На вход программе подается натуральное число n и n строк с названиями файлов. Напишите программу, которая создает
# файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

# put your python code here
n = int(input())
result = ''

for i in range(n):
    with open(input(), 'r', encoding='utf-8') as file:
        result += file.read()

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(result)
