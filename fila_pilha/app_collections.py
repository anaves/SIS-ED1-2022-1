from collections import deque
print('FILA')
fila = deque()
print(fila)
fila.append(3)
print(fila)
fila.append(6)
print(fila)
fila.append(9)
print(fila)             #[3,6,9]
print(fila.popleft())   #-> retira 3
print(fila)
print('PILHA')
pilha = deque()
print(pilha)
pilha.append(3)
print(pilha)
pilha.append(6)
print(pilha)
pilha.append(9)
print(pilha)        # [3,6,9]
print(pilha.pop())  # -> retira 9
print(pilha)
