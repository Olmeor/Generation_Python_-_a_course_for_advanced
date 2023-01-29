# Дополните приведенный код, чтобы он вывел элементы множества fruits, каждый на отдельной строке, отсортированные по
# убыванию (в обратном лексикографическом порядке).

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}

print(*sorted(fruits, reverse=True), sep='\n')
