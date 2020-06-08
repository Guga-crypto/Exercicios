salario = float(input('Digite o valor do seu salário: '))

if salario < 280:
    aumento = (salario * 20) / 100
    reajuste = salario + aumento
    print(f'Seu salário antes do reajuste era {salario} reais.')
    print('Você ganhou um reajuste de 20%.')
    print(f'Você irá ganhar mais {aumento} reais em seu salário.')
    print(f'Seu salário passará a ser {reajuste} reais.')
elif salario >= 280 or salario < 700:
    aumento = (salario * 15) / 100
    reajuste = salario + aumento
    print(f'Seu salário antes do reajuste era {salario} reais.')
    print('Você ganhou um reajuste de 20%.')
    print(f'Você irá ganhar mais {aumento} reais em seu salário.')
    print(f'Seu salário passará a ser {reajuste} reais.')
elif salario >= 700 or salario < 1500:
    aumento = (salario * 10) / 100
    reajuste = salario + aumento
    print(f'Seu salário antes do reajuste era {salario} reais.')
    print('Você ganhou um reajuste de 20%.')
    print(f'Você irá ganhar mais {aumento} reais em seu salário.')
    print(f'Seu salário passará a ser {reajuste} reais.')
elif salario >= 1500:
    aumento = (salario * 5) / 100
    reajuste = salario + aumento
    print(f'Seu salário antes do reajuste era {salario} reais.')
    print('Você ganhou um reajuste de 20%.')
    print(f'Você irá ganhar mais {aumento} reais em seu salário.')
    print(f'Seu salário passará a ser {reajuste} reais.')
else:
    print('Erro.')
