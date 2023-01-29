# Онлайн-школа BEEGEEK 6 🌶️
# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала
# учебного года. Для каждого урока есть листок со списком присутствовавших учеников.
#
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.

# put your python code here
n = int(input())
list_family = [[input() for _ in range(int(input()))] for _ in range(n)]
geek = set(list_family[n - 1])
for i in range(n - 1):
    geek = geek.intersection(set(list_family[i]))
print(*sorted(geek), sep='\n')
