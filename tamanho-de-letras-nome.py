"""
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
    ou menos escreva "seu nome é curto; se tiver entre 5 e 6 letras, escreva seu
    nome é normal, maior que 6, escreva seu nome é grande."
"""
print('Verificador do tamanho do nome.')
primeiro_nome = str(input('Seu primeiro nome: ')).strip()
tamanho = len(primeiro_nome)
if tamanho:
    if tamanho <= 4:
        print('Seu nome é pequeno.')
    elif tamanho < 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é grande.')

