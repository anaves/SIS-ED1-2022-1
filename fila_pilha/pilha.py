class Pilha:
    def __init__(self):
        self.dados = []
    
    def empilhar(self,valor):
        self.dados.append(valor)

    def desempilhar(self):
        return self.dados.pop(-1)
    
    def info(self):
        return self.dados