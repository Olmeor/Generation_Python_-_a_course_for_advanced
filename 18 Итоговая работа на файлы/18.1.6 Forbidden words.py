# Forbidden words 🌶️
# На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое
# этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).
#
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что
# все слова в этом файле записаны в нижнем регистре.

with open(input(), 'r', encoding='utf-8') as file, open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden:
    check = forbidden.readline().split()
    for line in file:
        s = line
        sl = line.lower()
        res = ''

        for word in check:
            if word in sl:
                sl = sl.replace(word, '*' * len(word))

        for i in range(len(sl)):
            res += s[i] if sl[i] != '*' else '*'

        print(res, end="")
