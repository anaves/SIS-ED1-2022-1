texto = "Este é um exemplo de texto que vamos justificar usando o nosso programa."
n_colunas = int(input('quantas colunas: '))
print(len(texto))
print('texto original: ')
print(texto)

for i in range(int(len(texto)/n_colunas)):
    inicio = i*n_colunas
    fim = inicio + n_colunas
    parte = texto[inicio:fim]    
    print(f'{parte}')

if fim < len(texto):
    print(texto[fim:])

