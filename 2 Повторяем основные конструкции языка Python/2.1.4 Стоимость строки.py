# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том
# числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# put your python code here
s = len(input())
print(f"{s * 60 // 100} р. {s * 60 % 100} коп.")
