#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
def tabuada(x):                             #função que recebe um número e retorna a sua tabuada
    print('{} x 1  = {}'.format(x,(x*1)))
    print('{} x 2  = {}'.format(x,(x*2)))
    print('{} x 3  = {}'.format(x,(x*3)))
    print('{} x 4  = {}'.format(x,(x*4)))
    print('{} x 5  = {}'.format(x,(x*5)))
    print('{} x 6  = {}'.format(x,(x*6)))
    print('{} x 7  = {}'.format(x,(x*7)))
    print('{} x 8  = {}'.format(x,(x*8)))
    print('{} x 9  = {}'.format(x,(x*9)))
    print('{} x 10 = {}'.format(x,x*10))

num = int(input('Digite um número para ver sua tabuada: '))
tabuada(num)    #chamando a função