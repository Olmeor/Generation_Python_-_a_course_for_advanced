# Goooood students
# Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки файла
# имеют вид: фамилия оценка_1 оценка_2 оценка_3.
#
# Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным, если количество
# баллов по нему не меньше 65.

counter = 0
with open('grades.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        student = line.split()
        if all(map(lambda g: True if int(g) >= 65 else False, student[1:])):
            counter += 1
print(counter)
