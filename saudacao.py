"""
   1 crie uma função que exibe uma saudação com os parâmentros saudação e nome.
"""


def funcao(msm='Olá', nome=''):
    print(f'{msm}, {nome}')


saudacao = str(input('Digite uma saudação, por favor: ')).strip().title()
name = str(input('Digite um Nome: ')).strip().title()
funcao(saudacao, name)
