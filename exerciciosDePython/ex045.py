'''Crie um programa que faça o computador jogar jokenpô com você'''

import random
import time

iten = ('pedra','papel','tesoura')

print('=-'*10,' JOKENPÔ','-='*10)

print('''[0] Pedra
[1] Papel
[2] Tesoura \n''')
jogada = int(input('Faça sua jogada: '))
computador = random.randint(0,2)
print('JO!')
time.sleep(1)
print('KEN!')
time.sleep(1)
print('PÔ!')
if jogada == computador:
    print('EMPATE')
elif jogada == 0 and computador == 2:
    print('VENCEU')
elif jogada == 1 and computador == 0:
    print('VENCEU')
elif jogada == 2 and computador == 1:
    print('VENCEU')
elif computador == 0 and jogada == 2:
    print('PERDEU')
elif computador == 1 and jogada == 0:
    print('PERDEU')
elif computador == 2 and jogada == 1:
    print('PERDEU')
else:
    print('Jogada invalida! tente novamente.')

print('O computador escolheu {} e você {}.'.format(iten[computador],iten[jogada]))