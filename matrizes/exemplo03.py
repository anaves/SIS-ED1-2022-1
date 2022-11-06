notas = [] # para armazenar as notas da turma
n_alunos =  3
n_provas = 5

for linha in range(n_alunos):
    print(f"Notas do aluno {linha+1}")
    notas_aluno = []
    for coluna in range(n_provas):
        nota = float(input(f'Nota {coluna+1}: '))
        notas_aluno.append(nota)
    notas.append(notas_aluno)
print("-"*20)
print(notas)

print("-"*20)
for i in range(len(notas)):
    print(notas[i])