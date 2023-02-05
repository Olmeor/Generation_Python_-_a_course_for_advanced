# Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и
# возвращает приветствие в соответствии с образцом.

def greet(name, *args):
    names = " and " + ' and '.join(args) if args else ""
    return f"Hello, {name}{names}!"
