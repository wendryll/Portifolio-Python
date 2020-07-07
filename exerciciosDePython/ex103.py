"""Faça um progra que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome,gols):
    """
    -> exibir ficha do jogador.
            parametro nome:(opcional) recebe nome do jogador
            parametro gols:(opcional) recebe o numero de gols
            return retorna os dados do jogador
    """
    if nome != '' and gols != '':
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif nome!= '' and gols == '':
        return print(f'O jogador {nome} fez 0 gol(s) no campeonato.')
    elif nome == '' and gols != '':
        return print(f"O jogador <desconhecido> fez {gols} gol(s) no campeonato.")
    else:
        return print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')


nome = str(input('Nome: ')).strip()
gols = str(input('Gols: ')).strip()
ficha(nome,gols)