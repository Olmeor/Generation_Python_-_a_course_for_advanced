# Камень, ножницы, бумага, ящерица, Спок 🌶️
# Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан
# играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто
# будет делать следующий модуль в новом курсе.

# put your python code here
r, t = input(), input()
a = ['камень', 'ножницы', 'бумага']
if (t == 'камень' and (r == 'ножницы' or r == 'ящерица')) or \
        (t == 'ножницы' and (r == 'бумага' or r == 'ящерица')) or \
        (t == 'бумага' and (r == 'камень' or r == 'Спок')) or \
        (t == 'ящерица' and (r == 'Спок' or r == 'бумага')) or \
        (t == 'Спок' and (r == 'камень' or r == 'ножницы')):
    print('Руслан')
elif t == r:
    print('ничья')
else:
    print('Тимур')
