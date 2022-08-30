# Faça um programa que simule um lançamento de
# dados. Lance o dado 100 vezes e armazene os resultados
# em um vetor. Depois, monte um outro vetor contendo
# quantas vezes cada valor foi obtido. Imprima os dois
# vetores. Use a função random.randint(1,6) para gerar
# números aleatórios, simulando os lançamentos dos dados.
import random
numeros_sorteados = []
for n in range(200):
    numero = random.randint(1,6) # gerou o numero
    numeros_sorteados.append(numero) # armazenou o numero
    #print(f'sorteado: {numero}')
print('--------------')
#print(numeros_sorteados)
ocorrencias=[]
for n in range(1,7):
    qtd = numeros_sorteados.count(n)
    ocorrencias.append(qtd)
    print(f'numero {n}',end=' ')
    print('='*qtd)