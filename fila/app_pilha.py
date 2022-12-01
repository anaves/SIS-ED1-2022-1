from pilha import Pilha
p = Pilha()

p.empilhar(3)
p.empilhar(6)
p.empilhar(9)
print(p.info())
print('Desempilhar')
print(p.desempilhar()) ## retira 9
print(p.info())