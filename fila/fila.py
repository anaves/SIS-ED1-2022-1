class Fila:
    # construtor
    def __init__(self):
        self.__dados = []
    
    def adicionar(self, conteudo):
        # adicionar no final
        self.__dados.append(conteudo)
        print(self.info())

    def remover(self):
        # remove do inicio
        if not self.eh_vazia():
            return self.__dados.pop(0)
        else:
            print('Lista vazia')
            print(self.info())
            return None
    
    def info(self):
        return self.__dados

    def eh_vazia(self):
        return len(self.__dados) == 0

