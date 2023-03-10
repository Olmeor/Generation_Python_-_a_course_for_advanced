# Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по
# убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка,
# каждый на новой строке в формате:
#
# <название штата>: <численность населения>
# Vermont: 626299
# Massachusetts: 7029917
# ...

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

data.sort(key=lambda data: data[1][-1], reverse=True)
print(*[f"{v}: {k}" for k, v in data], sep="\n")
