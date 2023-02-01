# Секретное слово
# Напишите программу для расшифровки секретного слова методом частотного анализа.

# put your python code here
cipher = input()
dct = {c: cipher.count(c) for c in set(cipher)}

letters = {}
for _ in range(int(input())):
    s = input().split(': ')
    letters[int(s[1])] = s[0]

print(*[letters[dct[c]] for c in cipher], sep="")
