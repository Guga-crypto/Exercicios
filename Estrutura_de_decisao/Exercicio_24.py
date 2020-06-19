num_1 = int(input('Digite um valor: '))
num_2 = int(input('Digite outro valor: '))
print('\n\t\t\t- Escolha uma operação -')
op = int(input('\n1 - Adição\t2 - Subtração\t3 - Multiplicação\t4 - divisão\n'))

if op == 1:
    resultado = num_1 + num_2
    print(f'{num_1} + {num_2} = {resultado}')
    par_impar = resultado % 2
    if par_impar == 0:
        print('Par.')
    else:
        print('Impar.')
    if resultado > 0:
        print('Positivo.')
    else:
        print('Negativo')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal.')
        print(f'Arredondando para baixo: {round(resultado-0.5)}')
        print(f'Arredondando para cima: {round(resultado+0.5)}')
elif op == 2:
    resultado = num_1 - num_2
    print(f'{num_1} - {num_2} = {resultado}')
    par_impar = resultado % 2
    if par_impar == 0:
        print('Par.')
    else:
        print('Impar.')
    if resultado > 0:
        print('Positivo.')
    else:
        print('Negativo')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal.')
        print(f'Arredondando para baixo: {round(resultado - 0.5)}')
        print(f'Arredondando para cima: {round(resultado + 0.5)}')
elif op == 3:
    resultado = num_1 * num_2
    print(f'{num_1} * {num_2} = {resultado}')
    par_impar = resultado % 2
    if par_impar == 0:
        print('Par.')
    else:
        print('Impar.')
    if resultado > 0:
        print('Positivo.')
    else:
        print('Negativo')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal.')
        print(f'Arredondando para baixo: {round(resultado - 0.5)}')
        print(f'Arredondando para cima: {round(resultado + 0.5)}')
elif op == 4:
    resultado = num_1 / num_2
    print(f'{num_1} / {num_2} = {resultado}')
    par_impar = resultado % 2
    if par_impar == 0:
        print('Par.')
    else:
        print('Impar.')
    if resultado > 0:
        print('Positivo.')
    else:
        print('Negativo')
    if resultado == round(resultado):
        print('Inteiro')
    else:
        print('Decimal.')
        print(f'Arredondando para baixo: {round(resultado - 0.5)}')
        print(f'Arredondando para cima: {round(resultado + 0.5)}')
else:
    print('Operação inválida!')
