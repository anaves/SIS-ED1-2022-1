def calcula_media(v:list):
    media = sum(v)/len(v)
    return media    



a = [1,2,3,4,5]
ma = calcula_media(a)
print(f'ma: {ma}')

b = [1,20,3,4,5]
mb = calcula_media(b)
print(f'mb: {mb}')