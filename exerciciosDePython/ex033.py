#Faça um programa que leia três números e mostre qual é o maior e o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num2 > num3:
    print('O maior número é {} e o menor é {}.'.format(num1,num3))
elif num1 > num2 and num3 > num2 and num1 > num3:
    print('O maior número é {} e o menor é {}.'.format(num1,num2))
elif num2 > num1 and num1 > num3:
    print('O maior número é {} e o menor é {}.'.format(num2,num3))
elif num2 > num1 and num3 > num1 and num2 > num3:
    print('O maior número é {} e o menor é {}.'.format(num2,num1))
elif num3 > num1 and num2 > num1:
    print('O maior número é {} e o menor é {}.'.format(num3,num1))
elif num1 == num2 and num1 == num3 and num2 == num3:
    print('Os números digitados são iguais')
else:
    print('O maior número é {} e o menor é {}.'.format(num3,num2))