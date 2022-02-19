"""
    Criar 1 programa para fazer 2 contagens.
    Uma de 0 até 10 e a outra de 10 até 0,
    Tudo isso utilizando o mesmo laço de repetição.
"""
# Primeira solução
fim = 11
for count in range(0, fim, 1):
    print(count)
    if not count >= 10:
        continue
    else:
        print('Contagem regressiva!')
        for count in range(10, -1, -1):
            print(f'{count}')

# segunda solução
count_list = list(range(0, 10))
count_list += list(range(10, -1, -1))
print('#'*40)
for count in count_list:
    print(count)

# Terceira solução
print('Terceira opção')
fim = 10
inicio = 0
passo = 1
while True:
    print(inicio)
    inicio += passo
    if inicio == -1:
        break
    elif inicio == 10:
        inicio = fim
        passo = -1
        fim = 0

