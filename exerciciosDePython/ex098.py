"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
seu programa tem que realizar três contagens através da função criada:
A)de 1 até 10, de 1 em 1
B)de 10 até 0,de 2 em 2
C)uma contagem personalizada."""
from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        print('-='*30)
        cont = inicio
        while cont <= fim:
            print(f"{cont} ",end="",flush=True)
            sleep(1)
            cont += passo
        print('FIM!')
    else:
        print('-='*30)
        cont = inicio 
        while cont >= fim:
            print(f'{cont} ',end="",flush=True)
            cont -= passo
            sleep(1)
        print('FIM!')

contador(1,10,1)
contador(10,0,2)
print("-="*20)
inicio = int(input("Inicio: "))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)