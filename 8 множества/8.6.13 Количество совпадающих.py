# Количество совпадающих
# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая определяет количество
# чисел, которые есть как в первой строке, так и во второй.

# put your python code here
s1, s2 = set(input().split()), set(input().split())
s = s1 & s2
print(len(s))
