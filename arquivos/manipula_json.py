import json
import pstats

def abrir_arquivo(url):
    dados = None
    with open(url, encoding="utf-8") as arquivo:
        dados = json.load(arquivo)       
    arquivo.close()
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

def adiciona():
    print('----- Adiciona novo registro -----')
    registro = {}
    registro['nome'] = input('Digite o nome: ')
    registro['cpf'] = input('Digite o CPF: ')
    registro['email'] = input('Digite o e-mail: ')
    registro['telefone'] = input('Digite o telefone: ')
    registro['endereco'] = input('Digite o endereco: ')
    registro['dataNascimento'] = input('Digite a data de nascimento: ')
    print(registro)
    return registro
    

def salvar(dados, url):
    # transformar de dict para json
    # serializar json
    objeto_json = json.dumps(dados, indent=4)
    with open(url, "w") as saida:
        saida.write(objeto_json)

# Exercicio - implementar o metodo que exclui um determinado registro e posteriormente salve os dados no arquivo sem o registro excluido da base dados
def excluir(dados, cpf):
    for indice,registro in enumerate(dados):
        pass


if __name__== "__main__":
    url = "./files/cliente.json"
    base_dados = abrir_arquivo(url)
    print(type(base_dados))
    print(type(base_dados[0]))
    print(base_dados)
    # listar_todos(base_dados)
    # listar_por_cpf(base_dados,'751.535.720-17')
    #novo_registro = adiciona()
    #base_dados.append(novo_registro)
    #salvar(base_dados,url)

    