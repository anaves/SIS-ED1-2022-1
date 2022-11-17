
def imprime_asterisco(tamanho):
    print('*' * tamanho)

def menu():
    imprime_asterisco(15)
    print('1- Somar')
    print('2- Subtrair')
    print('3- Sair')
    imprime_asterisco(15)

def adicao(x, y = 5):
    print("adicao...")
    return x+y

def subtracao():
    print('subtracao...')

def opcao():
    op = 0
    while op != 3:
        menu()
        op = int(input('Digite sua opcao: '))
        if op < 1 or op > 3:
            print('opcao invalida')
        elif op ==1:
            r = adicao(10,2) # y assumiu valor 2
            #r = adicao(10)  # y assumiu valor padrao = 5
            print(f'adicao = {r}')
        elif op == 2:
            subtracao()
        elif op == 3:
            print('saindo...')

if __name__ == '__main__':
    opcao()