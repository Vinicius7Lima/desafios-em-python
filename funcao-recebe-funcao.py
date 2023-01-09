"""
    1 crie uma função que recebe outra função como parâmentro e
    retorne o valor da outra função execuada.
"""


def principal(msg):
    return msg()


def mensagem():
    return 'Seja muito bem vindo!'


print(principal(mensagem))

