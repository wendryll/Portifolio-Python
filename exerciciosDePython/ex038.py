#EScreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print('O número {} é maior.'.format(num1))
elif num1 < num2:
    print('O número {} é maior.'.format(num2))
else:
    print('Não existe número maior, ambos são iguais.')