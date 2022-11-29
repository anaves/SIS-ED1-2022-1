from fila import Fila

# PROGRAMACAO ORIENTADA A OBJETOS
if __name__ == '__main__':
    # objeto clientes do tipo Fila
    clientes = Fila()
    clientes.adicionar("Cascao")
    #print(clientes.info())
    clientes.adicionar("Cebolinha")
    #print(clientes.info())
    clientes.adicionar("Monica")

    # atender
    elemento =  clientes.remover()
    print('------ ATENDEU ------')
    print(elemento)
    print('---------------------')
    print(clientes.info())
    print('***********')
    #print(clientes.remover()) # Cebolinha
    ##print(clientes.remover()) # Monica
    #print(clientes.remover()) ### erro


    produtos = Fila()
    produtos.adicionar('Chave')
    
    print(clientes.info())
    print(produtos.info())


