#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o úsuario tentar descobrir qual foi o número escolhido pelo computador. o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randrange
numComputador = randrange(0,5)
print(numComputador)

print('Vamos brincar de adivinha')
numUsuario = int(input('Digite um número entre 0 e 5: '))
print('processando ...')

if numComputador == numUsuario:
    print('=-'*40)
    print('Parabéns! Você ganhou. Eu realmente pensei no número {}'.foramt(numComputador ))
    print('=-'*40)
else:
    print('=-'*40)
    print('Que pena! infelizmente você perdeu. Eu pensei no número {} e não no {}'.format(numComputador,numUsuario))
    print('=-'*40)