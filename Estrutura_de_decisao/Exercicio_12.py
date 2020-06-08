salario_hora = float(input('Qual o valor da hora trabalhada?\n'))
hora_trab = int(input('Quantas horas trabalhou no mês?\n'))

salario_bruto = hora_trab * salario_hora

if salario_bruto < 900:
    print(f"Salário Bruto: ({salario_hora} * {hora_trab})\t\t: R$ {salario_bruto}")
    print('(-) IR (isento)\t\t\t\t    : R$ 0,0')
    inss = (salario_bruto * 10) / 100
    print(f'(-) INSS (10%)\t\t\t\t    : R$ {inss}')
    fgts = (salario_bruto * 11) / 100
    print(f'FGTS (11%)\t\t\t\t        : R$ {fgts}')
    print(f'Total de descontos\t\t\t    : R$ {inss}')
    salario_liquido = salario_bruto - inss
    print(f'Salário liquido\t\t\t\t    : R$ {salario_liquido}')
elif 900 <= salario_bruto < 1500:
    print(f"Salário Bruto: ({salario_hora} * {hora_trab})\t\t: R$ {salario_bruto})")
    ir = (salario_bruto * 5) / 100
    print(f'(-) IR (5%)\t\t\t\t        : R$ {ir}')
    inss = (salario_bruto * 10) / 100
    print(f'(-) INSS (10%)\t\t\t\t    : R$ {inss}')
    fgts = (salario_bruto * 11) / 100
    print(f'FGTS (11%)\t\t\t\t        : R$ {fgts}')
    descontos = inss + ir
    print(f'Total de descontos\t\t\t    : R$ {descontos}')
    salario_liquido = salario_bruto - descontos
    print(f'Salário liquido\t\t\t\t    : R$ {salario_liquido}')
elif 1500 <= salario_bruto <2500:
    print(f"Salário Bruto: ({salario_hora} * {hora_trab})\t\t: R$ {salario_bruto})")
    ir = (salario_bruto * 10) / 100
    print(f'(-) IR (10%)\t\t\t\t      : R$ {ir}')
    inss = (salario_bruto * 10) / 100
    print(f'(-) INSS (10%)\t\t\t\t    : R$ {inss}')
    fgts = (salario_bruto * 11) / 100
    print(f'FGTS (11%)\t\t\t\t        : R$ {fgts}')
    descontos = inss + ir
    print(f'Total de descontos\t\t\t    : R$ {descontos}')
    salario_liquido = salario_bruto - descontos
    print(f'Salário liquido\t\t\t\t    : R$ {salario_liquido}')
elif salario_bruto >= 2500:
    print(f"Salário Bruto: ({salario_hora} * {hora_trab})\t\t: R$ {salario_bruto}")
    ir = (salario_bruto * 20) / 100
    print(f'(-) IR (20%)\t\t\t\t    : R$ {ir}')
    inss = (salario_bruto * 10) / 100
    print(f'(-) INSS (10%)\t\t\t\t    : R$ {inss}')
    fgts = (salario_bruto * 11) / 100
    print(f'FGTS (11%)\t\t\t\t        : R$ {fgts}')
    descontos = inss + ir
    print(f'Total de descontos\t\t\t    : R$ {descontos}')
    salario_liquido = salario_bruto - descontos
    print(f'Salário liquido\t\t\t\t    : R$ {salario_liquido}')
else:
    print ('Entradas inválidas.')
