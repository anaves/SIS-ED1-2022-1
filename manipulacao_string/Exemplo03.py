numerador = 5
denominador = 3
divisao = numerador/denominador

print(f'{numerador} / {denominador} = {divisao:.2f}')

print(f'{12/10:.5f}')

divisao_str = f'R$ {divisao:.2f}'
print(divisao_str)
divisao_virg = divisao_str.replace('.',',') # substituir . por ,
print(divisao_virg)