'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

num = int(input('Digite um número(inteiro não negativos) para ver seu fatorial: '))
i = 1
fatorial = 1
while i <= num:
    fatorial = fatorial * i
    i += 1
print('o fatorial de {} é {}'.format(num,fatorial))