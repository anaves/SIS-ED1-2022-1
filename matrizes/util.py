def imprimir(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            print(matriz[l][c],end='\t')
        print('')