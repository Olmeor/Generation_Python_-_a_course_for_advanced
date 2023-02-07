# Отличники
# Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться,
# что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите программу с
# использованием встроенных функций all(), any() для помощи Тимуру в проверке.

# put your python code here
progress = []
for i in range(int(input())):
    progress.append(any(['5' in input().split() for j in range(int(input()))]))

print('YES' if all(progress) else 'NO')
