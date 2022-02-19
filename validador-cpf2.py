cpf = '529.982.247-25'
novo_cpf = cpf[:-2].replace('.', '').replace('-', '')

repetido = 0
for caracter in novo_cpf:
    if novo_cpf[0] == caracter:
        repetido += 1

if repetido >= 9:
    msg = f'O CPF {cpf} é inválido!'
else:
    for vezes in range(1, 3):
        soma = 0
        for p, r in enumerate(range(9 + vezes, 1, -1)):
            soma += (int(novo_cpf[p]) * r)

        resto = (soma * 10) % 11

        if resto > 9:
            resto = 0

        novo_cpf += str(resto)


    novo_cpf2 = ''
    for a, b in enumerate(novo_cpf):
        if a == 3 or a == 6:
            novo_cpf2 += '.'
        elif a == 9:
            novo_cpf2 += '-'
        novo_cpf2 += b

    if novo_cpf2 == cpf:
        msg = f'O CPF {novo_cpf2} é válido!'
    else:
        msg = f'O CPF {novo_cpf2} é inválido!'

print(msg)
