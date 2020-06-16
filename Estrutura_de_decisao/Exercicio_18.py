dia = int(input('Digite o dia (dd): '))
mes = int(input('Digite o mês (mm): '))
ano = int(input('Digite o ano (aaaa): '))

bissexto = ano % 4

if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0 and mes != 2:
    print(f'{dia}/{mes}/{ano} é uma data válida.')
elif 1 <= dia <= 29 and mes == 2 and bissexto == 0:
    print(f'{dia}/{mes}/{ano} é uma data válida e é um ano bissexto.')
else:
    print(f'{dia}/{mes}/{ano} não é uma data válida.')





