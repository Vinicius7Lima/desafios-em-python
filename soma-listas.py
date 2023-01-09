"""
    Considere 2 listas de inteiros ou floats, some os valores nas listas,
    retornandouma nova lista com os valores somados.
"""
from itertools import zip_longest

one_lista = [1, 2, 3, 4, 5, 6, 7]
two_lista = [1, 2, 3, 4]

soma = [float(sum(x)) for x in zip(one_lista, two_lista)]
soma_2 = [float(sum(x)) for x in zip_longest(one_lista, two_lista, fillvalue=0)]
print(f'{soma}')
print(soma_2)


