# Хороший пароль
# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и
# строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

# put your python code here
psw = input()
d = any(map(lambda x: x.isdigit(), psw))
l = any(map(lambda x: x.islower(), psw))
u = any(map(lambda x: x.isupper(), psw))
print('YES' if all([len(psw) >= 7, d, l, u]) else 'NO')
