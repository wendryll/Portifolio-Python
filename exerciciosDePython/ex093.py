'''Crie um programa que leia gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitas em cada partida. No final, tudo isso será guardado em
um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()
lista = list()
qtdGols = 0
jogador['Nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range (0,p):
    lista.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = lista[:]
for i in range(len(jogador['gols'])):
    qtdGols += jogador['gols'][i]
jogador['total'] = qtdGols

print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols')
