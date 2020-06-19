'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, des considere-o.'''

soma = 0
for i in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        
print('A soma dos números pares digitados é {:.2f}.'.format(soma))