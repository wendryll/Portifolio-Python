#Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Impar.

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número digitado foi {} e ele é um numero par.'.format(num))
else:
    print('O número digitado foi {} e ele é impar.'.format(num))