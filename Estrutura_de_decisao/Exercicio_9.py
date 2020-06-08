x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if x > y > z:
    print(f'{x}, {y}, {z}')
elif x > z > y:
    print(f'{x}, {z}, {y}')
elif y > x > z:
    print(f'{y}, {x}, {z}')
elif y > z > x:
    print(f'{y}, {z}, {x}')
elif z > x > y:
    print(f'{z}, {x}, {y}')
elif z > y > x:
    print(f'{z}, {y}, {x}')
elif x == y or x == z or y == z:
    print('Inválido.')
else:
    print('Erro.')



