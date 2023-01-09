perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        "resposta": {
            'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 'Nenhuma'
        },
        'resposta_certa': 'c',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3 + 2?',
        "resposta": {
            'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 'Nenhuma'
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 2 / 2?',
        "resposta": {
            'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 'Nenhuma'
        },
        'resposta_certa': 'a',
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 2 x 7?',
        "resposta": {
            'a': 1, 'b': 14, 'c': 4, 'd': 5, 'e': 'Nenhuma'
        },
        'resposta_certa': 'b',
    },
    'pergunta 5': {
        'pergunta': 'Quanto é 2 - 2?',
        "resposta": {
            'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 'Nenhuma'
        },
        'resposta_certa': 'e',
    },
}


nota = 0
for k, v in perguntas.items():
    print(f'\n{k.title()}: {v["pergunta"]}')
    print('Opções: ')
    for op, r in v['resposta'].items():
        print(f'\t{op}) {r}')
    while True:
        res = input(str('Resposta: '))
        if res.strip().lower() in 'abcde':
            break
        else:
            print('Digite uma opção válida!')
    if res == v['resposta_certa']:
        nota += 2

if nota != 0:
    certas = nota / 2
else:
    certas = 0
porcentagem = certas / len(perguntas) * 100
print(f'''\nNota: {nota}
      Acertos: {certas:.0f}
      Porcentagem de acertos: {porcentagem:.0f}%''')




