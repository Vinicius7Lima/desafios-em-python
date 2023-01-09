"""
    3 crie uma função que recebe 2 números. o primeiro é um valor e o segundo um percentual
   (ex. 10%). Retorne o valor do primeiro somado do aumento do percentual do mesmo.
"""


def aumento(valor_inicial, porcentagem):
    valor_final = valor_inicial + (valor_inicial * (porcentagem / 100))
    return valor_final


while True:
    valor = str(input('Digite um valor: ')).strip()
    porcen = str(input('Digite uma porcentagem [sem %]: ')).strip()
    try:
        valor = float(valor)
        porcen = float(porcen)
    except:
        print('Valor inválido!')
    else:
        break

novo_valor = aumento(valor, porcen)
print(f'O Valor de R${valor:.2f} com {porcen}% de aumento, vai para R${novo_valor:.2f}')
