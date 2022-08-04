nome_completo = input('Digite o nome completo: ')
# dividir string pelo separador
nome_dividido = nome_completo.split(' ') 
print(nome_dividido)
primeiro_nome = nome_dividido[0].lower()
tamanho = len(nome_dividido)
# nome_dividido[-1] - acessar ultima posicao do vetor
sobrenome = nome_dividido[tamanho-1].lower() 
dominio = 'libertas.edu.br'
# concatenar string
email = primeiro_nome + '.' + sobrenome + '@' + dominio
print(email)