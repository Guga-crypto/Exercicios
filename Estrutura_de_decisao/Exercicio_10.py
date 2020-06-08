print('\t\tM - matutino\tV - vespertino\tN - noturno')
opcao = input('\nEm que turno você estuda: ')

if opcao == 'M':
    print('Bom dia!')
elif opcao == 'V':
    print('Boa tarde!')
elif opcao == 'N':
    print('Boa noite!')
else:
    print('Entrada inválida!')
