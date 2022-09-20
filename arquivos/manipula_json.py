import json

def abrir_arquivo(url):
    dados = None
    with open(url, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)       
    return dados

def informacoes(reg):
    print(f'Nome: {reg["nome"]}')
    print(f'CPF: {reg["cpf"]}')
    print(f'e-mail: {reg["email"]}')
    print(f'endereco: {reg["endereco"]}')
    print(f'telefone: {reg["telefone"]}')
    print(f'data nascimento: {reg["dataNascimento"]}')
    print('-'*30)

def listar_todos(dados):
    print('--- Listar todos ---')
    for reg in dados:
        informacoes(reg)

def listar_por_cpf(dados, cpf):
    print(f'Buscar CPF: {cpf}')
    for reg in dados:
        if reg['cpf'] == cpf:
            informacoes(reg)
            return True
    print('Nao encontrado')
    return False
    
if __name__== "__main__":
    base_dados = abrir_arquivo("./files/cliente.json")
    listar_todos(base_dados)
    listar_por_cpf(base_dados,'751.535.720-17')