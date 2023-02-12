# Входная строка
# Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.

# put your python code here
string = input()
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(string)
