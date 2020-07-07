"""Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará."""
import time
def msg(msg):
    tamanho = len(msg)
    print('-'*tamanho)
    print(msg)
    print('-'*tamanho)

while True:
    msg('Sistema de ajuda Pyhelp')
    resp = input('Função ou biblioteca [FIM para siar]: ')
    if resp != 'FIM':
        help(resp)
        print()
    else:
        msg("Encerrando ...")
        time.sleep(1)
        break