# Самое редкое слово 🌶️
# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
# без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# put your python code here
result = {}
for w in input().lower().split():
    word = w.strip(':,.!?();')
    result[word] = result.get(word, 0) + 1

words = sorted([key for key, values in result.items() if values == min(result.values())])
print(words[0])
