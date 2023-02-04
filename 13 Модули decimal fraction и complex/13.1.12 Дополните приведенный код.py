# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

from decimal import *

num = Decimal(input())
d = num.as_tuple().digits
print(max(d) + (min(d) if int(num) != 0 else 0))
