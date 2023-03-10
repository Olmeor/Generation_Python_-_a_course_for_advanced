# Набор сообщений
# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. Поскольку с
# каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. При однократном
# нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2,3,4 или 5 раз генерирует
# второй, третий, четвертый или пятый символ клавиши.
#
# 1	.,?!:
# 2	ABC
# 3	DEF
# 4	GHI
# 5	JKL
# 6	MNO
# 7	PQRS
# 8	TUV
# 9	WXYZ
# 0	space (пробел)
#
# Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.

# put your python code here
s = input().upper()
nums = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

for c in s:
    for key, value in nums.items():
        if c in value:
            print(key * (value.index(c) + 1), end="")
