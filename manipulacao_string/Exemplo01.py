nome = 'Maria Silva'
i = 0
tamanho = len(nome)
print('Percorrendo string com while')
while i < tamanho:
    print(f'{nome[i]}', end=' ')
    # atualizar i
    i = i + 1    # i += 1

print('\nPercorrendo string com for')
for i in range(tamanho):
    print(f'{i}: {nome[i]}', end=' ')

print('\nPercorrendo string com for - no index')
for caracter in nome:
    print(caracter, end='-')