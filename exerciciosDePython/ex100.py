"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
numeros = list()

def sorteia():
    for i in range(0,5):
        numeros.append(randint(0,100))

def somaPar():
    soma = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f"A soma dos números pares da lista {numeros} é {soma}.")

sorteia()
somaPar()
