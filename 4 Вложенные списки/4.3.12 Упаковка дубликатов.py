# Упаковка дубликатов 🌶️
# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
# последовательности одинаковых символов заданной строки в подсписки.

# put your python code here
c = input().split()
arr = []
counter = 1
for i in range(len(c)):
    if i < len(c) - 1 and c[i] == c[i + 1]:
        counter += 1
    else:
        arr.append([c[i]] * counter)
        counter = 1
print(arr)
