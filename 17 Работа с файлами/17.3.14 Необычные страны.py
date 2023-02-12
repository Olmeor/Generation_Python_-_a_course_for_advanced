# Необычные страны
# Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом
# табуляции '\t'.

with open('population.txt', 'r', encoding='utf-8') as file:
    for line in file:
        country, count = line.split('\t')
        if country.startswith('G') and int(count) > 500_000:
            print(country)
