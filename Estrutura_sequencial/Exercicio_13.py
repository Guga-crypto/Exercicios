genero = input('Digite seu gênero(M/F): ')
altura = float(input('Digite sua altura: '))

if genero == 'M':
    result_1 = (72.2 * altura) - 58
    print(f'\nSeu peso ideal é {result_1}.')
elif genero == 'F':
    result_2 = (62.1 * altura) - 44.7
    print(f'\nSeu peso ideal é {result_2}.')
else:
    print('Erro! Algoritmo ultrapassado, esolha M ou F.')
