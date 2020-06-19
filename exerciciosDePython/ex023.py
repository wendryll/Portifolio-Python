#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = input('Digite um número entre 0 e 9999: ')
print('O número digitado possui')
print('Unidade:{}'.format(num[0]))
print('Dezena:{}'.format(num[1]))
print('Centena:{}'.format(num[2]))
print('Milhar:{}'.format(num[3]))