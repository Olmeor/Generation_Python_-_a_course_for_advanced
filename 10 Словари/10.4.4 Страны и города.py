# Страны и города
# На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу,
# которая для каждого города выводит, в какой стране он находится.

# put your python code here
d = {}
for _ in range(int(input())):
    s = input().split()
    for i in range(1, len(s)):
        d[s[i]] = s[0]
print(*[d[input()] for _ in range(int(input()))], sep="\n")
