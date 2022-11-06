a = int(input('valor a: '))
b = int(input('valor b: '))
print('antes')
print(f'a = {a}')
print(f'b = {b}')

a,b = b,a

print('depois')
print(f'a = {a}')
print(f'b = {b}')