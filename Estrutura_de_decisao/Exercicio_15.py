lado_1 = int(input('Digite o primeiro lado do triângulo: '))
lado_2 = int(input('Digite o segundo lado do triângulo: '))
lado_3 = int(input('Digite o terceiro lado do triângulo: '))

if (lado_2 - lado_3) < lado_1 < (lado_2 + lado_3) and (lado_1 - lado_3) < lado_2 < (lado_1 + lado_3) and (lado_1 - lado_2) < lado_3 < (lado_1 + lado_2):
    print('É um triângulo...')
    if lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print('Escaleno.')
    elif lado_1 == lado_2 != lado_3 or lado_2 == lado_3 != lado_1 or lado_3 == lado_1 != lado_2:
        print('Isosceles.')
    elif lado_1 == lado_2 == lado_3:
        print('Equilátero.')
    else:
        print('Erro!')
else:
    print('Medidas erradas.')





