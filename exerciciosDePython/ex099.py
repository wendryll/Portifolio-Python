"""Faça um programa que leia uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

def maior(*num):
    maior = 0
    for i in range(len(num)):
        if maior < num[i]:
            maior = num[i]
    print(f'foram informados {len(num)} valores. O maior valor é {maior}.')

maior(2,9,4,5,7,1)