"""
    4 Fizz Buzz - se o parâmentro da função for divisível por 2, retorne fizz,
    ou se for divisível por 5, retorne buzz,
    ou se for divisível por 5 e por 3, retorne fizzbuzz
    se não retorne o número capturado.
"""


def fizbuz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'fizzbuzz'
    elif numero % 5 == 0:
        return 'buzz'
    elif numero % 2 == 0:
        return 'fizz'
    else:
        return numero


while True:
    dividendo = str(input('Digite um número e vamos ver se faz "fizzbuzz":  ')).strip()
    try:
        dividendo = int(dividendo)
    except:
        print('Valor inválido!')
    else:
        break


res = fizbuz(dividendo)
print(res)
