"""
    Desafio -> Mostrar os valores dentro das variáveis
    e calcular o Índice de masa corporal.
"""
nome = "João"
idade = 40
altura = 1.60
peso = 65
imc = peso / (altura ** 2)

if idade > 18:
    e_maior = 'Sim'
else:
    e_maior = 'Não'

dados = ['nome', 'idade', 'altura', 'peso', 'imc', 'Maior de Idade']
tamanho = []

for quantidade in enumerate(dados):
    count = 30 - len(quantidade)
    tamanho.append(count)


print(f"""
{'Nome:':<{tamanho[0]}} {nome}
{'Idede:':<{tamanho[1]}} {idade} Anos
{'altura:':<{tamanho[2]}} {altura:.2f}m
{'peso:':<{tamanho[3]}} {peso:.2f}Kg
{'IMC:':<{tamanho[4]}} {imc:.2f}
{'Maior de Idade:':<{tamanho[5]}} {e_maior}
    """)
