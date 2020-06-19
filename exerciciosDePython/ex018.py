#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tengente desse ângulo.
import math
angulo = int(input('Digite o angulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {}° possui o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(angulo,seno,cosseno,tangente))