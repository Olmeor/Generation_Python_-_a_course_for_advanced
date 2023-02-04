# Математическое выражение
# На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения:

# put your python code here
from decimal import Decimal as D

n = D(input())
print(n.exp() + n.ln() + n.log10() + n.sqrt())
