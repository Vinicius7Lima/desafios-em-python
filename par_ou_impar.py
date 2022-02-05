"""
    O programa ira receber um valor do tipo inteiro do usuário e
    vai dizer se esse valor é par ou ímpar.
"""

print(f'{"Verificador de números pares ou ímpares"}')
numero = str(input('Digite um número inteiro: ')).strip()
try:
    numero = int(numero)
except:
    print('O valor digitado não é um inteiro.')
else:
    if numero % 2 == 0:
        print(f'{numero} é Par.')
    else:
        print(f'{numero} é Ímpar.')
