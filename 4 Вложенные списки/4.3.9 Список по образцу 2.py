# Список по образцу 2
# На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

# put your python code here
n = int(input())
print(*([i for i in range(1, j + 1)] for j in range(1, n + 1)), sep="\n")
