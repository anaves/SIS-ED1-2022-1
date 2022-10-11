# preencher uma matriz 3x3
n_dimensao = 3
"""
0,0     0,1     0,2
1,0     1,1     1,2
2,0     2,1     2,2

[[]]


"""
matriz = []
for i in range(n_dimensao):
    matriz.append([])
    print(matriz)
    for j in range(n_dimensao):
        aux=input(f'insira o valor da linha {i} coluna {j}: ')
        aux = abs(int(aux))
        matriz[i].append(aux)
        print(matriz)

print('FINAL')
print(matriz)
qtd = 0
for l in range(n_dimensao):
    for c in range(n_dimensao):
        valor = matriz[l][c]
        print(valor, end='\t')
        if valor%2 == 0: # valor eh par
            qtd += 1
    print('')
print(f'Tem {qtd} numeros pares na matriz')