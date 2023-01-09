
"""
Exercício -> Crie uma função que encontra os 2 primeiros números duplicados na lista interna.

    Requisitos:
        A ordem dos números duplicados é contado a partir da segunda ocorrência.
        Ex: [1, 2, 3, 3, 2, 1]  = 3
        Se não encontrar duplicados, retorne -1

-> É uma lista de listas de números inteiros
-> As listas internas tem 10 elementos
-> As listas tem números entre 1 e 10, e podem ser duplicados
"""
from random import randint

valor_x = []
for vezes in range(0, 10):
    valor_x.append(randint(1, 11))

p_lista = [
    list(range(1, 11)),
    [2, 3, 1, 2, 4, 7, 10, 9, 5, 3],  # 2
    valor_x
]

repetido = 0
for lista in p_lista:
    count = 0
    duplicados = []
    print(f'{lista}, tem o seguinte valor duplicado -> ')
    for valor in lista:
        count += 1
        for numb in range(count, 10):
            if valor == lista[numb]:
                duplicados.append(numb)
                break
    if not duplicados:
        repetido = -1
    else:
        repetido = lista[min(duplicados)]

    print(repetido)
