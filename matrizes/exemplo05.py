import random as rnd
import requests
pessoas = []
aux = requests.get('https://gerador-nomes.wolan.net/apelidos/11').json()
for i in range(10):
    registro = [aux[i], rnd.randint(18,108)]
    pessoas.append(registro)
print("-----")
print(pessoas)
# registro da linha 0 como sendo menor
menor_idade = pessoas[0][1]
indice_menor = 0
for linha in range(1, len(pessoas)):
    if pessoas[linha][1] < menor_idade:
        menor_idade = pessoas[linha][1]
        indice_menor = linha
print('-----')
print(f'menor idade {menor_idade}')
print(f'nome: {pessoas[indice_menor][0]}')
