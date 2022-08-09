nomes = []

#nomes[0] = 'Cebolinha' # forma errada
nomes.append('Cebolinha')
tmp = input('Digite um nome: ')
nomes.append(tmp)
nomes.append(input('Digite outro nome: '))
for i in range(len(nomes)):
    print(f'posicao {i}: {nomes[i]}')