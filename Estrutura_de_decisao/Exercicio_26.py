print('\t-Tipos de Combustível-\n\n\tG - Gasolina\tA - Álcool\n')

#Qual combustivel irá colocar
tipo_comb = input('Escolha qual tipo de combustível (G/A): ')

#Quantidade de litros
litros = int(input('Quantos litros irá colocar? '))

gas = 2.5
alcool = 1.9

if tipo_comb == 'A' or 'a':
    if 0 < litros <= 20:
        #Calcula a quantidade total do desconto
        desconto = litros * 3
        #Calcula o custo bruto do combustivel colocado
        custo = litros * alcool
        #Calcula o desconto total
        desconto_final = (custo * desconto) / 100
        #Calcula o custo liquido
        custo_final = custo - desconto_final
        print(f'Valor total: R$ {custo:.2f}')
        print(f'Desconto: {desconto}%')
        print(f'Valor do desconto: R$ {desconto_final:.2f}')
        print(f'Com um total de {litros}l, você irá pagar R${custo_final:.2f} reais.')
    elif litros > 20:
        # Calcula a quantidade total do desconto
        desconto = litros * 5
        # Calcula o custo bruto do combustivel colocado
        custo = litros * alcool
        # Calcula o desconto total
        desconto_final = (custo * desconto) / 100
        # Calcula o custo liquido
        custo_final = custo - desconto_final
        print(f'Valor total: R$ {custo:.2f}')
        print(f'Desconto: {desconto}%')
        print(f'Valor do desconto: R$ {desconto_final:.2f}')
        print(f'Com um total de {litros}l, você irá pagar R${custo_final:.2f} reais.')
    else:
        print('Quantidade errada.')
else:
    print('Entrada Errada.')

if tipo_comb == 'G' or 'g':
    if 0 < litros <= 20:
        desconto = litros * 4
        custo = litros * gas
        desconto_final = (custo * desconto) / 100
        custo_final = custo - desconto_final
        print(f'Valor total: R$ {custo:.2f}')
        print(f'Desconto: {desconto}%')
        print(f'Valor do desconto: R$ {desconto_final:.2f}')
        print(f'com um total de {litros}l, você irá pagar R${custo_final:.2f} reais.')
    elif litros > 20:
        desconto = litros * 6
        custo = litros * gas
        desconto_final = (custo * desconto) / 100
        custo_final = custo - desconto_final
        print(f'Valor total: R$ {custo:.2f}')
        print(f'Desconto: {desconto}%')
        print(f'Valor do desconto: R$ {desconto_final:.2f}')
        print(f'com um total de {litros}l, você irá pagar R${custo_final:.2f} reais.')
    else:
        print('Quantidade errada.')
else:
    print('Entrada inválida.')
