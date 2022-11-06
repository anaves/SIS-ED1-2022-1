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
        matriz[i].append([])
        print(matriz)
        for k in range(n_dimensao):
                aux=input(f'insira o valor da linha {i} coluna {j}: ')
                aux = abs(int(aux))
                matriz[i][j].append(aux)
                print(matriz)

print('FINAL')
print(matriz)
