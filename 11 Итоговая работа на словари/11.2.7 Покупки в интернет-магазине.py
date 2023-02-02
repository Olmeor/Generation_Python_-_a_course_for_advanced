# Покупки в интернет-магазине 🌶️
# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем
# интернет-магазина.

# put your python code here
customer = {}
for _ in range(int(input())):
    n, i, c = input().split()
    if n not in customer:
        customer[n] = customer.setdefault(n, {i: int(c)})
    elif i not in customer[n].keys():
        customer[n][i] = int(c)
    elif i in customer[n].keys():
        customer[n][i] += int(c)

for n in sorted(customer):
    print(n + ':')
    print(*sorted(i + ' ' + str(c) for i, c in customer[n].items()), sep="\n")
