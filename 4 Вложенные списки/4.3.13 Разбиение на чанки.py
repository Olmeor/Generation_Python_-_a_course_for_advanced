# Разбиение на чанки 🌶️
# На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает
# список из чанков указанной длины.

# put your python code here
def chunked(s, n):
    s = s.split()
    arr = []
    for i in range(0, len(s), n):
        arr.append(s[i: i + n])
    return arr


text = input()
num = int(input())
print(chunked(text, num))
