# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает
# именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов
# следуют в алфавитном порядке (по возрастанию).

def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f"{k}: {v}")
