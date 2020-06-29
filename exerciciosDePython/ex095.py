"""Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

jogador = dict()
lista = list()
time = list()
partidas = list()
qtdGols = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for i in range (0,p):
        lista.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = lista[:]
    for i in range(len(jogador['gols'])):
        qtdGols += jogador['gols'][i]
    jogador['total'] = qtdGols
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar[S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print("ERRO! responda apenas S ou N.")
    if resp == "N":
        break
print('-='*30)
print('cod ', end="")
for i in jogador.keys():
    print(f'{i:<15}',end="")
for k,v in enumerate(time):
    print(f"{k:>3}",end="")
    for d in v.values():
        print(f"{str(d):>15}",end="")
    print()
print('-='*30)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):    
        print(f"ERRo! não existe jogador com o código {busca}")
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i} fez {g} gols.')