import random as r
from util import imprimir
matriz=[]
n = 4
for l in range(n):
    linha = []
    for c in range(n):
        linha.append(r.randint(0,1000))
    matriz.append(linha)
imprimir(matriz)
print('-------------')
transposta=[]
for c in range(n):
    linha=[]
    for l in range(n):
        linha.append(matriz[l][c])
    transposta.append(linha)
imprimir(transposta)
print('---------')
print(transposta)
# import numpy as np
# a = np.array(matriz)
# print(a)
# b = np.transpose(a)
# print(b)