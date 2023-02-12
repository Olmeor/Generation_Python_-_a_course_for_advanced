# Подарок на новый год
# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
# оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
#
# Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в
# файл new_scores.txt.

# put your python code here
with open('class_scores.txt', 'r', encoding='utf-8') as file_in, open('new_scores.txt', 'w', encoding='utf-8') as file_out:
    arr = list(file_in.readlines())
    for s in arr:
        n, g = s.split()
        print(f'{n} {int(g) + 5 if int(g) + 5 <= 100 else 100}', file=file_out)
