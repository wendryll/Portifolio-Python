'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
sem usar o sort.No fina ,mostre a lista ordenada na tela.'''
lista = []
for i in enumerate(range(1,6)): 
    lista.append(int(input(f'Digite o valor a inserir na lista: ')))
print()
k = 0
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            k = lista[j]
            lista[j] = lista[i]
            lista[i] = k
print(lista)
