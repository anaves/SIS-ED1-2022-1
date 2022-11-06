lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = []

#verificar a maior lista
t1 = len(lista1)
t2 = len(lista2)
tamanho = max(t1, t2)
for i in range(tamanho):
    print(f'i = {i}')
    if i < t1:
        lista_intercalada.append(lista1[i])
    if i < t2:
        lista_intercalada.append(lista2[i])

print(f'lista 1: {lista1}')
print(f'lista 2: {lista2}')
print(f'lista intercalada: {lista_intercalada}')