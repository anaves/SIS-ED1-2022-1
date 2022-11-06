"""
Codigo que calcula a media da turma com N aluno(a)s e posteriormente retorna
o(a)s aluno(a)s que estao acima da media da turma
"""
n_alunos =  40
soma_notas = 0
nomes = []      # armazena os nomes
notas = []      # armazena as notas
# entrada de dados
for it in range(n_alunos):
    aux_nome = input('Digite o nome: ')
    aux_nota = float(input(f'Digite a nota do(a) {aux_nome}: '))
    nomes.append(aux_nome)
    notas.append(aux_nota)
################################
print('-'*20)
print('Nomes: ')
print(nomes)
print('Notas: ')
print(notas)

media = sum(notas)/len(notas)  # sum(notas)/n_alunos
print('-'*30)
print(f'Pessoas acima da media {media:.1f}')
print('-'*30)

# for i in range(len(notas)):
#     nota = notas[i]
for i, nota in enumerate(notas):
    if nota > media:
        print(f'Nome: {nomes[i]}')
print('-'*20)