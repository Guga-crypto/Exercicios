nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print('Aprovado!')
elif media == 10:
    print('Aprovado com distinção!')
else:
    print(f'Sua média foi {media}. Reprovado!')
