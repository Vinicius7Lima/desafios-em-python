"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
    descrito, exiba a saudação apropriada. Ex.
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horas = str(input('Informe o horário, por favor: ')).strip()
hora = minuto = 0
resposta = True
if 1 <= len(horas) <= 5 and ':' in horas:
    valor = horas.split(':')
    for i in range(2):
        try:
            valor[i] = int(valor[i])
        except:
            print('Formato de hora inválido!')
            resposta = False
            break
        else:
            if i == 0:
                hora = valor[0]
            elif i == 1:
                minuto = valor[1]
else:
    resposta = False
    print('Formato de hora inválido!')

if resposta:
    if 0 <= hora <= 11:
        print('Bom Dia!')
    elif 12 <= hora <= 17:
        print('Boa Tarde!')
    elif 18 <= hora <= 23:
        print('Boa Noite!')
