'''Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai continuar.No final,mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
contador = 0
totgasto = 0
produtoCaro = 0
menor = 0
nomeBarato = ''

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    totgasto += preco
    contador += 1
    if preco > 1000:
        produtoCaro += 1

    if contador == 1 or preco < menor:
        menor = preco
        nomeBarato = nome
    cont = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi de R${totgasto:.2f}.')
print(f'{produtoCaro} produtos custam mais de mil reais.')
print(f'O produto mais barato foi {nomeBarato} que custa R${menor}')