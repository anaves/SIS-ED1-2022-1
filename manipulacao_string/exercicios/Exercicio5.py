alvo = input('Digite palavra 1: ')
palavra = input('Digite palavra 2: ')

alvo_tmp = sorted(alvo.replace(' ','').lower())
palavra_tmp = sorted(palavra.replace(' ','').lower())

if alvo_tmp == palavra_tmp:
    print('anagrama')
    
print(alvo_tmp)
print(palavra_tmp)