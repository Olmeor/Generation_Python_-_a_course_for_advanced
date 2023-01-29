# Общие цифры
# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

# put your python code here
n = int(input())
arr_nums = [set(*input().split()) for _ in range(n)]
interseption_num = arr_nums[0].intersection(*arr_nums)
print(*sorted(interseption_num))
