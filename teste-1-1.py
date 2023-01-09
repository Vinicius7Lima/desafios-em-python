def n_valores_x():
    from random import randint
    principal_l = [list(range(1, 11))]
    for repet in range(0, 10):
        valor_x = []
        for vezes in range(0, 10):
            valor_x.append(randint(1, 10))
        principal_l.append(valor_x)
    return principal_l


p_lista = n_valores_x()

for lista in p_lista:
    conjunto = set()
    print(lista)
    duplicados = []
    p = -1
    #  print(f'{lista}, tem o seguinte valor duplicado -> ')
    for valor in lista:
        if valor in conjunto:
            p = valor
            break
        conjunto.add(valor)
    print(conjunto)
    print(p)
