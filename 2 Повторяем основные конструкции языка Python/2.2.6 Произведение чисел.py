# Произведение чисел
# Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат
# в виде ответа «ДА» или «НЕТ».

# put your python code here
n = int(input())
a = [int(input()) for _ in range(n)]
r = int(input())


def is_proiz():
    for i in range(n):
        for j in range(n):
            if i != j and a[i] * a[j] == r:
                return 'ДА'
    return 'НЕТ'


print(is_proiz())
