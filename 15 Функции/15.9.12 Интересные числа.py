# Интересные числа
# На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции all()
# для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них цифру без остатка.

# put your python code here
a, b = int(input()), int(input())
d = [i for i in range(a, b + 1)]
print(*filter(lambda n: all('0' not in i and n % int(i) == 0 for i in str(n)), d))
