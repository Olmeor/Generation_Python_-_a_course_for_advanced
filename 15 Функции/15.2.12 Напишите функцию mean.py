# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое
# переданных в нее числовых (int или float) аргументов.

def mean(*args):
    counter, total = 0, 0
    for i in args:
        if type(i) == int or type(i) == float:
            total += i
            counter += 1
    return total / counter if counter else 0.0
