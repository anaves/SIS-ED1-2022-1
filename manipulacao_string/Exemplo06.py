texto = 'Augusta Ada Byron King, Condessa de Lovelace (nascida Byron, 10 de dezembro de 1815 — 27 de novembro de 1852), atualmente conhecida como Ada Lovelace, foi uma matemática e escritora inglesa. Hoje é reconhecida principalmente por ter escrito o primeiro algoritmo para ser processado por uma máquina, a máquina analítica de Charles Babbage.'
texto = texto.lower()
termo = input('Digite termo a ser procurado: ')
posicao = texto.find(termo)
print(f'posicao: {posicao}')
if posicao >= 0:
    print(f'O termo: {termo} esta na posicao {posicao} do texto')
else:
    print(f'O termo: {termo} NAO esta no texto')