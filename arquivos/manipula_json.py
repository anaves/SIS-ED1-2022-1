import json

dados = None
with open("cliente.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(len(dados))

print('Exemplo de busca')
for registro in dados:
    #print(f"cpf: {registro['cpf']}")    
    if '751.545.720-17' in registro['cpf']:
        print(f"nome: {registro['nome']}")


    