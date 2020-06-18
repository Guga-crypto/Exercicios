print('\n\t\t- Caixa eletrônico -')
print('\nNotas Dísponiveis: 1, 5, 10, 50 e 100')
print('\nValor minimo de saque: R$ 10,00')
print('Valor máximo de saque: R$ 600,00')
saque = int(input('\nDigite o valor a ser sacado: '))

cem = int(saque / 100)
saque = saque % 100

cinquenta = int(saque / 50)
saque = saque % 50

dez = int(saque / 10)
saque = saque % 10

cinco = int(saque / 5)
saque = saque % 5

um = saque

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  1,00 = ', um)
