# Строка запроса
# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после
# вопросительного знака и идет до конца адреса. Например:
#
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
#
# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса,
# сформированную из этих параметров.

def build_query_string(params):
    return '&'.join([k + '=' + str(v) for k, v in sorted(params.items())])
