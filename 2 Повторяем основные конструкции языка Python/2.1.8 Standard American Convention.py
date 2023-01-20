# Standard American Convention
# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в
# соответствии со стандартным американским соглашением о запятых в больших числах.

# put your python code here
n = input()[::-1]
s = ''
for i in range(len(n)):
    # s = n[i] + s if (i - 1) % 3 == 0 else ',' + n[i] + s
    if i % 3 != 0 or i == 0:
        s += n[i]
    else:
        s += ',' + n[i]
print(s[::-1])
