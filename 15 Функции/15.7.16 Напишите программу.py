# Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном
# порядке список primary городов с населением более 10000000 человек, в формате:
#
# Cities: Beijing, Buenos Aires, ...

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

step1 = filter(lambda l: l if l[1] > 10_000_000 and l[2] == 'primary' else None, data)
step2 = sorted(map(lambda c: c[0], step1))
step3 = reduce(lambda c, t: c + t + ', ', step2, 'Cities: ')

print(step3[:-2])
