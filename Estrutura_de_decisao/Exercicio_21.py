print('\n\t\t- Caixa eletrônico -')
print('\nNotas Dísponiveis: 1, 5, 10, 50 e 100')
print('\nValor minimo de saque: R$ 10,00')
print('Valor máximo de saque: R$ 600,00')
saque = int(input('\nDigite o valor a ser sacado: '))

nota_1 = 1
nota_2 = 5
nota_3 = 10
nota_4 = 50
nota_5 = 100

if 10 <= saque < 50:
    unidade = saque % 10
    unidade = int(unidade)
    if 1 <= unidade < 5:
        print(f'{unidade} notas de 1')
    elif unidade == 5:
        print('Uma nota de 5.')
    elif 5 < unidade <= 9
        
    aux = saque % 10
    dezena = (saque - aux) / 10
    dezena = int(dezena)
    print(f'{dezena} notas de 10')

else:
    print('erro.')

