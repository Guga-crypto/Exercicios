nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if 7 <= media <= 10:
    print(f'Aprovado! Sua média foi {media}.')
    if media == 10:
        print('Aprovado com distinção. Parabéns!')
elif 0 <= media < 7:
    print(f'Reprovado! Sua média foi {media}')
else:
    print('Entrada inválida.')
