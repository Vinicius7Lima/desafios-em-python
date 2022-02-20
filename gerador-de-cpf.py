"""
    gerador de cpfs
"""

from random import randint # imporpei uma biblioteca com uma class que gera números aleatórios.

nine = ''
for a in range(0, 9):   # Um laço de repetição para gerar os 9 valores aleatórios
    nine += (str(randint(0, 9)))  # gerando valores, transformando em strings e guardando-os.

print(nine)
repetido = 0  # váriavel para somar os valores reptidos
for caracter in nine:  # laço para verificar os valores reptidos em nine
    if nine[0] == caracter:  # verifica se à ação é verdadeira.
        repetido += 1       # incrementa + 1

novo_cpf2 = ''  #  Vai guardar o novo cpf gerado
if repetido < 9:  # verifica se há repetição dos algarismos
    for vezes in range(1, 3):  # faz 2 repetições para gerar mais 2 valores para o cpf
        soma = 0  # soma os valores da multiplicação.
        for p, r in enumerate(range(9 + vezes, 1, -1)):  # laço para pecorrer a contagem e os númeos aleatórios
            soma += (int(nine[p]) * r)  #  tranformando os valores em inteiro e somando os valores da multiplicação

        resto = (soma * 10) % 11   # calculo para pegar o resto da divisão.

        if resto > 9:   # verifica se o resto é maior do que 9.
            resto = 0

        nine += str(resto)  # resto vira string e é calcatenado no nine.

    for a, b in enumerate(nine):  # formatando o nine para a saída se parecer com um cpf.
        if a == 3 or a == 6:  # verifica onde vai ser acrescentador o símbolo "." no novo_cpf2
            novo_cpf2 += '.'  # recebendo o "." na 3° posição ou na 6º posição
        elif a == 9:    # verifica onde vai ser acrescentador o símbolo "-" no novo_cpf2
            novo_cpf2 += '-'    # recebendo o "-" na 9° posição
        novo_cpf2 += b  # recebendo os caracteres da váriavel nine

print(novo_cpf2)    # mostrar o valor gerado na tela.
