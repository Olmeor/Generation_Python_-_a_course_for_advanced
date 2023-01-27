# Конкурсный отбор
# Напишите программу, которая выводит список хорошистов и отличников в классе.

# put your python code here
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
[print(*t) for t in arr]
print()
[print(*t) for t in arr if int(t[1]) > 3]
