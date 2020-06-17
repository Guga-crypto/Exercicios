print('\n\t\t- Caixa eletrônico -')
print('\nNotas Dísponiveis: 1, 5, 10, 50 e 100')
print('\nValor minimo de saque: R$ 10,00')
print('Valor máximo de saque: R$ 600,00')
saque = float(input('Digite o valor a ser sacado: '))

nota_1 = 1
nota_2 = 5
nota_3 = 10
nota_4 = 50
nota_5 = 100

if 10 <= saque < 50:
    print('Opções:')
    print('\tR$ 1,00 \t- 9 notas')
    print('\tR$ 5,00 \t- 2 notas')
    print('\tR$ 10,00 \t- 4 notas')
    print('\tR$ 50,00 \t- 1 nota')
    print('\tR$ 100,00 \t- indisponível')
