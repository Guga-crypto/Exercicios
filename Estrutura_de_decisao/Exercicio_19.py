num = int(input('Digite um número menor que 1000: '))

if 0 < num < 1000:
    unidade = num % 10
    num = (num - unidade) / 10
    dezena = num % 10
    num = (num - dezena) / 10
    centena = num
    dezena = int(dezena)
    centena = int(centena)
    print(f'{centena}, {dezena}, {unidade}')
else:
    print('Valor inválido.')
