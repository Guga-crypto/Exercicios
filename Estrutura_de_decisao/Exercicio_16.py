a = int(input('Digite o valor de a: '))

if a == 0:
    print('Não é uma equação do segundo grau.')
elif a > 0:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Valores negativos. A equação não possui raizes iguais')
    elif delta == 0:
        x_1 = (-b + delta) / (2 * a)
        print(f'A equação tem somente uma raiz real equivalente a {x_1}')
    else:
        x_1 = (-b + delta) / (2 * a)
        x_2 = (-b - delta) / (2 * a)
        print(f'x¹ = {x_1}')
        print(f'x² = {x_2}')
else:
    print('Erro.')
