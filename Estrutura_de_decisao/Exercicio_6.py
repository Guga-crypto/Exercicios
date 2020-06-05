x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
z = int(input('Digite um ultimo valor: '))

if x > y and x > z:
    print(f'{x} é o maior valor')
elif y > x and y > z:
    print(f'{y} é o maior valor.')
else:
    print(f'{z} é o maior valor.')
