"""
    Contagem progressiva e regressiva ao mesmo tempo.
"""

count_list = list(range(10, -1, -1))

for count1, count2 in enumerate(count_list):
    print(f'{count1:<4}  {count2}')
