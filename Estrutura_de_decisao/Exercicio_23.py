num = float(input('Numero original: '))

if num == round(num):
    print('Inteiro')
else:
    print('Decimal')
    print(f'Arredondado pra baixo: {round(num-0.5)}')
    print(f'Arredondado pra cima : {round(num+0.5)}')

