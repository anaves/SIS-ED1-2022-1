# 3. Faça um programa que percorre um vetor e
# imprime na tela a média dos valores do vetor e o
# valor mais próximo da média. Exemplo:
# Vetor: [2.5, 7.5, 10.0, 4.0]
# Média: 6.0
# Valor mais próximo da média: 7.5

vetor = [2.5, 7.5, 10, 6.9, 2, 9.1]
print(f'vetor: {vetor}')
media = sum(vetor)/len(vetor)
print(f'media: {media}')
dist = []
for valor in vetor:
    dist.append(abs(valor-media))
print('Distancia')
print(dist)
minimo = min(dist)
print(f'minimo: {minimo}')
posicao_min = dist.index(minimo)
print(f'posicao: {posicao_min}')
print(f'valor mais proximo da media: {vetor[posicao_min]}')
