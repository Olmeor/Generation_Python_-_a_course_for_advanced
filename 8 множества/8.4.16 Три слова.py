# Три слова
# На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован
# один и тот же набор букв?

# put your python code here
s = input().split()
print(('NO', 'YES')[set(s[0]) == set(s[1]) == set(s[2])])
