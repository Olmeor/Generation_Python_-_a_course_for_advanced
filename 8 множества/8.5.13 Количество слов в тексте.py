# Количество слов в тексте
# Напишите программу для определения общего количества различных слов в строке текста.

# put your python code here
s = input().lower().split()
for i in range(len(s)):
    s[i] = s[i].strip(".,;:-?!")
print(len(set(s)))
