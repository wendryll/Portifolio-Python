'''Faça um programa que ajude um jogador da mega sena a criar palpites, o programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
lista = []
cont = 0

cont = int(input('Deseja jogar quantas vezes: '))
for i in range(0,cont):
    for i in range(0,6): 
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
        else:
            num = randint(1,60)
            lista.append(num)
    print(f'{lista}')
    lista.clear()
    sleep(1)