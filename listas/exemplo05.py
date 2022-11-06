lista = [1, 10, 2, 10, 3, 10, 4, 10, 6]
cont = 0 # armazenar ocorrencias do valor 10

for e in lista:
    if e == 10:
        cont+=1

print(f'Ha {cont} ocorrencias do valor 10')

# for i, e in enumerate(lista):
#     print(f'index: {i} valor: {e}')

# for i in range(len(lista)):
#     e = lista[i]
#     print(f'indice: {i} valor: {e}')