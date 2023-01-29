# Уникальные символы 1
# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

# put your python code here
arr = []
for i in range(int(input())):
    arr.append(len(set(input().lower())))
print(*arr, sep="\n")
