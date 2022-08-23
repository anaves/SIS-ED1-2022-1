lista = [1, 10, 2, 10, 3, 10, 4, 5, 6]

print(f'Ha {lista.count(10)} ocorrencias do valor 10')

print(lista)
lista.insert(3,50)
print(lista)

print('Posicao que encontrou determinado valor (10) na lista')
print(lista.index(10))
if 15 in lista:
    print('Posicao de valor que nao esta na lista (15)')
    print(lista.index(15))
