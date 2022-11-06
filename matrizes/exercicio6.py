import random as r
#import util
from util import imprimir

matriz = []

for i in range(6):
    linha = []
    nome = input('Digite o nome do competidor: ')
    linha.append(nome)
    for v in range(10):
        linha.append(r.randint(50,500))
    matriz.append(linha)

#util.imprimir(matriz)
imprimir(matriz)