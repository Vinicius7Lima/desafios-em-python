"""
    Criar uma lista com produtos e depois somar esses valores em uma list compreention
"""


carrinho = []


carrinho.append(('produto_1', 15))
carrinho.append(('produto_2', 25))
carrinho.append(('produto_3', 35))
carrinho.append(('produto_4', 45))
carrinho.append(('produto_5', 5))

somador = sum([float(x[1]) for x in carrinho])

print(somador)


