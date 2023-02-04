# Сопряженные числа
# Дано натуральное числоn и два комплексных числаz1 ,z2. Напишите программу, которая вычисляет и выводит значение
# выражения

# put your python code here
n = int(input())
a, b = complex(input()), complex(input())

print(a ** n + b ** n + a.conjugate() ** n + b.conjugate() ** (n+1))
