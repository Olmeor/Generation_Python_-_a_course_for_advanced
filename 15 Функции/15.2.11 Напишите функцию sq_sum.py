# Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их
# квадратов.

def sq_sum(*args):
    return sum(i * i for i in args)
