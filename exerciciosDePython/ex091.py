'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado'''

from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador3'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)
print('   Valores sorteados   ')
for k,v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = dict()
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('   ganhadores   ')
for i in range(len(ranking)):
    print(f'{ranking[i]}')