salario_hr = float(input('Quanto você ganha por hora?\n'))
hr_mes = float(input('Quantas horas trabalhou no mês?\n'))

salario_bruto = salario_hr * hr_mes
desc_inss = (salario_bruto * 8) / 100
desc_sind = (salario_bruto * 5) / 100
desc_ir = (salario_bruto * 11) / 100
total_desc = desc_inss + desc_sind + desc_ir
salario_liquido = salario_bruto - desc_ir - desc_inss - desc_sind

print(f'\nSeu salário bruto é igual a {salario_bruto} reais.')
print(f'\nVocê pagou {desc_inss} reais ao INSS.')
print(f'\nVocê pagou {desc_sind} reais ao Sindicato')
print(f'\nSeu salário líquido é {salario_liquido} reais.')
print(f'\nO total de desconto é {total_desc} reais.')



