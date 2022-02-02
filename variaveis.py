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

print(f"""
Nome: {nome:>14}
Idede: {idade:>11} Anos
altura: {altura:>12.2f}m
peso: {peso:>15.2f}Kg
IMC: {imc:>16.2f}
Maior de Idade? {e_maior}
    """)
