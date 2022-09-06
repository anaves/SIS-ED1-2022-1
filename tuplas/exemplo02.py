def calcula_pagamento(horas_trabalhadas, valor_hora):
    salario_base =  horas_trabalhadas*valor_hora*4
    inss = salario_base*0.08
    return salario_base, inss


salario_bruto, desconto = calcula_pagamento(40, 35.0)

print(f'Salario Bruto: R$ {salario_bruto}')
print(f'Desconto: R$ {desconto}')
print(f'Salario liquido: {salario_bruto-desconto}')
print('-'*20)