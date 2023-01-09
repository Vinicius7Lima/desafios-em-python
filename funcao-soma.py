"""
    2 crie uma função que recebe 3 números como parâmentros e
     exiba a soma entre eles.
"""


def adicao(numeros):
    n1 = numeros[0]
    n2 = numeros[1]
    n3 = numeros[2]
    return n1 + n2 + n3


numeros = []
for vezes in range(3):
    numero = str(input('Digite um número, por favor: ')).strip()
    try:
        numeros.append(int(numero))
    except:
        print('Valor inválido!')
        numeros.append(0)

soma = adicao(numeros)
print(f'A soma entre os valores {numeros[0]}, {numeros[1]} e {numeros[2]}, é igual a {soma}.')

