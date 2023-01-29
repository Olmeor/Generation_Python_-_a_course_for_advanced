# Онлайн-школа BEEGEEK 3
# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
# У руководителя школы есть списки изучающих каждый предмет.
#
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.

# put your python code here
m = int(input())
n = int(input())
m_arr = set([input() for _ in range(m)])
n_arr = set([input() for _ in range(n)])
print(len(m_arr ^ n_arr) if len(m_arr ^ n_arr) else 'NO')
