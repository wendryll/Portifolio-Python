'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
menor = maior = numeros[0]
print(f'Os números sorteados foram: {numeros}')
for i in range(len(numeros)):
    if maior < numeros[i]:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
print(f'O maior número é {maior} e o menor é {menor}.')