nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

if 9 < media <= 10:
    print(f'Sua primeira nota foi {nota_1} e a segunda {nota_2}')
    print(f'Sua média foi {media}')
    print('Conceito: A')
    print('Aprovado!')
elif 7.5 < media <= 9:
    print(f'Sua primeira nota foi {nota_1} e a segunda {nota_2}')
    print(f'Sua média foi {media}')
    print('Conceito: B')
    print('Aprovado!')
elif 6 < media <= 7.5:
    print(f'Sua primeira nota foi {nota_1} e a segunda {nota_2}')
    print(f'Sua média foi {media}')
    print('Conceito: C')
    print('Aprovado!')
elif 4 < media <= 6:
    print(f'Sua primeira nota foi {nota_1} e a segunda {nota_2}')
    print(f'Sua média foi {media}')
    print('Conceito: D')
    print('Reprovado!')
elif 0 < media <= 4:
    print(f'Sua primeira nota foi {nota_1} e a segunda {nota_2}')
    print(f'Sua média foi {media}')
    print('Conceito: E')
    print('Reprovado!')
else:
    print('Entrada inválida')
