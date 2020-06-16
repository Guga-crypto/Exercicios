ano = int(input('Digite o ano: '))

bissexto = ano % 4

if bissexto == 0:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto')
