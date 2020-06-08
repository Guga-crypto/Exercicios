produto_1 = float(input('Digite o preço do primeiro produto: '))
produto_2 = float(input('Digite o preço do segundo produto: '))
produto_3 = float(input('Digite o preço do terceiro produto: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print('Sua melhor escolha é o produto 1')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('Sua melhor escolha é o produto 2')
else:
    print('Sua melhor escolha é o produto 3')
