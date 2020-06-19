#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
op = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é de {:.2f}'.format(math.hypot(op,adj))) #print usando a biblioteca math