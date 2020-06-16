dia = int(input('Digite o dia (dd): '))
mes = int(input('Digite o mês (mm): '))
ano = int(input('Digite o ano (aaaa): '))

bissexto = ano % 4

if 1 <= dia <= 31 and mes != 2:
    print(f'{dia} é válido.')
elif 1 <= dia <= 29 and mes == 2 and bissexto == 0:
        print(f'{dia} é válido')
else:
    print('Dia incorreto.')

if 1 <= mes <= 12:
    print(f'{mes} é válido.')
else:
    print('Mês incorreto')

if ano == 2020:
    print(f'{ano} é válido.')
else:
    print('Não é uma data atual.')

print(f'{dia}/{mes}/{ano} é uma data válida.')




