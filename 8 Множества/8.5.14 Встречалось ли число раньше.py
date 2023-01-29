# Встречалось ли число раньше?
# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

# put your python code here
numbers = [int(i) for i in input().split()]
_set = set()
for i in range(len(numbers)):
    if numbers[i] not in _set:
        print('NO')
        _set.add(numbers[i])
    else:
        print('YES')
