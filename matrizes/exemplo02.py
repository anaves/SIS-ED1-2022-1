notas = [[7, 10, 5, 8],
         [9, 8, 5, 7]]

soma_geral = 0
for linha in range(len(notas)):
    print(f"Notas do(a) aluno(a) {linha+1}")
    print(notas[linha])
    soma = 0
    for coluna in range(len(notas[linha])):
        # print(f'{linha} | {coluna}: ', end='')
        # print(notas[linha][coluna])
        soma += notas[linha][coluna]
    media = soma/len(notas[linha])
    soma_geral += media
    print(f'media aluno(a) {linha+1}: {media:.1f}')

media_turma = soma_geral/len(notas)
print('-'*15)
print(f'media turma: {media_turma:.1f}')