'''Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Entre com o nome: ')))
    dados.append(float(input('Entre com o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = input('Deseja continuar[S/N]: ')[0].strip().upper()
    if cont in 'N':
        break

print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}KG ', end ='')
for i in range(len(pessoas)):
    for j in range(len(pessoas[i])):
        if pessoas[i][j] == maior:
            print(f'e seu nome é {pessoas[i][j-1]}')
print(f'O menor peso foi de {menor}KG ', end='')
for i in range(len(pessoas)):
    for j in range(len(pessoas[i])):
        if pessoas[i][j] == menor:
            print(f'e seu nome é {pessoas[i][j-1]}')