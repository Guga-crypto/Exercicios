x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))
z = int(input('Digite um valor: '))

if x > y and x > z:
    print(f'{x} é o maior valor.')
elif y > x and y > z:
    print(f'{y} é maior valor.')
else:
    print(f'{z} é o maior valor.')

if x < y and x < z:
    print(f'{x} é o menor valor.')
elif y < x and y < z:
    print(f'{y} é menor valor.')
else:
    print(f'{z} é o menor valor.')
