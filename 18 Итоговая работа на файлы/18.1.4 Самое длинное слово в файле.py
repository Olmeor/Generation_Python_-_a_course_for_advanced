# Самое длинное слово в файле
# Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и
# выводит самые длинные слова этого файла, не меняя порядка их следования.

with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_len = max(map(lambda s: len(s), words))
    print(*[word for word in words if len(word) == max_len], sep="\n")
