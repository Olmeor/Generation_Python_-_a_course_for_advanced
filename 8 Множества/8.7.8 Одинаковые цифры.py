# Одинаковые цифры
# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

# put your python code here
a, b = set(input()), set(input())
if a.isdisjoint(b):
    print('NO')
else:
    print('YES')
