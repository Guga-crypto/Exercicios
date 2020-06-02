peso = float(input('Dgite o peso do peixe: '))

excesso = peso - 50.0

if excesso >= 1:
    multa = excesso * 4.0
    print(f'\nVocê excedeu em {excesso}kg e deve pagar uma multa de {multa} reais.')
else:
    print('\nNenhuma multa deverá ser paga.')

