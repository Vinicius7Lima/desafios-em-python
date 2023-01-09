"""
    2 crie uma função que recebe outra função como parâmentro e
    retorne o valor da outra função execuada. Faça a função
    executar duas funçoes
    que recebam um número diferente de argumentos.
"""


def principal(func1, func2, *args):     # funão principal vai receber nº argumentos, 2 deles são funções
    return func1(args[0]), func2(args[2])[0], func1(args[1])
#  retornando  as funções com argumentos dentro delas,
#  especificando os valores e descompactando as funções e valores.


def mensagem1(msg='Oi'):     # retorna o argumento msg que pode ser qualque valor
    return msg


def mensagem2(nome='', resp='ok'):  # retorna os argumentos nome e resp, que pode ser qualque valor.
    return nome, resp


#  mostra o resultado das funções acima. chama a função principal que recebe vários arqumentos.
#  Sendo 2 deles funções, as funções em se, o restante são valores do tipo strings.
print(*principal(mensagem1, mensagem2, 'Seja bem vindo', 'Fique avontade!', 'Vini,'))



