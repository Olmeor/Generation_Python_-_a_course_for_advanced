# CSV-файл
# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из
# этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую
# последующую строку как значения этих ключей.

def read_csv():
    result = []

    with open('data.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        keys = lines[0].strip().split(',')
        for i in range(1, len(lines)):
            result.append(dict(zip(keys, lines[i].strip().split(','))))
    return result
