# Больше предыдущего
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу
# подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим
# числом.

# put your python code here
s = input().split()
counter = 0
for i in range(0, len(s) - 1):
    if int(s[i]) < int(s[i + 1]):
        counter += 1
print(counter)
