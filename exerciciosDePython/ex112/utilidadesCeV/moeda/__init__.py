def aumentar(preco=0,taxa=0,formato=False):
    res =  preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0,taxa=0,formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0,formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco=0,formato=False):
    res = preco / 2 
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'RS'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')

def resumo(preco = 0,aum = 0,dim = 0):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preco)}.')
    print(f'Aumentando {aum}% de {moeda(preco)} temos {aumentar(preco,aum,True)}.')
    print(f'Diminuindo {dim}% de {moeda(preco)} temos {diminuir(preco,dim,True)}.')
    print(f'O dobro de {moeda(preco)} é {dobro(preco,True)}.')
    print(f'A metade de {moeda(preco)} é {metade(preco,True)}.')
    print('-'*30)